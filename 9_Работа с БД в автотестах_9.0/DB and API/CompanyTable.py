from sqlalchemy import create_engine, text

class CompanyTable:
    __scripts = {
        "select": text("SELECT * FROM company WHERE deleted_at IS NULL"),
        "select_active": text("SELECT * FROM company WHERE \"is_active\" = TRUE AND deleted_at IS NULL"),
        "delete_by_id": text("DELETE FROM company WHERE id = :id_to_delete"),
        # Используем RETURNING, чтобы получить ID новой записи сразу после вставки
        "insert_new": text("INSERT INTO company(\"name\") VALUES (:new_name) RETURNING id"),
        "get_max_id": text("SELECT MAX(\"id\") FROM company WHERE deleted_at IS NULL"),
        "select_by_id": text("SELECT * FROM company WHERE id = :select_id AND deleted_at IS NULL")
    }

    def __init__(self, connection_string):
        # echo=True покажет SQL-запросы в консоли (полезно для отладки)
        self.__db = create_engine(connection_string, echo=False)

    def _get_connection(self):
        """Создает соединение. Используем контекстный менеджер в методах для авто-закрытия."""
        return self.__db.connect()

    def get_companies(self):
        with self._get_connection() as conn:
            result = conn.execute(self.__scripts["select"])
            return result.mappings().all()

    def get_active_companies(self):
        with self._get_connection() as conn:
            result = conn.execute(self.__scripts["select_active"])
            return result.mappings().all()

    def delete(self, id_val):
        with self._get_connection() as conn:
            trans = conn.begin()
            try:
                conn.execute(self.__scripts["delete_by_id"], {"id_to_delete": id_val})
                trans.commit()
            except Exception:
                trans.rollback()
                raise

    def create(self, name):
        with self._get_connection() as conn:
            trans = conn.begin()
            try:
                result = conn.execute(self.__scripts["insert_new"], {"new_name": name})
                # scalar() возвращает первое значение первой строки (наш новый ID)
                new_id = result.scalar()
                trans.commit()
                return new_id
            except Exception:
                trans.rollback()
                raise

    def get_max_id(self):
        with self._get_connection() as conn:
            result = conn.execute(self.__scripts["get_max_id"])
            return result.scalar()

    def get_company_by_id(self, id_val):
        with self._get_connection() as conn:
            result = conn.execute(self.__scripts["select_by_id"], {"select_id": id_val})
            return result.mappings().all()