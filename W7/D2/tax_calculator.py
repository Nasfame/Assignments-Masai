def tax(amt, sav):
    amt = amt / 100000
    sav = sav / 100000

    if amt < 2.5:
        taxi = (0, 0.5 * sav)



    elif amt > 2.5 and amt < 5:
        taxi = (0.1 * amt, 0.3 * sav)
    elif amt > 10:
        if 0.1 * sav > 0.5:
            taxi = (0.3 * amt, 0.5)
        else:
            taxi = (0.3 * amt, 0.1 * sav)
    else:
        taxi = (0.2 * amt, 0.3 * sav)

    return taxi[0]*10**5,taxi[1]*10**5



