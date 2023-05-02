<h1 align="center">FoodRecipe-Flask</h1>
<h3 align="center">A Food Recipe App with Flask, Python</h3> 

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- AboutProject -->
<h2> :pencil: About Project</h2>

<h4> Why FoodRecipe App ? </h4>
<p align="justify"> 
A web application created for this project makes use of the Flask web framework.
Users can see, like, and propose recipes using this platform for recipe sharing
depending on their preferences. The program manages a SQLite database that has user information,
recipe information, and ingredient information using SQLAlchemy. In order to manage user login and authorisation,
it additionally supports Flask-Login.
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<p align="justify" > 

A number of routes in the application handle requests for various pages.
All of the recipes and ingredients in the database are listed when using the "/" route.
All of the recipes in the database are listed on the "/recipes" route. The "/recipes/int:id" route shows information
on a particular recipe, such as the name, picture, ingredients, and directions. A list of all the recipes that the
user has loved is displayed on the "/liked_recipes" route. A list of recipes that share at least two ingredients with
the user's favorite dishes is shown using the "/recommended_recipes" route. Users can like dishes using the "/recipes/int:recipe_id/like" route,
and they can unlike recipes using the "/recipes/int:recipe_id/unlike" way.

</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)



<p align="justify" > 

The classes for Ingredient, Recipe, User, and Like make up the application's models.
A secondary table called recipe_ingredient serves as the many-to-many connection between the Ingredient and Recipe classes.
Through a second table called user_saved_recipe, the User and Recipe classes are linked many-to-many.
A timestamp attribute on the Like class, which links the User and Recipe classes in a one-to-many relationship,
keeps track of when the user liked the recipe.


for run the Website,

---> pip install -r requirements.txt
---> cd FoodRecipe
---> python3 DbContext.py
---> python3 app.py



</p>
