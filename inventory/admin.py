from django.contrib import admin
from .models import Ingredient, MenuItem, RecipieRequirements, PurchaseLog

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_unit', 'quantity_in_stock')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    
@admin.register(RecipieRequirements)
class RecipieRequirementsAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'ingredients')
    
@admin.register(PurchaseLog)
class PurchaseLogAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'quantity_purchased', 'time_purchased')