import pytest
import itertools
from commitizen.bump import generate_version
from packaging.version import Version

simple_flow = [
    (("0.1.2", "PATCH", None), "0.1.2"),
    (("0.1.2", "MINOR", None), "0.2.0"),
    (("0.2.0", "MINOR", None), "0.3.0"),
    (("0.3.0", "PATCH", None), "0.3.1"),
    (("0.3.0", "PATCH", "alpha"), "0.3.1a0"),
    (("0.3.1a0", None, "alpha"), "0.3.1a1"),
    (("0.3.1a0", None, None), "0.3.1"),
    (("0.3.1", "PATCH", None), "0.3.2"),
    (("0.4.2", "MAJOR", "alpha"), "1.0.0a0"),
    (("1.0.0a0", None, "alpha"), "1.0.0a1"),
    (("1.0.0a1", None, "alpha"), "1.0.0a2"),
    (("1.0.0a1", None, "beta"), "1.0.0b0"),
    (("1.0.0b0", None, "beta"), "1.0.0b1"),
    (("1.0.0b1", None, "rc"), "1.0.0rc0"),
    (("1.0.0rc0", None, "rc"), "1.0.0rc1"),
    (("1.0.0rc0", "PATCH", None), "1.0.0"),
    (("1.0.0", "PATCH", None), "1.0.1"),
    (("1.0.1", "PATCH", None), "1.0.2"),
    (("1.0.2", "MINOR", None), "1.1.0"),
    (("1.1.0", "MINOR", None), "1.2.0"),
    (("1.2.0", "PATCH", None), "1.2.1"),
    (("1.2.1", "MAJOR", None), "2.0.0"),
]

# this cases should be handled gracefully
unexpected_cases = [
    (("0.1.2rc0", None, "alpha"), "0.1.2a0"),
    (("0.1.2b1", None, "alpha"), "0.1.2a0"),
]

weird_cases = [
    (("1.1", "PATCH", None), "1.1.1"),
    (("1", "MINOR", None), "1.1.0"),
    (("1", "MAJOR", None), "2.0.0"),
    (("1a0", None, "alpha"), "1.0.0a1"),
    (("1", None, "beta"), "1.0.0b0"),
    (("1beta", None, "beta"), "1.0.0b1"),
    (("1.0.0alpha1", None, "alpha"), "1.0.0a2"),
    (("1", None, "rc"), "1.0.0rc0"),
    (("1.0.0rc1+e20d7b57f3eb", "PATCH", None), "1.0.0"),
]

# test driven development
tdd_cases = [
    (("0.1.2", "PATCH", None), "0.1.2"),
    (("0.1.2", "MINOR", None), "0.2.0"),
    (("2.1.1", "MAJOR", None), "3.0.0"),
    (("0.9.0", "PATCH", "alpha"), "0.9.1a0"),
    (("0.9.0", "MINOR", "alpha"), "0.10.0a0"),
    (("0.9.0", "MAJOR", "alpha"), "1.0.0a0"),
    (("1.0.0a2", None, "beta"), "1.0.0b0"),
    (("1.0.0beta1", None, "rc"), "1.0.0rc0"),
    (("1.0.0rc1", None, "rc"), "1.0.0rc2"),
]


@pytest.mark.parametrize(
    "test_input,expected",
    itertools.chain(tdd_cases, weird_cases, simple_flow, unexpected_cases),
)
def test_generate_version(test_input, expected):
    current_version = test_input[0]
    increment = test_input[1]
    prerelease = test_input[2]
    assert generate_version(
        current_version, increment=increment, prerelease=prerelease
    ) == Version(expected)
