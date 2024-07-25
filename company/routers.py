# myapp/routers.py
class CompanyDatabaseRouter:
    def db_for_read(self, model, **hints):
        company_name = hints.get('company_name')
        if company_name:
            return company_name
        return 'default'

    def db_for_write(self, model, **hints):
        company_name = hints.get('company_name')
        if company_name:
            return company_name
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'default'
