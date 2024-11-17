from .models import Ingredient, MenuItem, RecipeRequirements, PurchaseLog
from django.views.generic import ListView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import CreateView

from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class IngredientListView(ListView):
    model = Ingredient
    template_name = 'inventory/ingredient_list.html'
    context_object_name = 'ingredients'
    ordering = ['name']
    
class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = 'inventory/ingredient_create.html'
    fields = ['name', 'price_per_unit', 'quantity_in_stock'] 
    success_url = reverse_lazy('ingredient_list')
    
class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete.html'
    success_url = reverse_lazy('ingredient_list')
    
class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = 'inventory/ingredient_form.html'
    fields = ['name', 'price_per_unit', 'quantity_in_stock']
    success_url = reverse_lazy('ingredient_list')

class PurchaseLogListView(LoginRequiredMixin, ListView):
    model = PurchaseLog
    template_name = 'inventory/purchase_logs.html'
    context_object_name = 'purchase_logs'
    ordering = ['-time_purchased']
    
class PurchaseLogCreateView(LoginRequiredMixin, CreateView):
    model = PurchaseLog
    template_name = 'inventory/purchase.html'
    fields = ['menu_item', 'quantity_purchased']

class PurchaseLogUpdateView(LoginRequiredMixin, UpdateView):
    model = PurchaseLog
    template_name = 'inventory/purchase_logs.html'
    fields = ['menu_item', 'quantity_purchased']
    
class PurchaseLogDeleteView(LoginRequiredMixin, DeleteView):
    model = PurchaseLog
    template_name = 'inventory/purchase_confirm_delete.html'
    success_url = 'inventory/purchase_logs.html'

class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'inventory/menu.html'
    context_object_name = 'menu_items'
    
class MenuItemCreateView(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = 'inventory/menu_add.html'
    fields = ['name', 'price']
    
class MenuItemUpdateView(LoginRequiredMixin, UpdateView):
    model = MenuItem
    template_name = 'inventory/menu_add.html'
    fields = ['name', 'price']
    
class MenuItemDeleteView(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = 'inventory/menu_confirm_delete.html'
    success_url = 'inventory/menu_add.html'
    
class RecipeRequirementsListView(ListView):
    model = RecipeRequirements
    template_name = 'inventory/menu_details.html'
    context_object_name = 'recipe_requirements'
    
class RecipeRequirementsCreateView(LoginRequiredMixin, CreateView):
    model = RecipeRequirements
    template_name = 'inventory/menu_details.html'
    fields = ['menu_item', 'ingredient', 'quantity_required']
    
class RecipeRequirementsUpdateView(LoginRequiredMixin, UpdateView):
    model = RecipeRequirements
    template_name = 'inventory/menu_details.html'
    fields = ['menu_item', 'ingredient', 'quantity_required']
    
class RecipeRequirementsDeleteView(LoginRequiredMixin, DeleteView):
    model = RecipeRequirements
    template_name = 'inventory/menu_details_confirm_delete.html'
    success_url = 'menu_details.html'
    
class UserCreateView(CreateView):
    model = User
    template_name = 'inventory/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    
class HomeView(TemplateView):
    template_name = 'inventory/home.html'

class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'inventory/logout.html'
    
class LogoutConfirmationView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/logout_confirmation.html'