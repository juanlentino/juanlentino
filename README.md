### Records are made by many hands. The credits rarely survive the trip.

I'm Juan. I've spent 15+ years making records between Buenos Aires and the U.S., founded Panacea Studio along the way, and have worked on about 110 releases since 2022 ([credits verified](https://juanlentino.com/music/)). Now I research how to prove who made what, at the moment it's made.

The short version: **detection guesses, provenance proves.** I write the papers, then build the small open tools that test them.

[**Sealed Record**](https://github.com/juanlentino/sealedrecord) checks a sealed session record end to end: hash chain, Ed25519 signatures, time receipts, and whether an audio file is the take it claims to be. No account, no server. Prefer a browser? [Drop a record here.](https://juanlentino.github.io/sealedrecord/)

<details><summary><b>Try it</b></summary>

```bash
curl -sO https://raw.githubusercontent.com/juanlentino/sealedrecord/main/vectors/record.json
curl -sO https://raw.githubusercontent.com/juanlentino/sealedrecord/main/vectors/take.wav
npx sealedrecord verify record.json take.wav
```

</details>

| Also building | Reading list |
| --- | --- |
| [**Signal & Noise**](https://github.com/juanlentino/signal-and-noise) + [**tools**](https://github.com/juanlentino/signal-and-noise-tools): the brutalist theme and plugin behind juanlentino.com<br><br>[**Provenance ledger**](https://github.com/juanlentino/signal-and-noise-provenance): every note I publish, signed and appended in public<br><br>[**Rights signals**](https://github.com/juanlentino/sn-rights-signals-worker): one machine-readable AI rights position, served at the edge<br><br>[**Connector for TypeSafe Jev**](https://github.com/juanlentino/jev-connector): typed, confidence-scored answers for WordPress, no prose to parse | Start at the [**provenance hub**](https://juanlentino.com/provenance/): the whole argument, in plain language<br><br>Then the papers on SSRN: [Provenance Over Detection](https://ssrn.com/abstract=6402298) · [Provenance as Substrate](https://ssrn.com/abstract=6730343) · [Provenance Without Institutions](https://ssrn.com/abstract=7456638)<br><br>Or the [**notes**](https://juanlentino.com/notes/): shorter essays on the same questions |

Upstream contributor to [**WordPress/openstation**](https://github.com/WordPress/openstation) (wp-admin as a desktop OS), [**AllTerrain Forms**](https://github.com/AllTerrainDeveloper/forms), and [**MAIA**](https://github.com/AllTerrainDeveloper/MAIA-Media-Asset-Interface-Administration): [see the merged pull requests](https://github.com/search?q=author%3Ajuanlentino+is%3Apr+is%3Amerged+-user%3Ajuanlentino&type=pullrequests). All of it engineered with Claude as a pair programmer.

MBA in Applied AI · Voting member, Recording Academy and Latin Recording Academy · Reviewer, LAMIR 2026 · [juanlentino.com](https://juanlentino.com) · [ORCID](https://orcid.org/0009-0006-8151-5920) · Hablo español.
