from django.urls import path
from . import views


# urlpatterns = [
#     path('', views.index, name='index'),
# ]

app_name= 'sinidelr'
urlpatterns=[path('',
                  views.PersonaList.as_view(),
                  name='personas'),

             path('test',
                   views.index,
                   name='index'),
             ]