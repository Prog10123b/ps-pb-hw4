cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
            {'user': users[1], 'city': cities[0]},
            {'user': users[2], 'city': cities[1]}]

city = input('Введите город: ')   #input

for tourist in tourists:          #итерирование по массиву
    if city.lower() == tourist['city'].lower():     #сравнивание
        print(f'Турист {tourist["user"]["name"]} возраст {tourist["user"]["age"]}. Посетил город {tourist["city"].lower()}')  #вывод результата на экран
