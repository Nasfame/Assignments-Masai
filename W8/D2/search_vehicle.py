import csv
def search():
    print("Your vehicle number")
    vin_num = input()
    with open("data/details.csv",'r') as f1:
        f1 =csv.reader(f1)
        flag = True


        for i in f1:
            if len(i)>0:
                if i[0]== vin_num:
                    print(*i)
                    flag= False
                    break
        if flag:
            print("vin_number not found!")

