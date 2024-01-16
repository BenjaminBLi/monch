from pydantic import BaseModel
from typing import List
from fastapi import FastAPI

app = FastAPI()
class Ingredient(BaseModel):
   name: str
   quantity: float
   unit: str

class Step(BaseModel):
   description: str
   time: int # in minutes

class Component(BaseModel):
   name: str
   ingredients: List[Ingredient]
   steps: List[Step]

class Recipe(BaseModel):
   id: int
   title: str
   components: List[Component]


recipes = []

@app.post("/recipes/")
async def create_recipe(recipe: Recipe):
   recipes.append(recipe)
   return recipe

@app.get("/recipes/{id}", response_model=Recipe)
async def read_recipe(id: int):
   for recipe in recipes:
       if recipe.id == id:
           return recipe
   raise HTTPException(status_code=404, detail="Recipe not found")

@app.put("/recipes/{id}")
async def update_recipe(id: int, recipe: Recipe):
   for index, r in enumerate(recipes):
       if r.id == id:
           recipes[index] = recipe
           return recipe
   raise HTTPException(status_code=404, detail="Recipe not found")

@app.delete("/recipes/{id}")
async def delete_recipe(id: int):
   global recipes
   recipes = [r for r in recipes if r.id != id]
   return {"detail": "Recipe deleted"}

