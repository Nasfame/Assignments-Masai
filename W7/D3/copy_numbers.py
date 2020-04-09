fnw = open('backup/sort_numbers.txt', 'r')
content = fnw.readlines()
num_list=[]
for i in content:
    i.strip('\n')
    num_list.append(i)
fnw.close()



file = open('backup/copy_numbers.txt', 'w')
file.write(' '.join(num_list))
file.close()