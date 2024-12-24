from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from .models import Advertisement, User
from .forms import AdvertisementForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def base(request):
    """Представление для базового шаблона."""
    return render(request, 'base.html')


def home(request):
    """Представление для шаблона главной страницы."""
    return render(request, 'home.html')


def signup(request):
    """Представление для регистрации."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/board')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    """Выход из системы."""
    logout(request)
    return redirect('home')


@login_required
def add_advertisement(request):
    """Для добавления объявления."""
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            img_obj = form.instance
            return redirect('board:advertisement_detail', pk=img_obj.pk)
    else:
        form = AdvertisementForm()
    return render(request, 'board/add_advertisement.html', {'form': form})


def advertisement_detail(request, pk):
    """Представление для страницы конкретного объявления."""
    advertisement = Advertisement.objects.get(pk=pk)
    context = {
        'advertisement': advertisement,
    }
    likes_connected = get_object_or_404(Advertisement, id=pk)
    dislikes = False
    if likes_connected.likes.filter(id=request.user.id).exists():
        dislikes = True
    context['number_of_likes'] = likes_connected.number_of_likes(),
    context['post_is_dislikes'] = dislikes
    return render(request, 'board/advertisement_detail.html', context=context)


def advertisement_list(request):
    """Все объявления."""
    advertisements = Advertisement.objects.all()
    count_likes = Advertisement.objects.filter(likes__id=request.user.id).count() + 1
    count_dislikes = Advertisement.objects.filter(dislikes__id=request.user.id).count() + 1
    context = {
        'advertisements': advertisements,
        'count_likes': count_likes,
        'count_dislikes': count_dislikes
    }
    print('count_likes', count_likes)
    print('count_dislikes', count_dislikes)
    return render(request, 'board/advertisement_list.html', context=context )


@login_required
def edit_advertisement(request, pk):
    """Представление  для редактирования объявлений, которое загружает форму существующего объявления и сохраняет изменения.
    """
    advertisement = Advertisement.objects.get(pk=pk)
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES, instance=advertisement)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            img_obj = form.instance
            return redirect('board:advertisement_detail', pk=img_obj.pk)
    else:
        form = AdvertisementForm(instance=advertisement)
    return render(request, 'board/edit_advertisement.html', {'form': form, 'advertisement': advertisement})


@login_required
def delete_advertisement(request, pk):
    """Представление для удаления объявления."""
    advertisement = Advertisement.objects.get(pk=pk)
    if request.method == "POST":
        advertisement.delete()
        return redirect('board:advertisement_list')
    return render(request, 'board/delete_advertisement.html', {'advertisement': advertisement})


@login_required
def post_like(request, pk):
    """Возможность пользователя ставить лайк."""
    post = get_object_or_404(Advertisement, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('board:advertisement_detail', args=[str(pk)]))


@login_required
def post_dislike(request, pk):
    """А так же дизлайк."""
    post = get_object_or_404(Advertisement, pk=pk)
    if post.dislikes.filter(id=request.user.id).exists():
        post.dislikes.remove(request.user)
    else:
        post.dislikes.add(request.user)

    return HttpResponseRedirect(reverse('board:advertisement_detail', args=[str(pk)]))


def advertisement_author_list(request):
    """Поиск объявлений по автору"""
    search_author = User.objects.get(author=request.user.id)
    search_advertisements = Advertisement.objects.filter(author=search_author)
    count_likes = Advertisement.objects.filter(likes__id=request.user.id).count() + 1
    count_dislikes = Advertisement.objects.filter(dislikes__id=request.user.id).count() + 1
    context = {
        'author': search_author,
        'advertisements':  search_advertisements,
        'count_likes': count_likes,
        'count_dislikes': count_dislikes
    }
    print('count_likes', count_likes)
    print('count_dislikes', count_dislikes)
    return render(request, 'board/advertisement_author_list.html', context=context)
