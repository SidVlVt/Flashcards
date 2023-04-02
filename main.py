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

#  создаем главную функцию программы
def main():
    print(get_user_link())

#  точка входа в программу
if __name__ == '__main__':
    main()