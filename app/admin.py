from sqladmin import ModelView
from app.schemas import *


class CollegeAdmin(ModelView, model=College):
    async_engine = True
    column_details_list = [College.id, College.name, College.updated_at, College.created_at]


app_views = [CollegeAdmin]
