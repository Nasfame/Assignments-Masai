
print("Hi, Please select the service you are looking via this keymap")
print("1 Total no of vehicles registered")
print("2 Vehicle Entry")
print("3 Know more on your vehicle")
z = int(input())


if z == 1:
    import count as c
    print(c.count())
elif z ==2:
    import add_vehicle as a
    a.entry()
elif z==3:
    import search_vehicle as s
    s.search()
else:
    print("wrong cmd,Try again")