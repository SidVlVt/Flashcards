import requests
from bs4 import BeautifulSoup


#  Step 1
#  функция запрашивает у пользователя ссылку и проверяет её
def get_user_link():
    value_stop = 1
    while value_stop == 1:
        link = input('Введите ссылку:\n')
        if link[:8] == 'https://':
            return link
        else:
            print('Неправильный формат ссылки, ссылка должна быть вида "https://"\n'
                  'Выберите дальнейшее действие.\n'
                  'Для повторного ввода ссылки введите - 1\n'
                  'Для закрытия программы введите - 0')
            value_stop = int(input())
    print('Закрытие программы - досвидания!')


#  Step 2
# функция принимает в себя объект bs4 c параграфами и отдает список со всеми словами из этих параграфов
def get_all_words(object):
    list_all_words = []

    for i in object:
        i = i.text
        list_words = i.split()
        for j in list_words:
            if j[-1] in '.,':
                j = j[:-1]
            if j.isalpha():
                list_all_words.append(j.lower())

    return list_all_words


#  функция парсит необходимые значения по ссылке полученной из Step 1
def parsing(link):
    response = requests.get(url=link)
    soup = BeautifulSoup(response.text, 'lxml')

    title = soup.find('title').text.strip()
    tags_p = soup.find_all('p')
    list_all_words = get_all_words(tags_p)

    return title, list_all_words


#  создаем главную функцию программы
def main():
    link = get_user_link()
    title, list_all_words = parsing(link)
    print(title)
    print(*list_all_words, sep='\n')


#  точка входа в программу
if __name__ == '__main__':
    main()