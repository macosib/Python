import os
from pprint import pprint

with open(os.path.join(os.getcwd(), 'recipes.txt'), 'r', encoding='UTF-8') as recipes_book:
    cook_book = {}
    for line in recipes_book.readlines():
        if '|' not in line.strip() and not line.strip().isdigit() and len(line.strip()) != 0:
            cook_book.setdefault(line.strip(), [])
            dish = line.strip()
        elif '|' in line.strip():
            ingredient_dict = {}
            ingredient_dict['ingredient_name'] = line.strip().split('|')[0].strip()
            ingredient_dict['quantity'] = int(line.strip().split('|')[1].strip())
            ingredient_dict['measure'] = line.strip().split('|')[2].strip()
            cook_book[dish].append(ingredient_dict)
        else:
            continue


def get_shop_list_by_dishes(dishes: list, person_count: int):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                update_result = {ingredient['ingredient_name']: {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }}
                if ingredient['ingredient_name'] not in result:
                    result.update(update_result)
                else:
                    result[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return result


# pprint(cook_book)
# print()
# pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
