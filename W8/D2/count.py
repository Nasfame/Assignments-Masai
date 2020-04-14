from csv import reader
def count():
    c = 0
    with open("data/details.csv",'r') as f1:
        cnt = reader(f1)

        for i in cnt:
            if len(i)>0:
                c+=1
    return c

count()