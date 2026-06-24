# Contributing

Changes should improve the explanatory and dependency quality of the atlas, not merely increase its node count.

1. Read [`docs/SCOPE.md`](docs/SCOPE.md).
2. Edit the canonical [`data/atlas.json`](data/atlas.json).
3. Follow [`docs/EDITING.md`](docs/EDITING.md).
4. Run `make test`.
5. Include a short explanation of the dependency pattern added or corrected.

A contribution that adds a named model or product without a distinct reusable dependency pattern should normally be represented as an alias or example instead of a new node.
