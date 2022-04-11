import pickle
import random
import time
import scipy.stats as sci
import pandas as pd
import requests
import json
from datetime import datetime
import numpy as np

import Analysing
import Constants
import DateGenerate


def getAllData():
    np.set_printoptions(linewidth=3000)

    for gameID in Constants.gameList:
        # open file with all names
        with open(gameID + 'ItemNames.txt', "rb") as file:  # Unpickling
            allItemNames = pickle.load(file)

        # initialize our Panda's dataframe with the data we want from each item
        allItemsPD = Constants.pd
        currRun = 1  # to keep track of the program running

        # for currItem in allItemNames:  # go through all item names
        for i in range(1):  # go through all item names
            # currItem = allItemNames[i]
            # currItemHTTP = rename(currItem)

            currItemHTTP = 'AK-47%20%7C%20Slate%20%28Field-Tested%29'
            item = requests.get(
                'https://steamcommunity.com/market/pricehistory/?appid=' + '730' + '&market_hash_name=' + currItemHTTP,
                cookies=Constants.cookie)  # get item data
            print(str(currRun), ' out of ', str(len(allItemNames)) + ' code: ' + str(item.status_code))
            currRun += 1
            if item.status_code == 200:
                item = item.content
                item = json.loads(item)
                if item:
                    itemPriceData = item['prices']
                    dataList = dateDistribution(itemPriceData)
                    analysisInformation(dataList)

                else:
                    continue
        # allItemsPD.to_excel('Test_table.xlsx')
        # allItemsPD.to_pickle(gameID + 'PriceData.pkl')
    print('All item data collected')


def analysisInformation(data):
    priceMatrix = []
    countMatrix = []

    for frame in data:
        price = np.array(frame[:, 1], dtype=float)
        priceMatrix.append(price)

        count = np.array(frame[:, 2], dtype=int)
        countMatrix.append(count)
    # print(np.array(priceMatrix))
    # print(np.array(countMatrix))

    priceAvgList = Analysing.createPriceAvgList(priceMatrix)
    countAvgList = Analysing.createPriceAvgList(countMatrix)


def rename(name):
    name = name.replace(' ', '%20')  # convert spaces to %20
    name = name.replace('&', '%26')  # convert & to %26
    name = name.replace("'", '%27')  # convert ' to %27
    name = name.replace("(", '%28')  # convert ( to %28
    name = name.replace(")", '%29')  # convert ) to %29
    name = name.replace("|", '%7C')  # convert | to %7C
    name = name.replace(",", '%2C')  # convert , to %2C
    return name


def dateDistribution(itemPriceData):
    priceList = np.zeros((31, 24, 3), dtype=object)
    date_list = DateGenerate.generateTime()
    itemPriceData = np.asarray(itemPriceData)
    # print(priceList.shape)
    # print(priceList)

    for i in range(len(date_list)):
        for j in range(len(date_list[i])):
            x, y = np.where(itemPriceData == date_list[i][j])
            try:
                (priceList[i, j, 0], priceList[i, j, 1], priceList[i, j, 2]) = (
                    itemPriceData[x][0][0], itemPriceData[x][0][1], itemPriceData[x][0][2])
            except:
                (priceList[i, j, 0], priceList[i, j, 1], priceList[i, j, 2]) = (0, 0, 0)

    np.set_printoptions(linewidth=3000)
    # for i in priceList:
    #     print([(e[0], e[1], e[2]) for e in i])
    return priceList


if __name__ == '__main__':
    getAllData()
