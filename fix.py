#while len(input) != 0:
result_list = []
for i in range(len(input)):
        small_number = 999  # biggest number we can imagine
        for i in input:
            if i < small_number:
                small_number = i
                indx = input.index(small_number)
        remove_num = input.pop(indx)
        result_list.append(remove_num)
print result_list

