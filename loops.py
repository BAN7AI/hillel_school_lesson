###############################################
# Друкує усі літери з рядку, які у верхньому регістрі, у прикладі вище це SFGA

value = input("Plese write here your string: ")

for i in value:
    if i.isupper():
        print(i)

###############################################
# Друкує індекси усіх пробілів, якщо вони є, у прикладі вище це  1, 8

a_letter = " "

for index, letter in enumerate(value):
    if letter == a_letter:
        print(f"{index}, _")

###############################################
# Друкує усі гласні букви з рядка, у прикладі вище це  aAa

list_words = ['A', 'a', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y']
answer = ''

for i in value:
    for letter in list_words:
        if letter == i:
            answer += letter
print(answer)

###############################################
# Якщо у рядку буде послідовність з трьох цифр, наприклад ab-c474f g - цикл переривається та друкується повідомлення про цю подію. Інакше друкується повідомлення про коректне завершення циклу

counter = 0
answer = ''


for i in value:
    if i.isalpha():
        counter = 0
        answer = ''
    else:
        counter += 1
        answer += i
        if len(answer) == 3:
            break

print(answer)

###############################################
