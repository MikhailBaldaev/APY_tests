import pytest
from main import list_search, unique, max_value
from YaDisk import createfolder, get_folder_info


@pytest.mark.parametrize(
    'x, y, etalon',
    [
        ([{'visit1': ['Москва', 'Россия']},{'visit2': ['Дели', 'Индия']}], 'Индия', [{'visit2': ['Дели', 'Индия']}]),
        ([{0: [0]}], 'word', []),
        ([{'user1': [213, 213, 213, 15, 213]}, {'user2': [54, 54, 119, 119, 119]}], 213, [{'user1': [213, 213, 213, 15, 213]}])
     ]
)
def test_list_search(x, y, etalon):
    func = list_search(x, y)
    assert func == etalon
    assert isinstance(func, list)


def test_list_search_raises():
    with pytest.raises(TypeError):
        func = list_search(11, 'Индия')


@pytest.mark.parametrize(
    'x, etalon',
    [
        ({'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}, [98, 35, 15, 213, 54, 119]),
        ({'1': [0, 1, 2, 3, 4],
       '2': [4, 5, 6, 7, 8],
       '3': [9]}, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    ]
)
def test_unique(x, etalon):
    func = unique(x)
    assert sorted(func) == sorted(etalon)
    assert isinstance(func, list)


def test_unique_raises():
    with pytest.raises(AttributeError):
        func = unique(())


@pytest.mark.parametrize(
    'x, etalon',
    [
        ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'yandex'),
        ({'1': 1,
          '2': 4,
          '3': 9},'3')
    ]
)
def test_max_value(x, etalon):
    func = max_value(x)
    assert func == etalon
    assert isinstance(func, str)


params = [
  ("name", 201),
  ("name2", 201),
  ("name3", 201),
]
@pytest.mark.parametrize("name, result", params)
def test_yandex(name, result):
    func1 = createfolder(name)
    func2 = get_folder_info(name)
    assert func1 == result
    assert func2 == True