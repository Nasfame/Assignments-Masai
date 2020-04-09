strs=input()
dicti={}

for i in strs:
	if i not in dicti:
		dicti[i]=1
	else:
		dicti[i]+=1
		
print(*dicti.items())


