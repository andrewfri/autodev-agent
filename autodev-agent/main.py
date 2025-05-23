"""
FastAPI app to track meals and calories.

Endpoints:
- POST /meals: Submit a meal (name, calories, timestamp)
- GET /meals: List all meals

Data is stored in memory.
"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(title="Meal Tracker API")

class Meal(BaseModel):
    name: str
    calories: int
    timestamp: datetime

# In-memory storage for meals
meals_db: List[Meal] = []

@app.post("/meals", response_model=Meal)
def add_meal(meal: Meal):
    """
    Add a new meal to the tracker.
    Args:
        meal (Meal): Meal data including name, calories, and timestamp.
    Returns:
        The added meal.
    """
    meals_db.append(meal)
    return meal

@app.get("/meals", response_model=List[Meal])
def list_meals():
    """
    List all submitted meals.
    Returns:
        List of all meals in the tracker.
    """
    return meals_db
