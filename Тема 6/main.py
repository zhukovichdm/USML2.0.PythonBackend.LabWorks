import csv
import urllib.request
from bs4 import BeautifulSoup


# Получаем все ссылки на курсы и их названия.
def get_all_course(html):
    soup = BeautifulSoup(html)
    all_course = soup.find_all('a', class_='course-promo-widget__title ember-view ember-link')

    # for a in all_course:
    #     html = a.get('href')
    #     # name = a.next_element
    #     # print(html, name)
    #
    #     # Получаем информацию о каждом курсе.
    #     result = get_info_for_curse(urllib.request.urlopen(html).read())
    #
    #     with open('result.csv', "w", newline="") as file:
    #         writer = csv.writer(file)
    #
    #         writer.writerows(result)

    with open('result.csv', "w", newline="") as file:
        writer = csv.writer(file)
        for a in all_course:
            html = a.get('href')
            # name = a.next_element
            # print(html, name)

            # Получаем информацию о каждом курсе.
            result = get_info_for_curse(urllib.request.urlopen(html).read())
            writer.writerows(result)






def get_info_for_curse(html):
    soup = BeautifulSoup(html)

    # Название курса.
    title = soup.find('h1', class_='course-preview__title')
    print(title.next_element)

    # Основная информация о курсе.
    course = soup.find_all('div', class_='course-index__def-row')
    load = course[0].next_element.next_element.next_element.next_element.next_element.next_element
    time = course[1].next_element.next_element.next_element.next_element.next_element.next_element
    language = course[2].next_element.next_element.next_element.next_element.next_element.next_element
    certificate = str
    try:
        certificate = course[3].next_element.next_element.next_element.next_element.next_element.next_element
    except:
        pass
    # print(load, time, language, certificate)

    # Описание курса.
    description = soup.find('p', class_='ember-view')
    print(description)

    # Информация о преподователях
    autor = soup.find_all('div', class_='author-widget__right')
    autors = []
    for a in autor:
        name = a.next_element.next_element.next_element
        info = a.next_element.next_element.next_element.next_element.next_element.next_element
        print(name, info)
        autors.append([name, info])

    result = [
        ['Title', title.next_element],
        ['Load', load],
        ['Time', time],
        ['Language', language],
        ['Certificate', certificate],
        ['Description', description],
        ['Autors', autors]
    ]

    return result


# Проверка на сохраненных страницах.
def parse_file():
    main_html = open('Stepik.html', encoding='utf-8').read()
    get_all_course(main_html)

    course_html = open('Course1.html', encoding='utf-8').read()
    get_info_for_curse(course_html)


def parse():
    main_html = open('Stepik.html', encoding='utf-8').read()
    get_all_course(main_html)


if __name__ == '__main__':
    parse()
    # parse_file()
