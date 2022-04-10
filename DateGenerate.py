import pytz
from datetime import datetime, timedelta


def generateTime():
    date_list = []
    for delta_days in range(31):
        date_list.append([])
        payTime = datetime.now(pytz.timezone('Europe/London')) - timedelta(days=delta_days)
        for hour in ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
                     '16', '17', '18', '19', '20', '21', '22', '23']:
            date_list[delta_days].append(payTime.strftime(f'%b %d %Y {hour}: +0'))
    return date_list


if __name__ == '__main__':
    s= generateTime()
    for i in range(30):
        print(s[i])

"""
['Apr 09 2022 16: +0', 312.937, '93']
['Apr 09 2022 17: +0', 305.868, '94']
['Apr 09 2022 18: +0', 310.44, '115']
"""
