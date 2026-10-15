def is_valid_phone(phone):
    if not isinstance(phone, str):
        return False
    if len(phone) != 11:
        return False
    if not phone.isdigit():
        return False
    if not phone.startswith("1"):
        return False
    return phone[1] in "3456789"


def explain_phone_result(phone):
    if is_valid_phone(phone):
        return f"手机号 {phone} 有效。"
    return f"手机号 {phone!r} 无效，请检查格式。"


def main():
    examples = [
        "13812345678",
        "15900001111",
        "12345678901",
        "1381234567",
        "138123456789",
        "1381234567a",
        "",
        None,
        13812345678,
    ]

    for phone in examples:
        print(explain_phone_result(phone))


if __name__ == "__main__":
    main()
