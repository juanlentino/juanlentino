"""Rewrite the latest-notes list in README.md from the juanlentino.com notes feed.

Replaces the lines between the BLOG-POST-LIST markers with the newest notes,
tracking query strings removed. Standard library only. Exits non-zero when the
feed cannot be read or parsed, so the README is never blanked.
"""
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

FEED = "https://juanlentino.com/notes/feed/"
README = "README.md"
COUNT = 3
START = "<!-- BLOG-POST-LIST:START -->"
END = "<!-- BLOG-POST-LIST:END -->"


def clean(url):
    parts = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def main():
    req = urllib.request.Request(FEED, headers={"User-Agent": "juanlentino-profile-readme"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        root = ET.fromstring(resp.read())
    items = []
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        if title and link:
            items.append(f"- [{title.replace(']', '\\]')}]({clean(link)})")
        if len(items) == COUNT:
            break
    if not items:
        sys.exit("feed returned no notes; README left unchanged")

    text = open(README, encoding="utf-8").read()
    if START not in text or END not in text:
        sys.exit("markers missing from README; nothing written")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    new = head + START + "\n" + "\n".join(items) + "\n" + END + tail
    if new != text:
        open(README, "w", encoding="utf-8").write(new)
        print("updated:", *items, sep="\n")
    else:
        print("no change")


if __name__ == "__main__":
    main()
