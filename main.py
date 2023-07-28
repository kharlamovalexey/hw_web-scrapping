import requests
import bs4
import fake_headers


if __name__ == '__main__':

    headers = fake_headers.Headers(browser='firefox', os='win')
    headers_dict = headers.generate()

    response = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2', headers=headers_dict)
    html_data = response.text
    soup = bs4.BeautifulSoup(html_data, 'lxml')
    print()

