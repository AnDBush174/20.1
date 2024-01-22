# main/urls.py
from django.urls import path
from . import views
from .views import BlogPostCreateView, BlogPostDetailView, BlogPostListView, CreateProductView, UpdateProductView, \
    DeleteProductView, ContactView, product_detail
from user_app.views import DashboardView, UserLoginView, RegisterView

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
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    # product_id передается в качестве аргумента
    path('product/<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),

    path('blog/create/', BlogPostCreateView.as_view(), name='post_create'),
    path('blog/<slug:slug>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('blog/', views.BlogPostListView.as_view(), name='post_list'),
    path('blog/', BlogPostListView.as_view(), name='blogpost_list'),
    path('create/', CreateProductView.as_view(), name='create_product'),
    path('list/', views.product_list, name='product_list'),
    path('update/<int:pk>/', UpdateProductView.as_view(), name='update_product'),
    path('delete/<int:pk>/', DeleteProductView.as_view(), name='delete_product'),
path('product/<int:product_id>/', product_detail, name='product_detail'),
]
