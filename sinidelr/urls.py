from django.urls import path
from . import views


# urlpatterns = [
#     path('', views.index, name='index'),
# ]

app_name= 'sinidelr'
urlpatterns=[path('personas',
                  views.PersonaList.as_view(),
                  name='personas'),
             path('persona/<int:pk>',
                  views.PersonaDetail.as_view(),
                  name='PersonaDetail'),
             path('',
                   views.index,
                   name='index'),

             ]