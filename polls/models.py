import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# 创建 Question 模型
class Question(models.Model):
	def __str__(self):
		return self.question_text
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# 创建 Choice 模型
class Choice(models.Model):
	def __str__(self):
		return self.choice_text
	# 每个Choice都与唯一的一个Question相关联
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	# 可选择的区域
	choice_text = models.CharField(max_length=200)
	# 投票计数区域
	votes = models.IntegerField(default=0)
