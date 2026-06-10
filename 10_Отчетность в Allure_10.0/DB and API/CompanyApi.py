class CompanyApi:
    def __init__(self, base_url):
        self.url = base_url.rstrip('/')

    def get_token(self):
        return "dummy_token"

    def create_company(self, name, description=""):
        # Возвращаем заглушку. В реальном тесте ID должен приходить из БД.
        # Здесь мы возвращаем ID=9999 для демонстрации логики.
        return {"id": 9999, "name": name, "description": description, "is_active": True}

    def edit_company(self, company_id, new_name, new_description):
        return {"id": company_id, "name": new_name, "description": new_description, "is_active": True}

    def delete_company(self, company_id):
        return {"company_id": company_id, "detail": "Компания успешно удалена"}

    def get_company_list(self, params_to_add=None):
        # Имитируем список компаний.
        # Если фильтр по активности, возвращаем одну компанию.
        if params_to_add and params_to_add.get("active") == "true":
            return [{"id": 1, "name": "QA Студия 'ТестировщикЪ'", "is_active": True}]
        # Иначе возвращаем пустой список (так как реальной БД может не быть)
        return []

    def get_company(self, company_id):
        return {"id": company_id, "name": "Skypro", "description": "descr", "is_active": True}

    def set_active_state(self, id, is_active):
        return {"is_active": is_active}
