# Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.
urls_list = ['https://yandex.ru/pogoda/?lat=55.8696773',
             'https://sportmail.ru/football2022/match/315882/?fromwidget=1',
             'https://ag.mos.ru/home',
             'https://gb.ru/lessons/284812',
             'https://www.hoyolab.com/article/7851051']
def poisk_domen(url: list) -> list:            
    domen_list = list(map(lambda i: i[:i.find('/')], [i for i in map(lambda i: i.replace('https://',''), url)]))
    return domen_list
print(poisk_domen(urls_list))