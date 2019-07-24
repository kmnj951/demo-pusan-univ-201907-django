from django.urls import path

from pokemon.views import index, pokemon_new, pokemon_edit, pokemon_list_html

urlpatterns = [
    path('', index),
    path('pokemon_list.html', pokemon_list_html),
    path('new/', pokemon_new),  # django는 post 구분(new/post/) 안함
    path('<int:pk>/', pokemon_edit),    # pk도 넣어서 호출
    # re_path(r'(?P<pk>\d+)', pokemon_edit),
]