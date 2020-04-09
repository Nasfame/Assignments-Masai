with open('emails.txt','r') as f1:
    cont=f1.readlines()

conti = set(cont)
print(len(conti))

dicti = {}

for i in cont:
    if i not in dicti:
        dicti[i]=1
    else:
        dicti[i]+=1
with open('duplicate_emails.txt','w') as f2:
    for x,y in dicti.items():

            x=x.strip('\n')
            y=str(y)+'\n'

            f2.write("{} {}".format(x,y))