from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeRequirements, PurchaseLog

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_unit', 'quantity_in_stock')

class RecipeRequirementsInline(admin.TabularInline):
    model = RecipeRequirements
    extra = 1  # Number of empty forms to show
    fields = ('ingredient', 'quantity_required')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    inlines = [RecipeRequirementsInline]
    
@admin.register(RecipeRequirements)
class RecipeRequirementsAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'ingredient', 'quantity_required')
    list_filter = ('menu_item',)  # Add a filter to easily group by Menu Item
    
@admin.register(PurchaseLog)
class PurchaseLogAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'quantity_purchased', 'time_purchased')