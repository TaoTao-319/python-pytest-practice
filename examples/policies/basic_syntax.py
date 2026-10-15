def greet_user(name):
    return f"你好，{name}！欢迎开始学习 Python。"


def get_adult_message(age):
    if age >= 18:
        return "已满 18 岁"
    return "未满 18 岁"


def calculate_score_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)


def print_student_info(student):
    print(f"姓名：{student['name']}")
    print(f"年龄：{student['age']}")
    print(f"学习方向：{student['direction']}")


def main():

    name = "测试学习者"
    age = 25
    is_learning = True
    print("姓名：", name)
    print("年龄：", age)
    print("是否正在学习：", is_learning)
    print(greet_user(name))
    print()


    skills = ["Python", "手工测试", "Git"]
    skills.append("pytest")
    skills[0] = "Python 基础"
    print("技能列表：")
    for skill in skills:
        print("-", skill)
    print()


    student = {
        "name": name,
        "age": age,
        "direction": "软件测试",
    }
    print_student_info(student)
    print()


    print(get_adult_message(age))
    print()


    scores = [80, 90, 85]
    total = 0
    for score in scores:
        total += score
    print("总分：", total)
    print("平均分：", calculate_score_average(scores))


if __name__ == "__main__":
    main()
