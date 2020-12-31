from django.db import models


# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)

    def __unicode__(self):
        return u'Student:%s' % self.username

    # 修改后台显示object
    def __str__(self):
        return u'Student:%s' % self.username


class Movie(models.Model):
    mname = models.CharField(max_length=255)
    mdesc = models.CharField(max_length=255)
    mimg = models.CharField(max_length=255)

    # 修改后台显示object
    def __str__(self):
        return u'Movie:%s' % self.mname
