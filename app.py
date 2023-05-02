from flask import Flask, redirect, render_template, url_for, request, flash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SECRET_KEY'] = 'secret-key-goes-here'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


# define models for ingredients and recipes
class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(50), nullable=False)
    recipes = db.relationship('Recipe', secondary='recipe_ingredient')


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    ingredients = db.relationship('Ingredient', secondary='recipe_ingredient')
    image_url = db.Column(db.String(50), nullable=False)
    likes = db.relationship('Like', backref='recipe', lazy=True)


recipe_ingredient = db.Table('recipe_ingredient',
                             db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
                             db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id'))
                             )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    likes = db.relationship('Like', backref='user', lazy=True)


user_saved_recipe = db.Table('user_saved_recipe',
                             db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                             db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'))
                             )


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


# login manager setup
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# The '/' route handles the request to the homepage. It displays a list of all the recipes and ingredients in the database.
@app.route('/')
def index():
    date = datetime.now()
    recipes = Recipe.query.all()
    ingredients = Ingredient.query.all()
    return render_template('index.html', recipes=recipes, ingredients=ingredients)


# The '/recipes' route handles the request to the recipes page. It displays a list of all the recipes in the database.
@app.route('/recipes')
def recipes():
    recipes = Recipe.query.all()
    return render_template('recipes.html', recipes=recipes)


# The '/recipes/int:id' route handles the request to view the details of a specific recipe.
# It displays the name, image, ingredients, and instructions of the recipe.
@app.route('/recipes/<int:id>')
def recipe_detail(id):
    recipe = Recipe.query.get(id)
    recipe_ins = recipe.instructions.split("\n")
    ingredients = [i for i in recipe.ingredients]
    return render_template('recipe_detail.html', recipe=recipe, ingredients=ingredients, recipe_ins=recipe_ins)


# The '/liked_recipes' route handles the request to view the user's liked recipes. It displays a list of all the recipes that the user has liked.
@app.route('/liked_recipes')
@login_required
def liked_recipes():
    user = current_user
    liked_recipes = user.likes
    return render_template('liked_recipes.html', liked_recipes=liked_recipes)


# The '/recommended_recipes' route handles the request to view the recommended recipes based on
# the user's likes. It displays a list of all the recipes that have at least two ingredients in common with the user's liked recipes.
@app.route('/recommended_recipes')
@login_required
def recommended_recipes():
    liked_recipes = []
    for liked_recipe in current_user.likes:
        recipe = Recipe.query.get(liked_recipe.recipe_id)
        liked_recipes.append(recipe)

    liked_ingredients = []
    for recipe in liked_recipes:
        liked_ingredients.extend(recipe.ingredients)
    liked_ingredients = list(set(liked_ingredients))

    recommended_recipes = []
    for ingredient in liked_ingredients:
        recipes_with_ingredient = Recipe.query.filter(Recipe.ingredients.any(name=ingredient.name)).all()
        for recipe in recipes_with_ingredient:
            if recipe not in liked_recipes and recipe not in recommended_recipes:
                if len(set(recipe.ingredients).intersection(set(liked_ingredients))) >= 2:
                    recommended_recipes.append(recipe)
    return render_template('recommended_recipes.html', recommended_recipes=recommended_recipes)


# The '/recipes/int:recipe_id/like' route handles the request to like a recipe. It adds a new Like object to the database.
@app.route('/recipes/<int:recipe_id>/like', methods=['POST'])
@login_required
def like_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    liked_recipe = Like(user_id=current_user.id, recipe_id=recipe.id)
    db.session.add(liked_recipe)
    db.session.commit()
    flash('Recipe Liked!', 'success')
    return redirect(url_for('recipe_detail', id=recipe_id))


# The '/recipes/int:recipe_id/unlike' route handles the request to unlike a recipe. It deletes the Like object from the database.
@app.route('/recipes/<int:recipe_id>/unlike', methods=['POST'])
@login_required
def unlike_recipe(recipe_id):
    liked_recipe = Like.query.filter_by(user_id=current_user.id, id=recipe_id).first()
    db.session.delete(liked_recipe)
    db.session.commit()
    flash('Recipe Unliked!', 'success')
    return redirect(url_for('liked_recipes'))


# The '/ingredients' route handles the request to the ingredients page. It displays a list of all the ingredients in the database.
@app.route('/ingredients')
def ingredients():
    ingredients = Ingredient.query.all()
    return render_template('ingredients.html', ingredients=ingredients)


# The '/search' route handles the request to search for recipes. It searches for recipes that contain the specified search query.
@app.route('/search')
def search():
    q = request.args.get('q')
    recipes = Recipe.query.filter(Recipe.name.contains(q)).all()
    return render_template('search_results.html', recipes=recipes, q=q)


# The '/register' route handles the request to register a new user. It adds a new User object to the database and logs in the user.
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('index'))
    return render_template('register.html')


# /login: This function authenticates the user when the username and password form is submitted and,
# if successful, logs the user in with the login_user() function. Then the user's last request
# or profile page is redirected with the redirect() function.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(request.args.get('next') or url_for('profile'))
    return render_template('login.html')


# /profile: This function provides a profile page accessible only to logged in users.
# The @login_required decorator provides access only to logged in users and otherwise
# redirects the user to the /login page with the unauthorized() function.
@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


# /logout: This function makes the user not logged in with the
# logout_user() function and then redirects the user to the homepage (/index).
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


# @login_manager.unauthorized_handler: This function redirects users trying to access pages that are only
# accessible to non-login users to the login page.
@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
