from django.urls import path
from .views import home, all_students

urlpatterns = [
    path('', home, name='home'),
    path('all/', all_students, name='all_students'),
]