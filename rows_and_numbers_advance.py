# first
name_user = input("Hello user, write your name here please: ")
print(name_user)

# second

# print(name_user.replace(" ", ""))  # удаляет все пробелы или другие знаки которые указать в old
name_user = name_user.strip()  # удаляет пробелы спереди и сзади
print(name_user)

# third
print(f"Hello user, {name_user.title()}")  # Пишит первую букву заглавную последующие маленькие

# fourd
print(f"Len your name: {len(name_user)}")  # кол-во букв в строке

# five
print("".join(reversed(name_user)))  # Друкує ім'я задом наперед
print(name_user[::-1])  # Друкує ім'я задом наперед
