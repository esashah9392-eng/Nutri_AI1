import random
from typing import Dict

class MealGenerator:
    def __init__(self):
        self.recipes = {}
        self.foods = {}

    def generate_meal_plan(self, calories: int, macros: Dict, goal: str):
        meal_types = ["breakfast", "lunch", "dinner", "snack"]
        
        meal_plan = {}

        for meal in meal_types:
            meal_plan[meal] = self._generate_single_meal(
                calories,
                macros,
                goal,
                meal
            )
        
        return meal_plan

    def _generate_single_meal(self, calories: int, macros: Dict, goal: str, meal_type: str) -> Dict:
        """Generate a single meal with recipe - SAFE VERSION"""

        result = {
            'name': f"{meal_type.title()} Meal",
            'nutrition': {'calories': calories//4, 'protein': 25, 'carbs': 40, 'fat': 15},
            'recipe': False
        }
        
        try:
            if meal_type in self.recipes and self.recipes[meal_type]:
                recipe = random.choice(self.recipes[meal_type])
                recipe_nut = recipe['nutrition']
                
                scale = min(1.5, (calories//4) / recipe_nut['calories'])
                result.update({
                    'name': recipe['name'],
                    'recipe': True,
                    'ingredients': recipe['ingredients'],
                    'instructions': recipe['instructions'],
                    'nutrition': {k: v * scale for k, v in recipe_nut.items()}
                })
                return result
            
            foods = []
            total = {'calories': 0, 'protein': 0, 'carbs': 0, 'fat': 0}
            
            # 🔥 Prevent crash if foods empty
            if not self.foods:
                return result

            food_items = list(self.foods.keys())
            for _ in range(3):
                category = random.choice(food_items)
                food_name = random.choice(list(self.foods[category].keys()))
                food_data = self.foods[category][food_name]
                
                portion = min(1.5, (calories//4) / 300)
                scaled = {k: v * portion for k, v in food_data.items()}
                
                foods.append({
                    'name': food_name.replace('_', ' ').title(),
                    'portion': f"{portion*100:.0f}g",
                    **scaled
                })
                
                for key in total:
                    total[key] += scaled[key]
            
            result.update({'foods': foods, 'nutrition': total})
        
        except Exception:
            result['nutrition'] = {'calories': calories//4, 'protein': 25, 'carbs': 40, 'fat': 15}
        
        return result