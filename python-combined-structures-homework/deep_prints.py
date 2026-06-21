# # A1. Университет и курсы
# university = {
#     "name": "Narxoz Tech",
#     "city": "Almaty",
#     "courses": [
#         {
#             "title": "Python Basic",
#             "teacher": "Madiyar",
#             "students": [
#                 {
#                     "name": "Ayan",
#                     "age": 17,
#                     "grades": [80, 90, 75],
#                     "skills": {"python", "git", "html"}
#                 },
#                 {
#                     "name": "Dana",
#                     "age": 18,
#                     "grades": [95, 100, 90],
#                     "skills": {"python", "sql", "figma"}
#                 }
#             ]
#         },
#         {
#             "title": "Frontend",
#             "teacher": "Aruzhan",
#             "students": [
#                 {
#                     "name": "Miras",
#                     "age": 19,
#                     "grades": [70, 65, 80],
#                     "skills": {"html", "css", "javascript"}
#                 }
#             ]
#         }
#     ]
# }

# print(university["name"])
# print(university["city"])
# print(university["courses"][0]["title"])
# print(university["courses"][1]["teacher"])
# print(university["courses"][0]["students"][1]["name"])
# print(university["courses"][0]["students"][1]["grades"][0])
# print(university["courses"][0]["students"][0]["skills"])
# print("python" in university["courses"][0]["students"][1]["skills"])
# print(university["courses"][1]["students"][0]["age"])
# print(university["courses"][1]["students"][0]["grades"][-1])


# # #A2. Интернет-магазин
# shop = {
#     "name": "Tech Store",
#     "categories": [
#         {
#             "name": "laptops",
#             "products": [
#                 {
#                     "id": 1,
#                     "title": "Lenovo IdeaPad",
#                     "price": 320000,
#                     "colors": ("gray", "black"),
#                     "tags": {"work", "study", "portable"},
#                     "stock": {"Almaty": 5, "Astana": 2}
#                 },
#                 {
#                     "id": 2,
#                     "title": "MacBook Air",
#                     "price": 600000,
#                     "colors": ("silver", "midnight"),
#                     "tags": {"work", "premium", "portable"},
#                     "stock": {"Almaty": 3, "Astana": 1}
#                 }
#             ]
#         },
#         {
#             "name": "phones",
#             "products": [
#                 {
#                     "id": 3,
#                     "title": "iPhone 15",
#                     "price": 450000,
#                     "colors": ("black", "blue"),
#                     "tags": {"mobile", "camera"},
#                     "stock": {"Almaty": 7, "Astana": 4}
#                 }
#             ]
#         }
#     ]
# }


# print(shop["name"])

# print(shop["categories"][0]["name"])

# print(shop["categories"][0]["products"][1]["title"])

# print(shop["categories"][0]["products"][1]["price"])

# print(shop["categories"][0]["products"][0]["colors"][0])

# print(shop["categories"][1]["products"][0]["stock"]["Astana"])

# print(shop["categories"][0]["products"][1]["tags"])

# print("portable" in shop["categories"][0]["products"][0]["tags"])

# print(shop["categories"][1]["products"][0]["id"])

# print(shop["categories"][1]["products"][0]["colors"][1])



# # # A3. CRM салона

# crm = {
#     "salon": "Beauty Lab",
#     "masters": [
#         {
#             "name": "Aruzhan",
#             "services": {"lashes", "brows"},
#             "schedule": {
#                 "monday": ["10:00", "12:00", "15:00"],
#                 "tuesday": ["11:00", "14:00"]
#             }
#         },
#         {
#             "name": "Dana",
#             "services": {"nails", "pedicure"},
#             "schedule": {
#                 "monday": ["09:00", "13:00"],
#                 "friday": ["16:00", "18:00"]
#             }
#         }
#     ],
#     "clients": [
#         {
#             "name": "Amina",
#             "phone": "87010000001",
#             "visits": [
#                 {"date": "2026-06-01", "service": "lashes", "price": 12000},
#                 {"date": "2026-06-10", "service": "brows", "price": 8000}
#             ]
#         }
#     ]
# }


# print(crm["salon"])

# print(crm["masters"][0]["name"])

# print(crm["masters"][1]["services"])

# print(crm["masters"][1]["schedule"]["friday"][1])

# print(crm["masters"][0]["schedule"]["monday"][0])

# print(crm["clients"][0]["name"])

# print(crm["clients"][0]["phone"])

# print(crm["clients"][0]["visits"][1]["service"])

# print(crm["clients"][0]["visits"][0]["price"])

# print("lashes" in crm["masters"][0]["services"])


# social = {
#     "app": "Campus Social",
#     "users": [
#         {
#             "id": 1,
#             "username": "ayan17",
#             "profile": {
#                 "name": "Ayan",
#                 "city": "Almaty",
#                 "interests": {"music", "python", "games"}
#             },
#             "posts": [
#                 {"text": "Learning Python", "likes": 15, "comments": ["good", "nice"]},
#                 {"text": "Git is useful", "likes": 9, "comments": []}
#             ]
#         },
#         {
#             "id": 2,
#             "username": "dana_ui",
#             "profile": {
#                 "name": "Dana",
#                 "city": "Astana",
#                 "interests": {"design", "figma", "python"}
#             },
#             "posts": [
#                 {"text": "My first UI kit", "likes": 25, "comments": ["wow"]}
#             ]
#         }
#     ]
# }

# print(social["app"])
# print(social["users"][0]["username"])
# print(social["users"][1]["profile"]["city"])
# print(social["users"][0]["profile"]["interests"])
# print("python" in social["users"][1]["profile"]["interests"])
# print(social["users"][0]["posts"][0]["text"])
# print(social["users"][0]["posts"][1]["likes"])
# print(social["users"][0]["posts"][0]["comments"][0])
# print(social["users"][1]["posts"][0]["text"])


# # # A5. Игровая библиотека
# game_library = {
#     "owner": "Madiyar",
#     "platforms": [
#         {
#             "name": "Steam",
#             "games": [
#                 {
#                     "title": "Path of Exile 2",
#                     "genres": {"RPG", "Action", "Online"},
#                     "hours": 120,
#                     "achievements": ("First Boss", "Act 1 Clear", "Rare Drop")
#                 },
#                 {
#                     "title": "Hades",
#                     "genres": {"Roguelike", "Action"},
#                     "hours": 45,
#                     "achievements": ("Escape Attempt", "First Win")
#                 }
#             ]
#         },
#         {
#             "name": "Epic Games",
#             "games": [
#                 {
#                     "title": "Control",
#                     "genres": {"Action", "Adventure"},
#                     "hours": 20,
#                     "achievements": ("Start", "Finish")
#                 }
#             ]
#         }
#     ]
# }
# print(game_library["owner"])
# print(game_library["platforms"][0]["name"])
# print(game_library["platforms"][0]["games"][1]["title"])
# print(game_library["platforms"][0]["games"][0]["hours"])
# print(game_library["platforms"][0]["games"][1]["genres"])
# print("RPG" in game_library["platforms"][0]["games"][0]["genres"])
# print(game_library["platforms"][0]["games"][0]["achievements"][1])
# print(game_library["platforms"][1]["games"][0]["title"])
# print(game_library["platforms"][1]["games"][0]["achievements"][0])
# print(game_library["platforms"][0]["games"][1]["hours"])


