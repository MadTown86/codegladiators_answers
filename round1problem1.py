def main():
    ltime = input().split(" ")
    if int(ltime[0]) > 24:
        exit()
    elif int(ltime[0]) < 0:
        exit()
    elif int(ltime[1]) > 59:
        exit()
    elif int(ltime[1]) < 0:
        exit()
    lth = int(ltime[0])
    ltm = int(ltime[1])
    ttime = input().split(" ")
    if int(ttime[0]) > 24:
        exit()
    elif int(ttime[0]) < 0:
        exit()
    elif int(ttime[1]) > 59:
        exit()
    elif int(ttime[1]) < 0:
        exit()
    tth = int(ttime[0])
    ttm = int(ttime[1])

    if (lth + tth) > 24:
        blasth = (lth - 24) + tth
    else:
        blasth = lth + tth


    if (ttm + ltm) == 60:
        blasth += 1
        blastm = 0
        if blasth >= 24:
            blasth = blasth - 24
            blastm = 0
        else:
            pass
    elif blasth == 24 and (ttm + ltm) < 60:
        blasth = 0
        blastm = (ttm + ltm)
    elif (ltm + ttm) > 59:
        if blasth + 1 >= 24:
            blasth = 0
        else:
            blasth += 1
        blastm = (ltm + ttm) - 60
    else:
        blastm = (ltm + ttm)

    print("{:0>2d} {:0>2d}".format(blasth, blastm))

main()