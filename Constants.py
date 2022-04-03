import pandas as pd


gameList = ['218620']
cookie = {'steamLoginSecure': '76561198823388271%7C%7CD6F8ADE139B6722E5D6E504121C936245287A293',
          'ActListPageSize': '10',
          '_ga': 'GA1.2.869442218.1648418074',
          '_gid': 'GA1.2.1081667056.1648418074',
          'browserid': '2498941715216671058',
          'sessionid': 'f96a86d3e7d4257d34cde7c0',
          'steamCountry': 'RU%7Cfe14595ade32e2cb5d41be3085969834',
          'steamMachineAuth76561198271348817': '8AE27C06C4743D644367F819A314C2EB5614B9F6',
          'steamMachineAuth76561198823388271': '9E4A365D4497763F12777D0EF20447FCFECBBB30',
          'steamRememberLogin': '76561198271348817%7C%7C67fbfb6771d18ecb6a52b84ed6ac6c50',
          'timezoneOffset': '10800,0'
          }

allItemsPD = pd.DataFrame(data=None, index=None,
                                  columns=['itemName', 'initial', 'timeOnMarket', 'priceIncrease', 'priceAvg',
                                           'priceSD',
                                           'maxPrice', 'maxIdx', 'minPrice', 'minIdx', 'swing', 'volAvg', 'volSD',
                                           'slope',
                                           'rr'])