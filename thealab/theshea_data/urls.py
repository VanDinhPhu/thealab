from django.urls import path, re_path, include

from . import views

app_name = 'theshea_data'

urlpatterns = [
  path('return_json_update_database/<func>/', views.return_json_update_database, name='return_json_update_database'),
  ##########################################################################################
  path('json-api/<data_for>/', views.json_api_data, name='json-api-data'),
  path('', views.index, name='index'),]