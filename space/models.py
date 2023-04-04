from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Spaces(models.Model):

    title       = models.CharField(max_length=200, verbose_name="공간명")
    address     = models.CharField(max_length=250, verbose_name="주소", null=True)
    instagram   = models.CharField(max_length=200, verbose_name="인스타아이디", null=True)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    summary     = models.TextField(verbose_name="소개", null=True)
    upload_sns  = models.BooleanField(verbose_name="인스타업로드", default=False)
    upload_app  = models.BooleanField(verbose_name="앱업로드", default=False)
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at  = models.DateTimeField(auto_now=True, verbose_name="최종수정일")

    def __str__(self):
        return self.title