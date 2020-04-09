with open('masai.txt','r') as f1:
    cnt = f1.read()
count=0

i=0
while i<len(cnt):
    if cnt[i]=='m':
        if cnt[i+4]=='i':
            count+=1
            i+=1
    i+=1

print(count)



