# # # B1. Журнал студентов
# students = [
#     {"name": "Ayan", "group": "Python-1", "grades": [80, 90, 75], "skills": {"python", "git", "html"}},
#     {"name": "Dana", "group": "Python-1", "grades": [95, 100, 90], "skills": {"python", "git", "sql"}},
#     {"name": "Miras", "group": "Python-2", "grades": [60, 55, 70], "skills": {"html", "css"}},
#     {"name": "Alina", "group": "Python-2", "grades": [100, 90, 95], "skills": {"python", "data", "sql"}}
# ]

# for student in students:
#     print(student["name"])

# print("Средние баллы:")
# for student in students:
#     avg = round(sum(student["grades"]) / len(student["grades"]), 2)
#     print(f"{student['name']}: {avg}")

# print("Студенты с баллом >= 70:")
# for student in students:
#     avg = sum(student["grades"]) / len(student["grades"])
#     if avg >= 70:
#         print(student["name"])

# print("Студенты с python:")
# for student in students:
#     if "python" in student["skills"]:
#         print(student["name"])

# all_skills = set()
# for student in students:
#     all_skills.update(student["skills"])
# print("\nВсе уникальные навыки:", all_skills)

# groups = {}
# for student in students:
#     group_name = student["group"]
#     if group_name not in groups:
#         groups[group_name] = []
#     groups[group_name].append(student)

# print("Группы:")
# for group, studs in groups.items():
#     names = [s['name'] for s in studs]
#     print(f"{group}: {names}")



# # B2. Корзина интернет-магазина
# cart = [
#     {"name": "Laptop", "category": "tech", "price": 350000, "count": 1},
#     {"name": "Mouse", "category": "tech", "price": 8000, "count": 2},
#     {"name": "Book", "category": "education", "price": 7000, "count": 3},
#     {"name": "Keyboard", "category": "tech", "price": 15000, "count": 1}
# ]

# total = sum(item["price"] * item["count"] for item in cart)
# print("Общая сумма:", total)

# tech_items = [item["name"] for item in cart if item["category"] == "tech"]
# print("Товары tech:", tech_items)

# more_than_one = [item["name"] for item in cart if item["count"] > 1]
# print("Товары с count > 1:", more_than_one)

# most_expensive = max(cart, key=lambda x: x["price"])
# print("Самый дорогой:", most_expensive["name"])

# names = [item["name"] for item in cart]
# print("Названия товаров:", names)

# category_total = {}
# for item in cart:
#     cat = item["category"]
#     category_total[cat] = category_total.get(cat, 0) + item["price"] * item["count"]

# print("Сумма по категориям:")
# for cat, s in category_total.items():
#     print(cat, ":", s)

# # B3. Курсы и студенты
# courses = {
#     "python": ["Ayan", "Dana", "Miras"],
#     "frontend": ["Dana", "Alina", "Miras"],
#     "design": ["Ayan", "Alina"],
#     "sql": ["Dana", "Ayan"]
# }

# all_students = set()
# for students in courses.values():
#     all_students.update(students)
# print("Все студенты:", sorted(all_students))

# print("Python:", courses["python"])

# python_and_sql = set(courses["python"]) & set(courses["sql"])
# print("Python и SQL:", sorted(python_and_sql))

# frontend_not_design = set(courses["frontend"]) - set(courses["design"])
# print("Frontend, но не Design:", sorted(frontend_not_design))

# print("Количество на курсах:")
# for course, students in courses.items():
#     print(course, ":", len(students))

# student_courses = {}
# for course, students in courses.items():
#     for student in students:
#         if student not in student_courses:
#             student_courses[student] = []
#         student_courses[student].append(course)

# print("Студент -> курсы:")
# for student, clist in sorted(student_courses.items()):
#     print(student, ":", clist)

# # # B4. Пользователи и права доступа
# users = [
#     {"name": "Ayan", "role": "admin", "permissions": {"read", "write", "delete", "ban"}},
#     {"name": "Dana", "role": "editor", "permissions": {"read", "write"}},
#     {"name": "Miras", "role": "viewer", "permissions": {"read"}},
#     {"name": "Alina", "role": "moderator", "permissions": {"read", "ban"}}
# ]

# print("Пользователи и роли:")
# for user in users:
#     print(user["name"], "-", user["role"])

# print("Имеют право write:")
# for user in users:
#     if "write" in user["permissions"]:
#         print(user["name"])

# print("Могут банить:")
# for user in users:
#     if "ban" in user["permissions"]:
#         print(user["name"])

# print("Имеют read и write:")
# for user in users:
#     if "read" in user["permissions"] and "write" in user["permissions"]:
#         print(user["name"])

# all_permissions = set()
# for user in users:
#     all_permissions.update(user["permissions"])
# print("Все уникальные права:", all_permissions)

# role_users = {}
# for user in users:
#     role = user["role"]
#     if role not in role_users:
#         role_users[role] = []
#     role_users[role].append(user["name"])

# print("Роль -> пользователи:")
# for role, names in role_users.items():
#     print(role, ":", names)

# # B5. Комментарии и теги
# posts = [
#     {
#         "title": "Python basics",
#         "tags": {"python", "programming", "study"},
#         "comments": [
#             {"user": "Ayan", "text": "Very useful", "likes": 5},
#             {"user": "Dana", "text": "I need more examples", "likes": 3}
#         ]
#     },
#     {
#         "title": "Git guide",
#         "tags": {"git", "github", "study"},
#         "comments": [
#             {"user": "Miras", "text": "Git is hard", "likes": 2},
#             {"user": "Alina", "text": "Now I understand push", "likes": 7}
#         ]
#     }
# ]
# for post in posts:
#     print(post["title"])

# all_tags = set()
# for post in posts:
#     all_tags.update(post["tags"])
# print(all_tags)

# total_comments = sum(len(post["comments"]) for post in posts)
# print(total_comments)

# for post in posts:
#     for comment in post["comments"]:
#         if comment["likes"] >= 5:
#             print(comment)

# all_comments = [comment for post in posts for comment in post["comments"]]
# top_comment = max(all_comments, key=lambda c: c["likes"])
# print(top_comment)

# title_comments = {post["title"]: len(post["comments"]) for post in posts}
# print(title_comments)