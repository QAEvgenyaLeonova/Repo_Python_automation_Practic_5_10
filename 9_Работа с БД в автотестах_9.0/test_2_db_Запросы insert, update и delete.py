from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = 'postgresql://qa:skyqa@5.101.50.27:5432/x_clients'

def test_insert():
    db = create_engine(db_connection_string)
    sql = text('insert into company ("name") values (:new_name)')

    rows = db.execute(sql, new_name = 'SkyPro')

def test_update():
    db = create_engine(db_connection_string)
    sql = text('update company set description = :descr where id = :id')

    db.execute(sql, descr = 'New description', id = 8)

def test_delete():
    db = create_engine(db_connection_string)
    sql = text('delete from company c where id = :id')

    db.execute(sql, id=9)