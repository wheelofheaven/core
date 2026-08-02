# Schemas

- `catalog.schema.json` validates the claim catalog.
- `claim.schema.json` validates individual claim records.

The repository validator performs additional cross-file checks that JSON Schema
cannot express, including catalog consistency, source-note existence,
dependency resolution, and optional validation against Wheel's aggregated
source registry.
