first_input_user = input("Input your letters and numbers here: ")
second_input_user = input("Input your letters and numbers here: ")

first_set = set(first_input_user)
second_set = set(second_input_user)

# 1.1

print(first_set.intersection(second_set))

# 1.2
a = list()
b = list()

for i in first_set:
    if i.isdigit():
        a.append(i)

for i in second_set:
    if i.isdigit():
        b.append(i)

a_set = set(a)
b_set = set(b)

print(a_set.difference(b_set))

# 2
a = {1, 2, 3}
b = {3, 4, 5}

a |= b

print(a)

###########################################

a = {1, 2, 3}
b = {2, 3, 4}

a &= b

print(a)
###########################################

a = {1, 2, 3, 4}
b = {2, 3}

a -= b

print(a)
############################################
a = {1, 2, 3}
b = {3, 4, 5}

a ^= b

print(a)
