from django.db import models

# Create your models here.
class Spaces(models.Model):

    title       = models.CharField(max_length=200, verbose_name="공간명")
    summary     = models.TextField(verbose_name="소개", null=True)
    address     = models.TextField(verbose_name="주소", null=True)
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at  = models.DateTimeField(auto_now=True, verbose_name="최종수정일")

    def __str__(self):
        return self.title