from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField
    
    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
class RecipieRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    
    def __str__(self):
        ingredient_list = [ingredient.name for ingredient in self.ingredients.all()]
        return f"{self.menu_item.name} requires: {', '.join(ingredient_list)}"
    
class PurchaseLog(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity_purchased = models.PositiveIntegerField
    time_purchased = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.quantity_purchased} units of {self.menu_item.name} purchased at {self.time_purchased}"
    
