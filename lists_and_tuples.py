message = input("Pleasw write here yuor message: ")

message_list = message.split(" ")

print(len(message_list))
print(message_list[2::3])

#####################################################

user_list = [1, 2.1, 'f', '2', 3, '1', 18, 'df']
out_list = []

gen_list = [
    i if isinstance(i, float) else
    i if isinstance(i, int) and i % 2 == 0 else
    i ** 2 if isinstance(i, int) and i % 2 != 0 else
    int(i) * 3 if isinstance(i, str) and i.isdigit() else -1
    for i in user_list
]
print(gen_list)
