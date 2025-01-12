import os
import pytest
from commitizen import bump

PYPROJECT = """
[tool.poetry]
name = "commitizen"
version = "1.2.3"
"""

VERSION_PY = """
__title__ = 'requests'
__description__ = 'Python HTTP for Humans.'
__url__ = 'http://python-requests.org'
__version__ = '1.2.3'
"""

REPEATED_VERSION_NUMBER = """
{
  "name": "magictool",
  "version": "1.2.3",
  "dependencies": {
      "lodash": "1.2.3"
  }
}
"""

files_with_content = (
    ("pyproject.toml", PYPROJECT),
    ("__version__.py", VERSION_PY),
    ("package.json", REPEATED_VERSION_NUMBER),
)


@pytest.fixture
def create_files():
    files = []
    for fileconf in files_with_content:
        filename, content = fileconf
        filepath = os.path.join("tests", filename)
        with open(filepath, "w") as f:
            f.write(content)
        files.append(filepath)
    yield files
    for filepath in files:
        os.remove(filepath)


def test_update_version_in_files(create_files):
    old_version = "1.2.3"
    new_version = "2.0.0"
    bump.update_version_in_files(old_version, new_version, create_files)
    for filepath in create_files:
        with open(filepath, "r") as f:
            data = f.read()
        assert new_version in data


def test_partial_update_of_file(create_files):
    old_version = "1.2.3"
    new_version = "2.0.0"
    filepath = "tests/package.json"
    regex = "version"
    location = f"{filepath}:{regex}"

    bump.update_version_in_files(old_version, new_version, [location])
    with open(filepath, "r") as f:
        data = f.read()
        assert new_version in data
        assert old_version in data
