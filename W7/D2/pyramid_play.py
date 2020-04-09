def py(lv=4):

    lini = '.'*(lv+1)
    li = list(lini)


    for i in range(lv):
        lvi = i+1
        li[i]='O'

        if lvi>2:
            while i>1:
                li[i-2]='O'
                i-=2
        rev = li[::-1]
        print(*rev,*li[1:])

        li = list(lini)


pp=[]
def inv(lv=4):

    lini = '.'*(lv+1)
    li = list(lini)
    final=[]

    for i in range(lv):
        lvi = i+1
        li[i]='O'

        if lvi>2:
            while i>1:
                li[i-2]='O'
                i-=2
        rev = li[::-1]
        final.append(rev+li[1:])
        li = list(lini)
    final.reverse()
    return final




def rho(lv=8):
    z = int(lv/2)
    py(z)

    tb = inv(lv-z)
    if lv%2!=0:
        tb = inv(lv-z-1)

    for i in range(1,lv-z):
        print(*tb[i])
