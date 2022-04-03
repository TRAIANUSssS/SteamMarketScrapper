import pickle
import random
import time
import requests
import json

import Constants
import Logs


def getAllNames():
    for gameID in Constants.gameList:
        # itialize
        allItemNames = []

        # find total number items
        allItemsGet = requests.get(
            'https://steamcommunity.com/market/search/render/?search_descriptions=0&sort_column=default&sort_dir=desc&appid=' + gameID + '&norender=1&count=100',
            cookies=Constants.cookie)  # get page

        if allItemsGet.status_code == 403:
            Logs.savePage(allItemsGet, text='stCode403', folder='Test')
        allItems = allItemsGet.content  # get page content

        allItems = json.loads(allItems)  # convert to JSON
        totalItems = allItems['total_count']  # get total count

        # you can only get 100 items at a time (despite putting in count= >100)
        # so we have to loop through in batches of 100 to get every single item name by specifying the start position
        for currPos in range(0, totalItems + 50, 50):  # loop through all items
            time.sleep(random.uniform(0.5, 2.5))  # you cant make requests too quickly or steam gets mad

            # get item name of each
            allItemsGet = requests.get('https://steamcommunity.com/market/search/render/?start=' + str(
                currPos) + '&count=100&search_descriptions=0&sort_column=default&sort_dir=desc&appid=' + gameID + '&norender=1&count=5000',
                                       cookies=Constants.cookie)
            print('Items ' + str(currPos) + ' out of ' + str(totalItems) + ' code: ' + str(
                allItemsGet.status_code))  # reassure us the code is running and we are getting good returns (code 200)

            allItems = allItemsGet.content
            allItems = json.loads(allItems)
            allItems = allItems['results']
            for currItem in allItems:
                allItemNames.append(currItem['hash_name'])  # save the names

        # remove dupes by converting from list to set and back again
        allItemNames = list(set(allItemNames))

        # Save all the name so we don't have to do this step anymore
        # use pickle to save all the names so i dont have to keep running above code
        with open(gameID + 'ItemNames.txt', "wb") as file:  # change the text file name to whatever you want
            pickle.dump(allItemNames, file)


if __name__ == '__main__':
    getAllNames()