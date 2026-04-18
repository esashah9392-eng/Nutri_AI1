import pandas as pd
import numpy as np
import json
from sklearn.linear_model import LinearRegression

class NutritionCalculator:
    def __init__(self):
        self.bmr_model = self._create_bmr_model()
    
    def _create_bmr_model(self):
        # Harris-Benedict Equation coefficients
        model = LinearRegression()
        return model
    
    def calculate_bmr(self, age, weight, height, gender):
        """Calculate Basal Metabolic Rate"""
        if gender.lower() == 'male':
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        return bmr
    
    def calculate_tdee(self, bmr, activity_level):
        """Calculate Total Daily Energy Expenditure"""
        multipliers = {
            'sedentary': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'active': 1.725,
            'very_active': 1.9
        }
        return bmr * multipliers.get(activity_level, 1.55)
    
    def get_calorie_target(self, tdee, goal):
        """Get calorie target based on goal"""
        if goal == 'weight_loss':
            return tdee - 500
        elif goal == 'weight_gain':
            return tdee + 500
        elif goal == 'muscle_gain':
            return tdee + 300
        else:
            return tdee
    
    def get_macros(self, calories, goal):
        """Get macro breakdown"""
        if goal == 'weight_loss':
            return {
                'protein': calories * 0.30 / 4,
                'carbs': calories * 0.45 / 4,
                'fat': calories * 0.25 / 9
            }
        else:
            return {
                'protein': calories * 0.35 / 4,
                'carbs': calories * 0.40 / 4,
                'fat': calories * 0.25 / 9
            }