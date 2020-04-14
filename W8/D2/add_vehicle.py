import csv
def entry():
    print("Type number,model,colour of the vehicle")
    enter = input().split(',')
    with open("data/details.csv",'r') as f1:
        f1 = csv.reader(f1)
        flag = True
        for i in f1:
            if len(i)>0:
                if i[0] == enter[0]:
                    print("Duplicate entry")
                    flag = False
                    break
    if flag:
        with open("data/details.csv",'a') as f2:
            f2 = csv.writer(f2)
            f2.writerow(enter)

    return

entry()





