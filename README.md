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

<table>
<tr><th>Also building</th><th>Reading list</th></tr>
<tr>
<td valign="top"><a href="https://github.com/juanlentino/sn-rights-signals-worker"><b>Rights signals</b></a>: one machine-readable AI rights position, served at the edge<br><br><a href="https://github.com/juanlentino/jev-connector"><b>Connector for TypeSafe Jev</b></a>: typed, confidence-scored answers for WordPress, no prose to parse<br><br>Upstream contributor to <a href="https://github.com/WordPress/openstation"><b>WordPress/openstation</b></a> (wp-admin as a desktop OS), <a href="https://github.com/AllTerrainDeveloper/forms"><b>AllTerrain Forms</b></a>, and <a href="https://github.com/AllTerrainDeveloper/MAIA-Media-Asset-Interface-Administration"><b>MAIA</b></a>: <a href="https://github.com/search?q=author%3Ajuanlentino+is%3Apr+is%3Amerged+-user%3Ajuanlentino&amp;type=pullrequests">see the merged pull requests</a></td>
<td valign="top">Start at the <a href="https://juanlentino.com/provenance/"><b>provenance hub</b></a>: the whole argument, in plain language<br><br>Then the papers on SSRN: <a href="https://ssrn.com/abstract=6402298">Provenance Over Detection</a> · <a href="https://ssrn.com/abstract=6730343">Provenance as Substrate</a> · <a href="https://ssrn.com/abstract=7456638">Provenance Without Institutions</a><br><br>Or the <a href="https://juanlentino.com/notes/"><b>notes</b></a>: shorter essays on the same questions</td>
</tr>
</table>

All of it engineered with Claude as a pair programmer. The theme, plugin and provenance ledger are pinned below.

MBA in Applied AI · Voting member, Recording Academy and Latin Recording Academy · Reviewer, LAMIR 2026 · [juanlentino.com](https://juanlentino.com) · [ORCID](https://orcid.org/0009-0006-8151-5920) · Hablo español.
