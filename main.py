import requests
import bs4
import fake_headers


if __name__ == '__main__':

    headers = fake_headers.Headers(browser='firefox', os='win')
    headers_dict = headers.generate()
    url = 'https://spb.hh.ru/search/vacancy?text=python+django+flask&area=1&area=2&items_on_page=20'
    response = requests.get(url, headers=headers_dict)
    html_data = response.text
    soup = bs4.BeautifulSoup(html_data, 'lxml')
    
    articles_list = bs.find_all(class_=“vacancy-serp-item__layout”)

    vacancy_list = []

    for article in articles_list:
        link = article.find(‘a’)[‘href’]
        if salary = article.find(‘span’, class_=“bloko-header-section-3”):
            salary = article.find(‘span’, class_=“bloko-header-section-3”)
        company = article.find(‘a’, class_=‘bloko-link bloko-link_kind-tertiary’).text
        city = article.find(‘div’,{‘data-qa’:‘vacancy-serp__vacancy-address’}).text
        
        vacancy_list.append({'link': link, 'salary': salary, 'company': company, 'city': city})
    
    with open('vacancy_list.json', 'w', encoding='utf-8') as f:
            json.dump(vacancy_list, f, ensure_ascii=False, indent=2)
    print()

