import pytest

from designtools.mathutil import Range


@pytest.mark.parametrize(
    "range_params",
    [
        (10, 0),
        (10, 10),
    ],
)
def test_bad_range_init(range_params: tuple[int, int]):
    with pytest.raises(ValueError):
        r = Range(*range_params)


@pytest.mark.parametrize(
    "range_params, test, expected",
    [
        ((0, 10, False), 5, True),
        ((0, 10, False), -5, False),
        ((0, 10, False), 0, True),
        ((0, 10, False), 10, False),
        ((0, 10, True), 10, True),
        ((0, 10, False), 10, False),
        ((0, 10, False), 5, True),
    ],
)
def test_range_contains(range_params, test, expected):
    assert (test in Range(*range_params)) == expected


@pytest.mark.parametrize(
    "params, expected",
    [
        ((0, 10, False), "Range(0, 10, False)"),
        ((0, 10, True), "Range(0, 10, True)"),
    ],
)
def test_range_repr(params, expected):
    assert repr(Range(*params)) == expected


@pytest.mark.parametrize(
    "params, expected",
    [
        ((0, 10, False), "Range [0, 10)"),
        ((0, 10, True), "Range [0, 10]"),
    ],
)
def test_range_str(params, expected):
    assert str(Range(*params)) == expected
