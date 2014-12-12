__author__ = 'martinsolheim'

person_list = []

for i in range(1, 1500, 2):
    person_list.append(i)

drinking_person = 1
while len(person_list) > 1:
    length = len(person_list)
    for i in range(drinking_person, length, 2):
        person_list[i] = 0

    if i == length - 1:
        drinking_person = 1
    else:
        drinking_person = 0

    person_list = list(filter((0).__ne__, person_list))
    print(person_list)

print(person_list)