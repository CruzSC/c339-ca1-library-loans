import pytest

from src.library_fine import calculate_fine


@pytest.mark.parametrize(
    "days_overdue, expected_fine",
    [
        (0, 0),
        (1, 50),
        (9, 450),
        (10, 500),
        (11, 550),  # Fails: the supplied code caps the fine at 500 cents.
        (1000, 50000),  # Check that the fine keeps increasing.
    ],
)
def test_nonnegative_overdue_days_returns_fine_in_cents(days_overdue, expected_fine):
    # Arrange: test data is supplied above.
    # Act
    result = calculate_fine(days_overdue)

    # Assert
    assert type(result) is int
    assert result == expected_fine


@pytest.mark.parametrize("days_overdue", [-1, -10])
def test_negative_overdue_days_raises_value_error(days_overdue):
    with pytest.raises(ValueError):
        calculate_fine(days_overdue)


# 1.0 is still a float. True and False are also invalid under the specification.
@pytest.mark.parametrize("days_overdue", [1.0, 1.5, "1", None, [], {}, True, False])
def test_invalid_overdue_days_type_raises_type_error(days_overdue):
    with pytest.raises(TypeError):
        calculate_fine(days_overdue)
