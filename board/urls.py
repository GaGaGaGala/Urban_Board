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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
