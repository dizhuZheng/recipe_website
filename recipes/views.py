from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView

# Create your views here.
logo = 'Welcome to Yummy Recipe'
sentence = 'picture uploaded !'

def index(request):
    """The home page for recipes"""
    return render(request, 'recipes/home.html', {'logo': logo})

def categories(request):
    """show all categories"""
    categories = Category.objects.all()
    paginator = Paginator(categories, 6)

    if request.method == "GET":
        page = request.GET.get('page')
        try:
            cats = paginator.page(page)
        except PageNotAnInteger:
            cats = paginator.page(1)
        except InvalidPage:
            return HttpResponse('Can\'t find page')
        except EmptyPage:
            cats = paginator.page(paginator.num_pages)
    return render(request, 'recipes/categories.html', {'cats': cats})

def sub_category(request, id):
    return render(request, 'recipes/breakfast.html')

@login_required(login_url='/accounts/login/')
def dish(request, dish_id):
    """show a single topic"""
    dish = Recipe.objects.get(id=dish_id)
    content = {'dish':dish}
    if request.method == 'POST':
        new_img = IMG(
            img = request.FILES.get('img'),
            name = request.FILES.get('img').name
        )
        new_img.save()
        content['sentence']= sentence
    return render(request, 'recipes/dish.html', content)


@login_required
def new_dish(request):
    """add a new dish"""
    if request.method != 'POST':
        form = RecipeForm()

    else:
        form = RecipeForm(request.POST)
        if form.is_valid():
            new_dish = form.save(commit=False)
            new_dish.owner = request.user
            new_dish.save()
            return redirect(reverse('recipes:dishes'))

    context = {'form': form}
    return render(request, 'recipes/new_dish.html', context)


@login_required
def edit(request, entry_id):
    entry = get_object_or_404(Entry, pk = entry_id)
    if request.method =='POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            entry = form.save()
            messages.success(request, 'Entry was successfully edited!')
            return redirect(reverse('recipes:categories'))   #????
    else:
        form = RecipeForm()
        return render(request, 'recipes/.html', context, {'form': form})
