from django.http import HttpResponse
from django.shortcuts import render

from pokemon.models import Pokemon

# urlpatterns에 추가해야 호출됨
# 앱 폴더 내에 urls.py 만들어서 urlpattens에 추가 - 재사용성 (추가하기 편리)
# 생성된 파일 최상위 urls.py 와 연결


def index(request):
    qs = Pokemon.objects.all()  # QuerySet Type (가져올 예정)
    # return render(request, 'root.html')
    return render(request, 'pokemon/pokemon_list.html', {
        'pokemon_list': qs,
    })

# def pokemon_list_html(request):
#     qs = Pokemon.objects.all()  # QuerySet 타입
#     return render(request, 'pokemon/pokemon_list_html.html', {
#         'pokemon_list': qs,
#     })


def pokemon_new(request):
    return HttpResponse("새 포켓몬 등록 Form")


def pokemon_edit(request, pk):
    # pk : Primary Key
    message = "기존 포켓몬 #{} 수정 Form".format(pk)
    return HttpResponse(message)
