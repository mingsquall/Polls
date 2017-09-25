# 告诉admin站点Question要有admin系统
from django.contrib import admin
from .models import Question
admin.site.register(Question)
