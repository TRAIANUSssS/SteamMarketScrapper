import numpy as np


def createPriceAvgList(priceMatrix):
    priceAvgList = []
    [(priceAvgList.append(np.average(e, weights=(e != 0)))) for e in priceMatrix]
    print(priceAvgList)
    return priceAvgList


def createCountAvgList(countMatrix):
    countAvgList = []
    [(countAvgList.append(np.average(e, weights=(e != 0)))) for e in countAvgList]
    print(countAvgList)
    return countAvgList
