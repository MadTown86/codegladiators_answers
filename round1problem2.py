def main():
    tcases = int(input())
    tcasesfin = tcases
    """
    if tcases >= 1 and tcases <= 10:
        tcasesfin = tcases
    else:
        exit()
    """

    while tcasesfin > 0:

        gbuy = int(input())
        gbuyfin = gbuy
        """
        if gbuy >= 1 and gbuy <= 100000:
            gbuyfin = gbuy
        else:
            exit()
        """

        nbask = int(input())
        """
        if nbask >= 1 and nbask >= gbuyfin:
            nbaskfin = list(range(0, nbask))
        else:
            exit()
        """

        priceraw = input()
        pricelist = priceraw.split(' ')
        intpricelist = [int(val) for val in pricelist]
        sortedintpricelist = sorted(intpricelist)
        """
        for indivp in intpricelist:
            if indivp >= 0 and indivp <= 10000000:
                continue
            else:
                exit()
        """

        cast_gbuyfin = gbuyfin

        totalcost = 0
        for val in range(0, cast_gbuyfin):
            totalcost += sortedintpricelist[val]
        """
        indexedpricedict = {}

        while nbaskfin:
            indexedpricedict[nbaskfin.pop()] = intpricelist.pop()

        highprice = {}
        midprice = {}
        lowprice = {}

        keylist = [key for key in indexedpricedict.keys()]
        for indexnum in keylist:
            if indexedpricedict[indexnum] > 650000:
                highprice[indexnum]=indexedpricedict[indexnum]
                indexedpricedict.pop(indexnum)
            elif 650000 >= indexedpricedict[indexnum] > 350000:
                midprice[indexnum] = indexedpricedict[indexnum]
                indexedpricedict.pop(indexnum)
            else:
                lowprice[indexnum] = indexedpricedict[indexnum]
                indexedpricedict.pop(indexnum)

        totalcost = 0
        purchcount = 0
        templowpricelist = sorted([val for val in lowprice.values()])
        tempmidpricelist = sorted([val for val in midprice.values()])
        temphighpricelist = sorted([val for val in highprice.values()])
        while purchcount < int(gbuyfin):
            while templowpricelist:
                if purchcount < gbuyfin:
                    if len(templowpricelist) > 1:
                        totalcost += templowpricelist.pop(templowpricelist.index(min(templowpricelist)))
                        purchcount += 1
                    else:
                        totalcost += templowpricelist.pop(0)
                        purchcount += 1
                else:
                    break

            while tempmidpricelist:
                if purchcount < gbuyfin:
                    if len(tempmidpricelist) > 1:
                        totalcost += tempmidpricelist.pop(tempmidpricelist.index(min(tempmidpricelist)))
                        purchcount += 1
                    else:
                        totalcost += tempmidpricelist.pop(0)
                        purchcount += 1
                else:
                    break

            while temphighpricelist:
                if purchcount < gbuyfin:
                    if len(temphighpricelist) > 1:
                        totalcost += temphighpricelist.pop(temphighpricelist.index(min(temphighpricelist)))
                        purchcount += 1
                    else:
                        totalcost += temphighpricelist.pop(0)
                        purchcount += 1
                else:
                    break
        """

        print(totalcost)
        tcasesfin -= 1

if __name__ == '__main__':
    main()




