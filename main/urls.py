from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('product/<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('blog/', views.BlogPostListView.as_view(), name='post_list'),
    path('blog/create/', views.BlogPostCreateView.as_view(), name='post_create'),
    path('blog/update/<slug:slug>/', views.BlogPostUpdateView.as_view(), name='post_update'),
    path('blog/delete/<slug:slug>/', views.BlogPostDeleteView.as_view(), name='post_delete'),
]
