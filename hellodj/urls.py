"""hellodj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include


def root(request):
    # html = open("index.html", "rt", encoding="utf8").read()
    # return HttpResponse(html)
    # alt + enter - import
    return render(request, 'root.html')  # request에 요청(user)에 관한 정보 다 저장


urlpatterns = [
    # ( 이 주소로 들어오면, 이 함수를 호출 )
    path('admin/', admin.site.urls),
    path('pokemon/', include('pokemon.urls')),  # pokemon\urls.py
    path('', root),  # 함수 넘김 ( 1급 함수를 지원하는 언어 )
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
