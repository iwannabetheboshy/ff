import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent









def set_cookies():
    ua = UserAgent()
    userAgent = ua.random

    headers = {
        # 'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
        # 'Sec-Ch-Ua-Mobile': '?0',
        # 'User-Agent': userAgent,
        # 'Sec-Ch-Ua-Arch': '""',
        # 'Sec-Ch-Ua-Full-Version': '""',
        # 'Accept': 'application/json, text/javascript, */*; q=0.01',
        # 'Sec-Ch-Ua-Platform-Version': '""',
        # 'X-Requested-With': 'XMLHttpRequest',
        # 'Sec-Ch-Ua-Bitness': '""',
        # 'Sec-Ch-Ua-Model': '""',
        # 'Sec-Ch-Ua-Platform': '"Windows"',
        # 'Sec-Fetch-Site': 'same-origin',
        # 'Sec-Fetch-Mode': 'cors',
        # 'Sec-Fetch-Dest': 'empty',

        'Upgrade-Insecure-Requests': '1',
        'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Full-Version': '""',
        'Sec-Ch-Ua-Arch': '""',
        'Sec-Ch-Ua-Platform-Version': '""',
        'Sec-Ch-Ua-Model': '""',
        'Sec-Ch-Ua-Bitness': '""',
        'User-Agent': userAgent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Priority': 'u=0, i'
    }

    response = requests.get('https://wwww.farpost.ru', headers={'User-Agent': userAgent})
    cookies = {i.split('=')[0]: i.split('=')[1] for i in response.headers['Set-Cookie'].split(';') if i != ' secure'}

    print(response.headers['Set-Cookie'])
    return headers, cookies



h, c = set_cookies()
c['ring'] = 'dde278d3c21bd2cbd802cbf2144315a0'

while True:
    response = requests.get('https://www.farpost.ru/vladivostok/service/internet/?pageOrderKeys=0&ajax=2&city=1', cookies=c, headers=h)
    soup = BeautifulSoup(response.text, 'lxml')
    links = soup.find_all('title')
    print(links)
    print('h =', h)
    print('c =', c)
    print()


    print('-------------------------')
    print(response.headers)
    print('-------------------------')

    if links != []:
        h, c = set_cookies()
