from datetime import datetime
import os
from bs4 import BeautifulSoup

def savePage(page, text='', folder=''):
    text = text + '_' if text != '' else text
    if folder == '':
        file = open(f'{text}{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.html', 'w', encoding="utf-8")
    else:
        file = open(
            os.path.join(f'SavedPages/{folder}', str(f'{text}{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.html')),
            'w',
            encoding="utf-8")
    file.write(BeautifulSoup(page.content).prettify())
    file.close()
    print('Page saved')