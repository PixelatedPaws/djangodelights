from django.shortcuts import render

from .models import Ingredient, MenuItem, RecipeRequirements, PurchaseLog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class IngredientListView(ListView):
    model = Ingredient
    template_name = 'inventory/ingredient_list.html'
    context_object_name = 'ingredients'
    ordering = ['name']
    
class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = 'inventory/ingredient_form.html'
    fields = ['name', 'price_per_unit', 'quantity_in_stock'] 
    
class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_confirm_delete.html'
    success_url = '/inventory/ingredients/'
    
class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = 'inventory/ingredient_form.html'
    fields = ['name', 'price_per_unit', 'quantity_in_stock']

class PurchaseLogListView(ListView):
    model = PurchaseLog
    template_name = 'inventory/purchase_logs.html'
    context_object_name = 'purchase_logs'
    ordering = ['-time_purchased']
    
class PurchaseLogCreateView(CreateView):
    model = PurchaseLog
    template_name = 'inventory/purchase.html'
    fields = ['menu_item', 'quantity_purchased']

class PurchaseLogUpdateView(UpdateView):
    model = PurchaseLog
    template_name = 'inventory/purchase_logs.html'
    fields = ['menu_item', 'quantity_purchased']
    
class PurchaseLogDeleteView(DeleteView):
    model = PurchaseLog
    template_name = 'inventory/purchase_confirm_delete.html'
    success_url = '/inventory/purchase_logs/'

class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'inventory/menu.html'
    context_object_name = 'menu_items'
    
class MenuItemCreateView(CreateView):
    model = MenuItem
    template_name = 'inventory/menu_add.html'
    fields = ['name', 'price']
    
class MenuItemUpdateView(UpdateView):
    model = MenuItem
    template_name = 'inventory/menu_add.html'
    fields = ['name', 'price']
    
class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = 'inventory/menu_confirm_delete.html'
    success_url = '/inventory/menu/'
    
class RecipeRequirementsListView(ListView):
    model = RecipeRequirements
    template_name = 'inventory/menu_details.html'
    context_object_name = 'recipe_requirements'
    
class RecipeRequirementsCreateView(CreateView):
    model = RecipeRequirements
    template_name = 'inventory/menu_details.html'
    fields = ['menu_item', 'ingredient', 'quantity_required']
    
class RecipeRequirementsUpdateView(UpdateView):
    model = RecipeRequirements
    template_name = 'inventory/menu_details.html'
    fields = ['menu_item', 'ingredient', 'quantity_required']
    
class RecipeRequirementsDeleteView(DeleteView):
    model = RecipeRequirements
    template_name = 'inventory/menu_details_confirm_delete.html'
    success_url = '/inventory/menu_details/'