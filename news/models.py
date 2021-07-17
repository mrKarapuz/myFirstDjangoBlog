from django.db import models
from django.urls import reverse

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контенкт')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) 
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey("Category", verbose_name=("Категория"), on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("get_new", kwargs={"new_id": self.pk})
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-id']

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"category_id": self.pk})
    

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']