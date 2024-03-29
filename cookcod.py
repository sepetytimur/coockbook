



def get_shop_list_by_dishes(menu, dishes, person_count):
    ee = {}
    for name in dishes:
        for ingridient in menu[name.strip()]:
            # ingridient = dict[name]
            # print(ingridient)
            if ingridient['ingridient_name'] in ee.keys():
                ee[ingridient['ingridient_name']]['quantity'] += ingridient['quantity'] * person_count
            else:
                ee[ingridient['ingridient_name']] = {
                    'measure': ingridient['measure'],
                    'quantity': ingridient['quantity'] * person_count
                }

    return ee


def read_you_cbook(name_of_file):
    menu = {}
    with open(name_of_file) as f:
        while True:
            title = f.readline().strip()
            # print(type(line))
            if not title:
                break
            menu[title] = []
            num = f.readline()
            n = int(num)

            for i in range(n):
                [ingridient_name, quantity, measure] = f.readline().split('|')
                menu[title].append({
                    'ingridient_name': ingridient_name.strip(),
                    'quantity': int(quantity.strip()),
                    'measure': measure.strip()
                })

            f.readline()

    return menu


def main():
    menu = read_you_cbook('cookbook')

    names = input('введите название блюд').split(',')
    number = int(input('введите колличество гостей'))
    print(menu)

    shop = get_shop_list_by_dishes(menu, names, number)
    print(shop)

#
# {
# 'Картофель': {'measure': 'кг', 'quantity': 2},
# 'Молоко': {'measure': 'мл', 'quantity': 200},
#  'Помидор': {'measure': 'шт', 'quantity': 4},
# 'Сыр гауда': {'measure': 'г', 'quantity': 200},
#  'Яйцо': {'measure': 'шт', 'quantity': 4},
# 'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
#
#
#
#
#
if __name__ == '__main__':
    main()


