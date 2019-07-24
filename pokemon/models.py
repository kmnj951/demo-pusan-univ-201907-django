from django.core.validators import MinLengthValidator
from django.db import models

# field 정의


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])     # 유효성 검사
    photo = models.ImageField(blank=True)   # blank : image가 없어도 됨
    page_url = models.URLField()
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name
