from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Pokemon

# 관리자 창
admin.site.register(Category)


class PokemonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'page_tag']

    def page_tag(self, pokemon):
        tag = '<a href="{}" target="_blank">링크</a>'.format(pokemon.page_url)
        return mark_safe(tag)   # 안전한 tag구나~~ <를 lt로 안바꿈


admin.site.register(Pokemon, PokemonAdmin)      # CRUD interface
