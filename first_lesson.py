# sum of two numbers
result = 1 + 1 # TODO calculation
print("Result", result)
print("Result", type("Result"))
print(result, type(result))

number = 2
string = "2"

number_a = 7    #straight method
numbet_b = number_a #reference to another object
print(numbet_b, number_a)

number_a, number_b = 4, 12 + 3   #multiple assignment exist, not recommended
print(number_a, number_b)

#type() - вычисляет тип данных и сообщает
#value:str = "string" - анатация типа к имени объекта (в данном случае строка (
#             value:str = "string", value: int = 12))
#id() - встроенная функция, который возвращает идитификатор объекта

my_first_value = 3
print(id(my_first_value), id(2), id(3))

usual_string = "New line \n and tabulation \t here" #\n - new line; \t - tabulation
print(usual_string)

usual_string = "New line \\n and tabulation \\t here" #напечатать не печатные симфолы
print(usual_string)

usual_string = r"New line \n and tabulation \t here" #напечатать не печатные симфолы
print(usual_string)

my_cool_str = "This is my test text"
format_string = f"Put some value here - {my_cool_str}" #форматирования и вставка переменной в строку
print(format_string)

format_string_2 = f"More magic = {my_cool_str=}" #форматирования и показывание названия вставленной именем переменно и ее значения
print(format_string_2)

username = input("Please tell me your name: ") #ввод данных от пользователя
result = f"Hello {username}, nice to meet you!"
print(result)

value_one: int = 2
square_root = value_one ** 0.5 #корень числа
print(square_root)

# % - остаток от деления
# // - целочисленное деление (сколько целых делителей входит в число делимое)

value_one *= 2 # value_one = value_one *(/, +, -, //, %) 2
print(value_one)