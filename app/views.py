from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    items_per_page = request.GET.get('items_per_page') or 5
    try:
        items_per_page = int(items_per_page)
    except ValueError:
        items_per_page = 5
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj, 'items_per_page': items_per_page})
