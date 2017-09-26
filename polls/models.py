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
		now = timezone.now()
		# 于近期出版 并且 出版时间在1天之前的全部返回False
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	# Admin中的was_published_recently一列默认是显示T/F; 我们在这里修改标题，并改成图片样式表示T/F
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

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
