from django.db import models
from authapp.models import TaskUser


class Utask(models.Model):
    title = models.CharField(max_length=100, verbose_name='Task')
    date_create = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date_create')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Date_update')
    achievement = models.BooleanField(default=False, blank=True, verbose_name='achevement')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, default='Home', verbose_name='Category')
    author = models.ForeignKey(TaskUser, related_name="tasks", on_delete=models.CASCADE, verbose_name='User')

    def __str__(self) -> str:
        return self.title[:5]

    class Meta:
        verbose_name_plural = 'Tasks'
        verbose_name = 'Task'
        ordering = ['-date_create']


class Category(models.Model):
    category_name = models.CharField(max_length=30, db_index=True, verbose_name='Category', default='Home')
    
    def __str__(self) -> str:
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        ordering = ['category_name']


