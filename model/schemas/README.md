# Schemas

- `catalog.schema.json` validates the claim catalog.
- `claim.schema.json` validates individual claim records.
- `expectation.schema.json` validates research-programme expectation records
  (RFC 0009, ADR 0017).

The repository validator performs additional cross-file checks that JSON Schema
cannot express, including catalog consistency, source-note existence,
dependency resolution, and optional validation against Wheel's aggregated
source registry.
