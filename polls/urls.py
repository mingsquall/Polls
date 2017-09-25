from django.conf.urls import url
from . import views

# 增加命名空间, 避免模板中标签{% url %}无法区分为URL创建哪个应用的视图
app_name = 'polls'
urlpatterns = [
	# ex: /polls/
	url(r'^$', views.IndexView.as_view(), name='index'),
	# ex: /polls/5/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	# ex: /polls/5/results/
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	# ex: /polls/5/vote/
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
