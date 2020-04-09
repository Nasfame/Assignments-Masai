import time
def time_dec(fc):
    def inner(*args):
        t1=time.time()

        fc(*args)
        t2=time.time()
        print(t2-t1)
    return inner



