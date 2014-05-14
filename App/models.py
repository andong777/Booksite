# coding=utf-8
from django.contrib.auth.models import User
from django.db import models
from BookSite import settings

# 一些常量
man_name_len = 50
press_name_len = 100
category_name_len = 50
book_name_len = 200

# 作者类
# 属性：id，姓名，简介，头像
class Writer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=man_name_len,verbose_name="姓名")
    intro = models.TextField(null=True,blank=True,verbose_name="简介")
    class Meta:
        db_table = "Writer"
    def __unicode__(self):
        return self.name

# 出版社类
# 属性：id，出版社名，简介，网址
class Press(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=press_name_len,verbose_name="出版社名")
    intro = models.TextField(verbose_name="简介",null=True,blank=True)
    site = models.URLField(null=True,blank=True,verbose_name="网址")
    class Meta:
        db_table = "Press"
    def __unicode__(self):
        return self.name

# 标签类
# 属性：标签名，书籍，介绍
class Tag(models.Model):
    name = models.CharField(max_length=category_name_len,primary_key=True,verbose_name="标签名")
    add_time = models.DateTimeField(verbose_name="添加时间")
    intro = models.TextField(verbose_name="介绍")
    class Meta:
        db_table = "Tag"
    def __unicode__(self):
        return self.name

# 书籍类
# 属性：13位isbn号，书名，作者，出版社，出版日期，简介，封面，分数，打分次数，添加时间
class Book(models.Model):
    isbn = models.CharField(max_length=13,primary_key=True,verbose_name="ISBN")
    name = models.CharField(max_length=book_name_len,verbose_name="书名")
    writer = models.ForeignKey(Writer,verbose_name="作者")
    press = models.ForeignKey(Press,verbose_name="出版社")
    date = models.DateTimeField(verbose_name="出版时间")
    intro = models.TextField(verbose_name="简介")
    cover = models.ImageField(upload_to='cover/',null=True,blank=True,verbose_name="封面")
    score = models.FloatField(null=True,blank=True,verbose_name="分数", default=0)
    vote = models.IntegerField(null=True,blank=True,default=0,verbose_name="打分次数")
    add_time = models.DateTimeField(verbose_name="添加时间")
    tag = models.ManyToManyField(Tag,verbose_name="标签")
    class Meta:
        db_table = "Book"
    def __unicode__(self):
        return self.name

# 评论类
# 属性：id，用户，书籍，评论内容，添加时间
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,verbose_name="用户")
    book = models.ForeignKey(Book,verbose_name="书籍")
    title = models.CharField(max_length=30,verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    add_time = models.DateTimeField(verbose_name="添加时间")
    class Meta:
        db_table = "Comment"
        unique_together = ("user","book")
    def __unicode__(self):
        return self.title
