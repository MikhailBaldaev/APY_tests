geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def list_search(iter_obj, word):
    result = [{k: v for (k, v) in i.items()} for i in iter_obj if word in list(i.values())[0]]
    return result


def unique(iter_obj):
    result = {i for lis in [v for (k, v) in iter_obj.items()] for i in lis}
    return list(result)


def max_value(key_values):
    max_v = 0
    for k, v in key_values.items():
        if v > max_v:
            result = {k: v}
            max_v = v
    return list(result.keys())[0]

if __name__ == '__main__':
    print(list_search(geo_logs, 'Россия'))
    print(unique(ids))
    print(max_value(stats))