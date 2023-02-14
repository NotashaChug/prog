def sorting_f(list):
    for i in range(1, len(list)):
        for k in range(0, i):
            if list[i] <= list[k]:
                j = list[k]
                list[k] = list[i]
                list[i] = j

raw_list = open("sort.txt", 'r').read().split(' ')
list = []
for i in range(0, len(raw_list)):
    list.append(int(raw_list[i]))

sorting_f(list)
string_list = ''
for i in range(0, len(list)):
    string_list = string_list + str(list[i]) + ' '

open('sorted.txt', 'w').write(string_list)















