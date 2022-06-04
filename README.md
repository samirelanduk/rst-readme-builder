# rst-readme-builder

This script generates an RST README from an existing Sphinx documentation. It
has a lot of expectations baked in currently:

- You are in the root directory of your repo.
- There is a docs folder called `docs`.
- Source files are in `docs/source`.
- There is an `index.rst` in there with a Table of Contents.
- There's also files called `installing.rst`, `overview.rst` and `changelog.rst`.

If there's an existing README.rst, the badges from this will be extracted before
it is overwritten, and added to the new version.