# start

num_list: list[int] = []

for i in range(1, 100 + 1):
    num_list.append(i)
print(num_list)
print(num_list[0])
print(num_list[len(num_list) - 1])
print(len(num_list))
print(num_list[2:12])
print(num_list[79:])
print(num_list[:17])
print(num_list[-1::-1])
print(num_list[1::2])
print(num_list[2::3])
print(num_list[6::7])
print(num_list[9::10])
print(num_list[-2:64:-3])
num_list.insert(49,999)
print(num_list)
num_list.pop()
print(num_list)