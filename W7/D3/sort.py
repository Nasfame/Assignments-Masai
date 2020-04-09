file = open('backup/numbers.txt', 'r')
content =file.readlines()
num_list=[]
for i in content:
    i.strip('\n')
    num_list.append(int(i))
file.close()
num_list.sort()
num_list=list(map(str,num_list))
fnw = open('backup/sort_numbers.txt', 'w')
fnw.write(' '.join(num_list))
fnw.close()

    
