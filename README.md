# Online Herbal

#### An searchable online source for herbal recipes and remedies.

## Project Description

Online Herbal contains a database of recipes which are searchable by name, key words or ingredients. Also, there are instructionals on basic medicine making and information on individual ingredients uses in herbal medicine.
Online Herbal has has full CRUD through the admin console.

### Technologies

Built with Python Django and Postgresql. Deployed to an EC2 instance on AWS, with routing through Route 53.

### Dependencies-

- Python 3
- Django
- Postgresql
- psycopg2-binary
- Pillow

### MVP/POST MVP

### MVP

- Full CRUD
- Searchable Database

### Post-MVP

#### Silver

- Linked infos on ingredients
- Instructionals
- re-usable pics

#### Gold/future

- Email recipes/instructionals to yourself
- Linked to Little Herbal Apothecary
- Add Categories for Recipes and Infos
- Merge Infos and Instructionals and sort by category

### Models

- Recipe
  - title
  - description
  - instructions
  - tags
  - image

-Ingredient - name - measure - info_link

- Instructional - title - instructions - image
  -Info - name - data
  Image - name - pic (upload)

### Code Snippet

This is a snippet for how I got the Recipe form to contain the ingredients, so that the recipe could be created with its ingredients simultaneously.

```
class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 1
    min_num = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, ]

admin.site.register(Recipe, RecipeAdmin)
```

### Issues and resolutions

I spent a lot of time trying to figure out how to create the ingredients with the recipe simultaneously. I had figured out a way to do it with forms, but it wasn't the cleanest solution. Then I realized I needed to do it from the admin console and that solution was much cleaner. I had no need for a non-admin site-user to upload recipes so I removed all of my other forms and just worked with the admin console.
I also made numerous changes to my Models as I worked through implementation. This forced me to become very familiar with the migrations system and I became adept at rolling back migrations and making adjustments.
The key command to clean up migrations is to run a previous migration, but you have to make sure that yourt current code base won't conflict with that migration.

```
python manage.py migrate herbal_recipe_finder 0003
```

This will migrate back to the migration for the herbal_recipe_finder app that starts with 003

### Timelines

area | estimate | actual
basic Layout | |
models, routes, urls| |
forms | |
CSS | |
database isues | |  
data Entry | |
