import requests

url = 'https://xn--90adear.xn--p1ai/news/region?perPage=20&page=2&region=65'
headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0',
    'X-Requested-With': 'xmlhttprequest'
}
params = {
    'perPage':30,
    'page':3,
    'region':65
}
response = requests.get(url, headers=headers, meta=params)
print(1)
