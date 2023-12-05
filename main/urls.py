# urls.py
from django.urls import path
from . import views
from .views import BlogPostCreateView, BlogPostDetailView, BlogPostListView

# Определение маршрутов для приложения 'main'
app_name = 'main'

# Список маршрутов
urlpatterns = [
    # Главная страница
    path('', views.IndexView.as_view(), name='index'),

    # Домашняя страница
    path('home/', views.HomeView.as_view(), name='home'),

    # Страница контактов
    path('contacts/', views.ContactsView.as_view(), name='contacts'),

    # Страница детального представления продукта
    # product_id передается в качестве аргумента
    path('product/<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),

    path('blog/create/', BlogPostCreateView.as_view(), name='post_create'),
    path('blog/<slug:slug>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('blog/', views.BlogPostListView.as_view(), name='post_list'),
    path('blog/', BlogPostListView.as_view(), name='blogpost_list'),

]
