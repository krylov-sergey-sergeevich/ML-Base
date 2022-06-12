from storage.properties import BASE_PATH

file = open(f'../{BASE_PATH}/animals.txt', 'r')
# print(file.read())

# for line in file:
#     print(line)

print(file.read(10))
file.close()

file.close()
