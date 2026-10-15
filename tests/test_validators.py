import pytest

from qa_utils.validators import is_password_valid, is_phone_number


@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param("13812345678", True, id="valid_phone"),
        pytest.param("19900001111", True, id="another_valid_phone"),
        pytest.param("1381234567", False, id="too_short_10_digits"),
        pytest.param("138123456789", False, id="too_long_12_digits"),
        pytest.param("03812345678", False, id="wrong_first_digit"),
        pytest.param("13812A45678", False, id="contains_letter"),
        pytest.param("13812 45678", False, id="contains_space"),
        pytest.param("１３８１２３４５６７８", False, id="fullwidth_digits"),

        pytest.param("1３８１２３４５６７８", False, id="mixed_non_ascii_digits"),
        pytest.param("", False, id="empty_string"),
        pytest.param(None, False, id="none_input"),
        pytest.param(13812345678, False, id="integer_input"),
        pytest.param(True, False, id="boolean_input"),
    ],
)
def test_is_phone_number(value, expected):
    result = is_phone_number(value)

    assert result is expected


@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param("Abc12345", True, id="minimum_length_8"),
        pytest.param("A1" + "b" * 18, True, id="maximum_length_20"),
        pytest.param("Ab12345", False, id="below_minimum_length_7"),
        pytest.param("A1" + "b" * 19, False, id="above_maximum_length_21"),
        pytest.param("abcdefgh", False, id="missing_digit"),
        pytest.param("12345678", False, id="missing_letter"),
        pytest.param("Abcdef１２", False, id="missing_ascii_digit"),
        pytest.param("中文12345678", False, id="missing_ascii_letter"),
        pytest.param("Abc1234!", True, id="special_character_allowed"),

        pytest.param("Abc1234 ", True, id="space_allowed_by_current_rule"),
        pytest.param("", False, id="empty_string"),
        pytest.param(None, False, id="none_input"),
        pytest.param(12345678, False, id="integer_input"),
    ],
)
def test_is_password_valid(value, expected):
    result = is_password_valid(value)
    assert result is expected
