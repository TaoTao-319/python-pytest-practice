def is_phone_number(value: object) -> bool:

    if not isinstance(value, str):
        return False

    return (
        len(value) == 11
        and value.startswith("1")
        and value.isascii()
        and value.isdigit()
    )


def is_password_valid(value: object) -> bool:
    if not isinstance(value, str) or not 8 <= len(value) <= 20:
        return False

    has_ascii_letter = any(char.isascii() and char.isalpha() for char in value)
    has_ascii_digit = any(char.isascii() and char.isdigit() for char in value)
    return has_ascii_letter and has_ascii_digit
