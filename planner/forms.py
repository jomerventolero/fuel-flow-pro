from django.forms import ModelForm
from .models import Recipe

# Fuel Flow Pro Form
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['day_of_the_week', 'meal_type', 'recipe_name', 'recipe_description']