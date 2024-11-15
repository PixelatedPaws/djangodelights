from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    def get_recipe_requirements(self):
        requirements = RecipeRequirements.objects.filter(menu_item=self)
        ingredients_list = [f"{req.quantity_required} of {req.ingredient.name}" for req in requirements]
        return f"Ingredients for {self.name}: {', '.join(ingredients_list)}"
    
class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, default="", on_delete=models.CASCADE)
    quantity_required = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.quantity_required} of {self.ingredient.name} for {self.menu_item.name}"
    
class PurchaseLog(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity_purchased = models.PositiveIntegerField(default=0)
    time_purchased = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.quantity_purchased} units of {self.menu_item.name} purchased at {self.time_purchased}"
    
