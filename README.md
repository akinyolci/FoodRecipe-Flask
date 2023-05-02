<h1 align="center">FoodRecipe-Flask</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Python-v3.8.5-blue?logo=python&style=flat-square" alt="Python Version" />
  <img src="https://img.shields.io/badge/Flask-v2.0.1-blue?logo=flask&style=flat-square" alt="Flask Version" />
  <img src="https://img.shields.io/badge/SQLAlchemy-v1.4.22-blue?logo=sqlite&style=flat-square" alt="SQLAlchemy Version" />
  <img src="https://img.shields.io/github/license/example/example-project?style=flat-square" alt="License" />
</p>
<p align="center">
  A Food Recipe App with Flask, Python.
  <br />
  <a href="https://github.com/akinyolci/FoodRecipe-Flask"><strong>Explore the docs »</strong></a>
  <br />
  <br />
  <a href="mailto:akinyolcu0@gmail.com">Report Bug</a>
  ·
  <a href="mailto:akinyolcu0@gmail.com">Request Feature</a>
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- AboutProject -->
<h2 align="center"> :pencil: About Project</h2>
<h4 align="center"> Why FoodRecipe App ? </h4>
<p align="justify"> 
A web application created for this project makes use of the Flask web framework.
Users can see, like, and propose recipes using this platform for recipe sharing
depending on their preferences. The program manages a SQLite database that has user information,
recipe information, and ingredient information using SQLAlchemy. In order to manage user login and authorisation,
it additionally supports Flask-Login.
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- Features -->
<h2 align="center"> :bulb: Features </h2>
List all the recipes and ingredients in the database
View recipe details, such as name, picture, ingredients, and directions
Like and unlike recipes
View a list of all the recipes that the user has liked
View recommended recipes that share at least two ingredients with the user's favorite dishes
User authentication and authorization


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- GettingStarted -->
<div>
  <h2 align="center"> :rocket: Getting Started </h2>
  <p>Prerequisites:</p>
  <ul>
    <li>Python 3.8.5 or higher</li>
    <li>Flask 2.0.1 or higher</li>
    <li>SQLAlchemy 1.4.22 or higher</li>
  </ul>
  <p>Installation:</p>
  <ol>
    <li>Clone the repo:</li>
  </ol>
  <pre><code>git clone https://github.com/akinyolci/FoodRecipe-Flask.git</code></pre>
  <p>Great! To run the website, please follow the steps below:</p>
  <ol>
    <li>Install the required packages listed in the requirements.txt file by running the following command in your terminal:</li>
  </ol>
  <pre><code>pip install -r requirements.txt</code></pre>
  <ol start="2">
    <li>Navigate to the project directory:</li>
  </ol>
  <pre><code>cd FoodRecipe</code></pre>
  <ol start="3">
    <li>Create the database by running the following command:</li>
  </ol>
  <pre><code>python3 DbContext.py</code></pre>
  <ol start="4">
    <li>Start the server by running the following command:</li>
  </ol>
  <pre><code>python3 app.py</code></pre>
  <p>Finally, open your web browser and navigate to <a href="http://localhost:5000">http://localhost:5000</a> to access the FoodRecipe app.</p>
  <p>That's it! You should now be able to use the app and browse the recipes.</p>
</div>
