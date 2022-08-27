import json
from json.decoder import JSONDecodeError

from settings import DB
from datetime import datetime


def get_all_data():
    with open(DB) as f:
        try:
            return json.load(f)
        except JSONDecodeError:
            return []


def create_data():
    id_ = datetime.now().strftime('%H%M%S')
    data = {
        'id': id_,
        'title': input('Введите название: '),
        'price': int(input('Введите цену: ')),
        'description': input('Введите описание: '),
        'data_created': datetime.now().strftime('%d.%m.%Y %H:%M'),
        'data_update': '',
        'status': 'Продается'

    }
    json_data: list = get_all_data()
    json_data.append(data)
    with open(DB, 'w') as f:
        json.dump(json_data, f, indent=4)


def buy():
    id = input('Введите id: ')
    data = get_all_data()
    for i in data:
        if i['id'] == id:
            sum_ = int(input('Введите сумму: '))
            if i['price'] <= sum_:
                i['status'] = 'Продано'
            with open(DB, 'w') as f:
                json.dump(data, f, indent=4)
            return None
        print("""
            Такого id не существует!
        
            Существующие id:
        """)
    for list in data:
        print(f"""
            ---------------------------------
            id: {list['id']}
            title: {list['title']}
            ---------------------------------
        """)

def get_data_by_id():
    id_ = input('Введите id: ')
    data = get_all_data()
    for obj in get_all_data():
        if obj['id'] == id_:
            return obj
        elif obj['id'] != id_:
            print("""
    Такого id не существует!
    
        Существующие id:
    """)
            for list in data:
                print(f"""
        id: {list['id']}
        title: {list['title']}
                """)
            break


def delete_data():
    id_ = input('Введите id: ')
    data = get_all_data()
    for obj in data:
        if obj['id'] == id_:
            data.remove(obj)
            break
    with open(DB, 'w') as f:
        json.dump(data, f, indent=4)
    print("""
        Такого id не существует!
    
        Существующие id:
    """)
    for list in data:
        print(f"""
        ---------------------------------
        id: {list['id']}
        title: {list['title']}
        ---------------------------------
        """)
        

def update():
    id_ = input('Введите id: ')
    data = get_all_data()
    for obj in data:
        if obj['id'] == id_:
            obj['title'] = input('Введите название: ') or obj['title']
            try:
                obj['price'] = int(input('Введите цену: ')) or obj['price']
            except ValueError:
                obj['price']
            obj['description'] = input('Введите описание: ')     
            obj['data_update'] = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            with open(DB, 'w') as f:
                json.dump(data, f, indent=4)
            return None
    print('Такого id не существует!!!', '\n'
    'Выберите id нужного вам товара:', '\n'
            )
            
    for list in data:
        print('id', list['id'], list['title'], '\n')
         

def get_price():
    print("""
    Выберите тип фильтрации:
    1. Показывает товары чья цена больше указанной суммы
    2. Показывает товары чья цены меньше указанной суммы
    """)
    price_ = int(input('Введите цену для фильтрации: '))
    num = input('Указать тип фильтрации: ')
    data = get_all_data()
    for obj in data:
        super_list = (f"""
        ---------------------------------
        id: {obj['id']}
        title: {obj['title']}
        price: {obj['price']}
        description: {obj['description']}
        data_created: {obj['data_created']}
        data_update: {obj['data_update']}
        status: {obj['status']}
        ---------------------------------
        """)
        if num == '1':
            if obj['price'] > price_:
                print (super_list)
        elif num == '2':
            if obj['price'] < price_:
                print(super_list)


def get_status():
    print("""
    Выберите тип фильтрации:
    1. Показывает имеющиеся товары
    2. Показывает проданные товары
    """)
    num = input()
    data = get_all_data()
    super_list = (f"""
    Товар № {num}
    ---------------------------------
    id: {obj['id']}
    title: {obj['title']}
    price: {obj['price']}
    description: {obj['description']}
    data_created: {obj['data_created']}
    data_update: {obj['data_update']}
    status: {obj['status']}
    ---------------------------------
    """)
    for obj in data:
        if num == '1':
            if obj['status'] == 'Продается':
                print(super_list)
        elif num == '2':
            if obj['status'] == 'Продано':
                print(super_list)

 
def all_data():
    data = get_all_data()
    num = 0
    for obj in data:
        num += 1
        print(f"""
        Товар № {num}
        ---------------------------------
        id: {obj['id']}
        title: {obj['title']}
        price: {obj['price']}
        description: {obj['description']}
        data_created: {obj['data_created']}
        data_update: {obj['data_update']}
        status: {obj['status']}
        ---------------------------------
         """)


def interface():
    info_data = """
        0. Список функций
        1. create - создать новый продукт
        2. delete - удалить продукт по id
        3. list - получить список всех продуктов
        4. retrieve - получить продукт по id
        5. update - изменить данные
        6. buy - купить товар
        7. filter price - фильтрация по цене
        8. filter status - фильтрация по статусу
        9. exit - выйти из программы
        """  
    print(info_data)
    while True:
        name = input()
        if name == '0':
            print(info_data)
        elif name == '1':
            create_data()
        elif name == '2':
            delete_data()
        elif name == '3':
            all_data()
        elif name == '4':
            get_data_by_id()
        elif name == '5':
            update()
        elif name == '6':
            buy()
        elif name == '7':
            get_price()
        elif name == '8':
            get_status()
        elif name == '9':
            break
        else:
            print('Функция с таким номером отсутствует')
            break
