import pytest

from src.library_fine import calculate_fine


@pytest.mark.parametrize(
    "days_overdue, expected_fine",
    [
        (0, 0),
        (1, 50),
        (9, 450),
        (10, 500),
        (11, 550),
        (1000, 50000),
    ],
)
def test_nonnegative_overdue_days_returns_fine_in_cents(days_overdue, expected_fine):
    # Arrange: each row supplies the days and the fine required by the specification.
    # Act
    result = calculate_fine(days_overdue)

    # Assert: the fine must be an integer and must not have a maximum cap.
    assert type(result) is int
    assert result == expected_fine


@pytest.mark.parametrize("days_overdue", [-1, -10])
def test_negative_overdue_days_raises_value_error(days_overdue):
    with pytest.raises(ValueError):
        calculate_fine(days_overdue)


@pytest.mark.parametrize("days_overdue", [1.5, "1", None, [], {}, True, False])
def test_invalid_overdue_days_type_raises_type_error(days_overdue):
    with pytest.raises(TypeError):
        calculate_fine(days_overdue)
