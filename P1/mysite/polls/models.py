from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default = 0)
	def __str__(self):
		return self.choice_text

class WorkModel(models.Model):
	id_val = models.AutoField(primary_key = True)
	timestamp = models.DateTimeField(auto_now_add=True)
	label = models.CharField(max_length=250)
	def __str__(self):
		return self.label


#CREATE TABLE `metrics` (
#  `id` int(11) NOT NULL AUTO_INCREMENT,
#  `extension` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
#  `timestamp` datetime NOT NULL,
#  `type` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
#  `label` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
#  `action` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
#  `value` int(11) DEFAULT NULL,
#  `location` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
#  `extra` json DEFAULT NULL,
#  `ip_address` int(4) unsigned DEFAULT NULL,
#  PRIMARY KEY (`id`,`extension`),
#  KEY `extension_date_index` (`extension`(16),`timestamp`)
#) ENGINE=InnoDB AUTO_INCREMENT=58853103 DEFAULT CHARSET=latin1
#/*!50100 PARTITION BY KEY (extension) */ |