import requests
import bs4
import fake_headers
import json


if __name__ == '__main__':

    headers = fake_headers.Headers(browser='firefox', os='win')
    headers_dict = headers.generate()

    pages = 5
    vacancy_list = []

    for i in range(pages):
        params = {'text': 'python django flask','area': [1, 2], 'items_on_page': 20, 'page': i}

        url = 'https://spb.hh.ru/search/vacancy'

        response = requests.get(url=url, headers=headers_dict, params=params)

        html_data = response.text
        html = bs4.BeautifulSoup(html_data, 'lxml')
        
        articles_list = html.find_all(class_='vacancy-serp-item__layout')

        for article in articles_list:
            salary = ''
            link = article.find('a')['href']

            if article.find('span', class_='bloko-header-section-2'):
                salary = article.find('span', class_='bloko-header-section-2').text
                
            company = article.find('a', class_='bloko-link bloko-link_kind-tertiary').text
            city = article.find('div', {'data-qa':'vacancy-serp__vacancy-address'}).text.split(',')[0]
            
            vacancy_list.append({'link': link, 'salary': salary, 'company': company, 'city': city})
    
    with open('vacancy_list.json', 'w', encoding='utf-8') as f:
            json.dump(vacancy_list, f, ensure_ascii=False, indent=2)
