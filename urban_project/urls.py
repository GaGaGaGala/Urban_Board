"""
URL configuration for urban_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from board import views as board_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls', namespace='board')),
    path('accounts/logout/', board_views.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', board_views.home, name='home'),
    path('board/signup', board_views.signup, name='signup'),
    path('board/add_advertisement', board_views.add_advertisement, name='add_advertisement'),
    path('board/advertisement_list', board_views.advertisement_list, name='advertisement_list'),
    path('board/advertisement_detail', board_views.advertisement_detail, name='advertisement_detail'),
    path('board/edit_advertisement', board_views.edit_advertisement, name='edit_advertisement'),
]