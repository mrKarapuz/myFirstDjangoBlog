from django.urls import path
from .views import * 

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('new/<int:new_id>/', get_new, name='get_new'),
]
