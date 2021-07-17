from django.shortcuts import render, get_object_or_404 

from .models import News, Category

def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news, 
        'title':'Список новостей',
    }
    return render(request, template_name='news/index.html', context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id) 
    category = Category.objects.get(pk=category_id)
    return render(request, template_name='news/category.html', context={'news': news, 'category': category})

def get_new(request, new_id):
    # new = News.objects.get(id=new_iter)
    new = get_object_or_404(News, id=new_id)
    return render(request, template_name='news/new.html', context={'new': new})
    
