import pytest

from src.library_eligibility import can_borrow


@pytest.mark.parametrize(
    "active_loans, overdue_books, expected",
    [
        (0, 0, True),
        (1, 0, True),
        (4, 0, True),
        (5, 0, False),  # Supplied code uses <= 5; the requirement is less than 5.
        (6, 0, False),
        (0, 1, False),
        (4, 1, False),
        (5, 1, False),
        (6, 2, False),
        (1000, 0, False),
        (0, 1000, False),
    ],
)
def test_valid_loan_counts_returns_expected_eligibility(active_loans, overdue_books, expected):
    # Arrange: each row gives the loan counts and expected borrowing decision.
    # Act
    result = can_borrow(active_loans, overdue_books)

    # Assert: identity checks the exact Boolean as well as its value.
    assert result is expected


@pytest.mark.parametrize("active_loans, overdue_books", [(-1, 0), (0, -1), (-1, -1)])
def test_negative_loan_counts_raises_value_error(active_loans, overdue_books):
    with pytest.raises(ValueError):
        can_borrow(active_loans, overdue_books)


@pytest.mark.parametrize("active_loans", [1.5, "1", None, [], {}, True, False])
def test_invalid_active_loans_type_raises_type_error(active_loans):
    with pytest.raises(TypeError):
        can_borrow(active_loans, 0)


@pytest.mark.parametrize("overdue_books", [1.5, "1", None, [], {}, True, False])
def test_invalid_overdue_books_type_raises_type_error(overdue_books):
    with pytest.raises(TypeError):
        can_borrow(0, overdue_books)
