with open('backup/name1.txt', 'r') as file1:
    c1 = set(file1.readlines())
with open('backup/name2.txt', 'r') as file2:
    c2 = set(file2.readlines())

c3 = list(c1.union(c2))
c4=[]
for i in c3:
    c4.append(i.strip('\n'))


with open('backup/merge.txt', 'w') as file3:
    file3.write(' '.join(c4))

