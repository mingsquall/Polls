# 告诉admin站点Question要有admin系统
from django.contrib import admin
from .models import Question, Choice

class ChoiceInlins(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	# fields = ['pub_date', 'question_text']
	fieldsets = [
		(None, 				 {'fields':['question_text']}),
		('Data information', {'fields':['pub_date'], 'classes':['collapse']}),
	]
	inlines = [ChoiceInlins]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	# 由于'pub_date'是DataTimeField，Django可以根据Any date/Today/Past 7 days/This month/This year来筛选
	list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
