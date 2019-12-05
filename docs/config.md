# Configuration

Commitizen has support for `toml` and `ini` files.

## pyproject.toml

Add an entry to `pyproject.toml`. Recommended for **python** projects.

    [tool.commitizen]
    name = "cz_conventional_commits"
    version = "0.1.4"
    files = [
        "src/__version__.py",
        "pyproject.toml:version"
    ]

## INI files

Supported files: `.cz`, `.cz.cfg`, `setup.py`, and `$HOME/.cz`

The format is slightly different to the `toml`, so pay attention.
Recommended for **other languages** projects (js, go, etc).

    [commitizen]
    name = cz_conventional_commits
    version = 0.1.4
    files = [
        "src/__version__.py",
        "pyproject.toml:version"
        ]

The extra tab before the square brakets (`]`) at the end is required.

## Settings

| Variable | Type | Default | Description |
| -------- | ---- | ------- | ----------- |
| `name` | `str` | `"cz_conventional_commits"` | Name of the commiting rules to use |
| `version` | `str` | `None` | Current version. Example: "0.1.4" |
| `files` | `list` | `[ ]` | Files were the version will be updated. A pattern to match a line, can also be specified, separated by `:` [See more](https://woile.github.io/commitizen/bump#files) |
| `tag_format` | `str` | `None` | Format for the git tag, useful for old projects, that use a convention like `"v1.2.1"`. [See more](https://woile.github.io/commitizen/bump#tag_format) |
| `bump_message` | `str` | `None` | Create custom commit message, useful to skip ci. [See more](https://woile.github.io/commitizen/bump#bump_message) |
