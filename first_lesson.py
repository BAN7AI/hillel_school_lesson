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

