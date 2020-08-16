# text = open("M2Files.txt")
#
# print(text)
# # print(text.read())
#
# line = text.read()
#
# elements = line.split()
#
# sum_elements = 0
#
# for element in elements:
#     sum_elements = sum_elements + int(element)
#
# print(sum_elements)


# text = open("M2Files.txt")
#
# print(text)
#
# sum_elements = 0
#
# for element in text.read().split():
#     # sum_elements = sum_elements + int(element)
#     sum_elements += int(element)
#
# print(sum_elements)

print(open(r"M2 Data.txt"))
print(open(r"M2 Data.txt").read())  # read the text inside
print(open(r"M2 Data.txt", encoding="UTF-8").read())
print(open(r"M2 Data.txt", encoding="Big5"))





