# a = [12, 3.85, "black", -4]
# print(a)       # [12, 3.85, 'black', -4]
# print(a[2:4]) #from 2 BEFORE 4 (not including 4)
#
# print(list(range(5)))

# number_list = list(range(20))
# print(number_list)
# print(number_list[5])
# print(number_list[-1])
# print(number_list[-2])
# print(number_list[-3])
# print(number_list[-4])
# print(number_list[-5])
# print(number_list[-6])

# print(number_list[5:16])
# # print(number_list[-15:-4])
# # print(number_list[5:-4])
# # print(number_list[-15:16])

# print(number_list[-1::-2]) #skip slice steps


line = 'Каждый элемент имеет свой индекс, или номер. Индексация начинается с нуля.'

# print(line[-1::-2])

print(len(line))

print(line[-1:-len(line):-1])
# print(line[5:len(line):5])

a = list(range(-1, -30, -3))
b = list(range(1, 30, 5))
c = list(range(15, -30, -4))

print(a+b+c) # for sorting - combine lists