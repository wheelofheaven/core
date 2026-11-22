# Machine-readable model

`catalog.json` indexes claim records under `claims/`. JSON Schemas live under
`schemas/`.

Human-readable documents under `docs/framework/` control conceptual meaning.
JSON records control machine interchange. Update both together.

Claim IDs are stable and never reused for a different proposition.

`expectations/` holds the research programme's register (RFC 0009, ADR 0017):
one record per registered expectation, `woh-exp-NNNN`. A record is added by
the commit that registers it and afterwards only gains its finding,
assessment, contest, ruling and outputs. See
[the research programme](../docs/methodology/research-programme.md).
