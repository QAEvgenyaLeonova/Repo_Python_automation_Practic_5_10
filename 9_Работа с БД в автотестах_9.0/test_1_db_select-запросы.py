from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = 'postgresql://qa:skyqa@5.101.50.27:5432/x_clients'

def test_db_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[3] == 'company'

def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute('select * from company').fetchall()
    row1 = rows[-1]

    assert row1['id'] == 5
    assert row1['name'] == "Служба поддержки QA"

def test_select_1_row():
    db = create_engine(db_connection_string)
    sql_statement = text('select * from company where id = :nazvat_kak_ygodno')

    rows = db.execute(sql_statement, nazvat_kak_ygodno = 1).fetchall()
    assert  len(rows) == 1
    assert rows[0]['name'] == "QA Студия 'ТестировщикЪ'"

def test_select_2_row_with_two_filters():
    db = create_engine(db_connection_string)
    sql_statement = text('SELECT * FROM company c WHERE c.is_active = :is_active AND c.id >= :id')

    rows = db.execute(sql_statement, {'is_active': True, 'id': 2}).fetchall()
    assert  len(rows) == 3


''' Или можно напмсать в формате json передав параметры'''
def test_select_3_row_with_two_filters():
    db = create_engine(db_connection_string)
    sql_statement = text('SELECT * FROM company c WHERE c.is_active = :is_active AND c.id >= :id')

    my_params = {
        'id': 2,
        'is_active': True
    }

    rows = db.execute(sql_statement, my_params).fetchall()
    assert len(rows) == 3




