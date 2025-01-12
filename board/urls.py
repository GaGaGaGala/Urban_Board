from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('advertisement/<int:pk>/', views.advertisement_detail, name='advertisement_detail'),
    path('add/', views.add_advertisement, name='add_advertisement'),
    path('signup/', views.signup, name='signup'),
    path('edit/<int:pk>/', views.edit_advertisement, name='edit_advertisement'),
    path('delete/<int:pk>/', views.delete_advertisement, name='delete_advertisement'),
    path('likes/<int:pk>/', views.post_like, name='post_like'),
    path('dislikes/<int:pk>/', views.post_dislike, name='post_dislike'),
    path('advertisement_author_list/', views.advertisement_author_list, name='advertisement_author_list'),
    path('search_author_list/', views.search_author_list, name='search_author_list'),
    path('profile/', views.update_profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
