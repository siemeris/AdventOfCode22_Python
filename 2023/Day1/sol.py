# file = open('input.txt', 'r')
# lines = file.readlines()

with open('input.txt', 'r') as file:
    lines = file.readlines()

arr_aux = []
arr = []
sum = 0
for line in lines:
    for char in line:
        if char.isdigit():
            arr_aux.append(char)
            print("arr_aux" , arr_aux)
    num_str = str(arr_aux[0]) + str(arr_aux[len(arr_aux)-1])
    arr.append(num_str)
    arr_aux = []
    print(arr)

for item in arr:
    print(int(item))
    sum = sum + int(item)

print(sum)
