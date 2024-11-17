from django.urls import path
from . import views

from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='inventory/login.html'), name='login'),
    path('logout_confirmation/', views.LogoutConfirmationView.as_view(), name='logout_confirmation'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('menu/', views.MenuItemListView.as_view(), name='menu'),
    path('ingredient_list/', views.IngredientListView.as_view(), name='ingredient_list'),
    path('ingredient_create/', views.IngredientCreateView.as_view(), name='ingredient_create'),
    path('ingredient_edit/', views.IngredientUpdateView.as_view(), name='ingredient_update'),
    path('ingredient_delete/', views.IngredientDeleteView.as_view(), name='ingredient_delete'),
    path('purchase_logs/', views.PurchaseLogListView.as_view(), name='purchase_logs'),
]