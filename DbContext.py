from app import db, Recipe, Ingredient, app, recipe_ingredient, User, Like

# I have defined the ingredients to be used in the recipes here.
# I have indicated the pictures and names of these materials.

with app.app_context():
    db.create_all()
    pasta = Ingredient(name='pasta', image_url='pasta.jpeg')
    tomato_sauce = Ingredient(name='tomato sauce', image_url='Tomato.jpeg')
    meatballs = Ingredient(name='meatballs', image_url='olive_oil.jpeg')
    cheese = Ingredient(name='cheese', image_url='cheese.jpeg')
    cucumber = Ingredient(name='cucumber', image_url='cucumber.jpeg')
    olive_oil = Ingredient(name='olive oil', image_url='olive_oil.jpeg')
    flour = Ingredient(name='flour', image_url='flour.jpeg')
    sugar = Ingredient(name='sugar', image_url='sugar.jpeg')
    baking_powder = Ingredient(name='baking powder', image_url='baking_powder.jpeg')
    salt = Ingredient(name='salt', image_url='salt.jpeg')
    milk = Ingredient(name='milk', image_url='milk.jpeg')
    egg = Ingredient(name='egg', image_url='egg.jpeg')
    butter = Ingredient(name='butter', image_url='butter.jpeg')
    macaroni = Ingredient(name='macaroni', image_url='macaroni.jpeg')
    cheddar_cheese = Ingredient(name='cheddar cheese', image_url='cheddar_cheese.jpeg')
    breadcrumbs = Ingredient(name='breadcrumbs', image_url='breadcrumbs.jpeg')
    pepper = Ingredient(name='pepper', image_url='pepper.jpeg')
    garlic = Ingredient(name='garlic', image_url='garlic.jpeg')
    water = Ingredient(name='water', image_url='water.jpeg')
    onion = Ingredient(name='onion', image_url='onion.jpeg')
    chicken = Ingredient(name='chicken', image_url='chicken.jpeg')
    noodles = Ingredient(name='noodles', image_url='noodles.jpeg')

    # Here, I created the recipes with a class example, respectively. I have added the details of the recipes.

    spaghetti_and_meatballs = Recipe(
        name='Spaghetti and Meatballs',
        instructions='1. Cook pasta according to package instructions. \n 2. Heat tomato sauce in a pan. \n 3. Cook meatballs in the tomato sauce. \n 4. Serve meatballs and sauce over cooked pasta. \n 5. Sprinkle cheese on top.',
        ingredients=[pasta, tomato_sauce, meatballs, cheese],
        image_url='creme-pasta.jpeg'
    )

    Egg_bread = Recipe(
        name='Egg-Bread',
        instructions='1. Cook pasta according to package instructions. 2. Heat tomato sauce in a pan. \n 3. Cook meatballs in the tomato sauce. \n 4. Serve meatballs and sauce over cooked pasta. \n 5. Sprinkle cheese on top.',
        ingredients=[pasta, cheese, olive_oil],
        image_url='egg-bread.jpeg'
    )

    Pancake = Recipe(
        name='Pancake',
        instructions='1. Mix flour, sugar, baking powder, and salt in a bowl. \n 2. In another bowl, beat together milk, egg, and melted butter. \n 3. Add dry ingredients to the wet mixture and mix well. \n 4. Heat a non-stick pan over medium heat. \n 5. Pour batter onto the pan and cook until bubbles appear. \n 6. Flip and cook until the other side is golden brown. \n 7. Serve with your favorite toppings.',
        ingredients=[flour, sugar, baking_powder, salt, milk, egg, butter],
        image_url='pancake.jpeg'
    )

    Mac_and_Cheese = Recipe(
        name='Mac and Cheese',
        instructions='1. Cook macaroni according to package instructions. 2. Melt butter in a separate pan. \n 3. Add flour and stir until well combined. \n 4. Gradually add milk, whisking constantly, until sauce is smooth. \n 5. Add cheese and stir until melted. \n 6. Combine cooked macaroni with cheese sauce. \n 7. Pour mixture into a baking dish and sprinkle with breadcrumbs. \n 8. Bake in preheated oven for 20-25 minutes, or until golden brown.',
        ingredients=[macaroni, butter, flour, milk, cheddar_cheese, breadcrumbs],
        image_url='mac-and-cheese.jpg'
    )

    Lasagna = Recipe(
        name='Lasagna',
        instructions='1. Preheat oven to 375°F. \n 2. Cook lasagna noodles according to package instructions. \n 3. In a pan, cook ground beef, onion, and garlic over medium heat. \n 4. Add tomato sauce, tomato paste, water, sugar, basil, fennel seeds, and salt. \n 5. Simmer for 15 minutes. \n 6. In a separate bowl, mix cottage cheese, beaten eggs, and Parmesan cheese. \n 7. In a 9x13 inch baking dish, spread a layer of the meat sauce. \n 8. Add a layer of noodles. \n 9. Add a layer of the cheese mixture. \n 10. Repeat layers until all ingredients are used up. \n 11. Bake for 25 minutes. \n 12. Let stand for 15 minutes before serving.',
        ingredients=[noodles, onion, garlic, tomato_sauce, water, sugar,
                     salt, egg],
        image_url='lasagna.jpeg'
    )

    Chicken_Soup = Recipe(
        name='Chicken Soup',
        instructions='1. In a large pot, cook carrots, celery, onion, and garlic in olive oil. \n 2. Add chicken broth, chicken, thyme, bay leaves, salt, and pepper. \n 3. Bring to a boil, then reduce heat and simmer for 30 minutes. \n 4. Remove chicken from the pot and shred it. \n 5. Add noodles to the pot and cook for 10 more minutes. \n 6. Return chicken to the pot. \n 7. Serve hot.',
        ingredients=[onion, garlic, olive_oil, chicken, salt, pepper,
                     noodles],
        image_url='chicken_soup.jpeg'
    )

    Spaghetti = Recipe(
        name='Spaghetti',
        instructions='1. Cook spaghetti according to package instructions. \n 2. In a pan, cook ground beef over medium heat. \n 3. Add onion and garlic, and cook until beef is no longer pink. \n 4. Drain excess fat. \n 5. Add tomato sauce, salt, pepper, and Italian seasoning. \n 6. Simmer for 10 minutes. \n 7. Serve meat sauce over cooked spaghetti. \n 8. Sprinkle cheese on top.',
        ingredients=[onion, garlic, tomato_sauce, salt, pepper, cheese],
        image_url='spaghetti.jpeg'
    )


# I added the recipes and ingredients I created to the database.
    db.session.add_all(
        [pasta, tomato_sauce, meatballs, cheese, spaghetti_and_meatballs, olive_oil, cucumber, Egg_bread, Pancake,
         Spaghetti, onion,
         Chicken_Soup, Lasagna, garlic, sugar, cheese, cheddar_cheese, pepper, salt, noodles, chicken, water, egg,
         macaroni, butter, flour, milk, breadcrumbs, baking_powder])
    db.session.commit()
