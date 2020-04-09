li = input().split()
dicti={}

for i in li:
	if i not in dicti:
		dicti[i]=1
	else:
		print(i)