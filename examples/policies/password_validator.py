def validate_password(password):
    errors = []

    if not isinstance(password, str):
        return {"valid": False, "errors": ["密码必须是字符串"]}

    if not 8 <= len(password) <= 20:
        errors.append("密码长度必须在 8 到 20 位之间")
    if " " in password:
        errors.append("密码不能包含空格")
    if not any(character.isupper() for character in password):
        errors.append("密码至少需要一个大写字母")


    if not any(character.islower() for character in password):
        errors.append("密码至少需要一个小写字母")
    if not any(character.isdigit() for character in password):
        errors.append("密码至少需要一个数字")
    if not any(not character.isalnum() and not character.isspace() for character in password):
        errors.append("密码至少需要一个特殊字符")


    return {
        "valid": not errors,


        "errors": errors,
    }


def print_password_result(password):
    result = validate_password(password)
    if result["valid"]:
        print("密码校验通过。")
        return

    print("密码校验不通过：")
    for error in result["errors"]:
        print("-", error)


def main():
    examples = [
        "Abc12345!",
        "abc12345!",
        "ABC12345!",
        "Abcdefgh!",
        "Abc123456",
        "Ab1!",
        "Abc 1234!",
        "",
        None,
    ]

    for password in examples:
        print(f"输入长度：{len(password) if isinstance(password, str) else '非字符串'}")
        print_password_result(password)
        print("=" * 30)


if __name__ == "__main__":
    main()
