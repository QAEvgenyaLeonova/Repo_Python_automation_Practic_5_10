import pytest

football_stats = {
    'Число стран': 48,
    'Страна': 'Катар',
    'Участники': ['Австралия', 'Англия', 'Аргентина', 'Бельгия', 'еще 42 страны', 'Эквадор', 'Япония'],
    'Награды': {
        'Золотой мяч': 'Лионель Месси',
        'Серебряный мяч': 'Килиан Мбаппе',
        'Золотая бутса': 'Килиан Мбаппе',
        'Серебряная бутса': 'Килиан Мбаппе',
        'Больше всего голов': {
            'Игрок': 'Килиан Мбаппе - капитан команды',
            'Количество мячей': 8
        }
    }
}

empty_dict = {}

def test_read_list():
    participants = football_stats['Участники']#верни мне в переменную ключ учвстники
    #participants = ['Австралия', 'Англия', 'Аргентина', 'Бельгия', 'еще 42 страны', 'Эквадор', 'Япония']
    england = football_stats['Участники'][1]

    assert participants[0] == 'Австралия'
    assert len(participants) > 0
    assert england == 'Англия'

def test_read_dict():
    total_goals = football_stats['Награды']['Больше всего голов']['Количество мячей']
    assert  total_goals == 8

def test_save_dict():
    awards = football_stats['Награды']
    player = awards['Больше всего голов']['Игрок']
    assert player == 'Килиан Мбаппе - капитан команды'

def test_read_error():
    with pytest.raises(KeyError):
        empty_dict['key'] #None

def test_get_empty():
    value = empty_dict.get('key')
    assert value == None

def test_get_empty_or_deffault():
    value = empty_dict.get('key', 'abc123')
    assert value == 'abc123'

