import re
import csv


def find_index(name, result_list):
    first_name, last_name = name.split()
    for item in result_list:
        if first_name == item[0] and last_name == item[1]:
            return result_list.index(item)


def compare_value(value_1, value_2):
    return (value_1, value_2)[value_1 == '']


def get_full_name(name):
    full_name = ' '.join(name[:3])
    if name == ['', '', '']:
        return name
    if len(full_name.split()) == 3:
        return full_name.split()
    else:
        return full_name.split() + ['']


def compare_name(name_1, name_2):
    name_1 = get_full_name(name_1)
    name_2 = get_full_name(name_2)
    res = []
    for index, name in enumerate(name_1):
        res.append((name_2[index], name)[name != ''])
    return res


def add_data_in_result(pattern_1, pat_rep_phone_add, pat_rep_phone, data_1, data_2=None):
    if data_2 is None:
        data_2 = ['', '', '', '', '', '', '']
    full_name = compare_name(data_1[:3], data_2[:3])
    organization = compare_value(data_1[3], data_2[3])
    position = compare_value(data_1[4], data_2[4])
    _pat_replace = pat_rep_phone_add if 'доб' in data_1[5] else pat_rep_phone
    phone = compare_value(
        re.sub(pattern_1, _pat_replace, data_1[5]),
        re.sub(pattern_1, _pat_replace, data_2[5])
    )

    email = compare_value(data_1[6], data_2[6])
    return [*full_name, organization, position, phone, email]


def main():
    pattern_phone = r'\+?([7|8])\s*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s+\(*доб.]*(\d+)*\)*'
    pattern_replace_phone = r'+7(\2)\3-\4-\5'
    pattern_replace_phone_add = r'+7(\2)\3-\4-\5 доб.\6'

    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    result = [contacts_list[0]]
    name_dict = {}

    for data in contacts_list[1:]:
        check_name = ' '.join(get_full_name(data[:3])[:2])
        if check_name in name_dict:
            value = find_index(check_name, result)
            result[value] = add_data_in_result(pattern_phone,
                                               pattern_replace_phone_add,
                                               pattern_replace_phone,
                                               result[value],
                                               data
                                               )
        else:
            result.append(add_data_in_result(pattern_phone,
                                             pattern_replace_phone_add,
                                             pattern_replace_phone,
                                             data
                                             )
                          )
            name_dict[check_name] = None

    with open("phonebook.csv", "w", encoding='utf-8', newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(result)

if __name__ == '__main__':
    main()