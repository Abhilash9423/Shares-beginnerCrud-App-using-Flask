# Shares-beginnerCrud-App-using-Flask
A basic CRUD application to input the name of share,its quantitya price using Flask,HTML,CSS, Boot Strap and SQLite

Installations 
pip install Flask
Pip install Flask-SQLAlchemhy
pip install Flask-Migrate
pip install Flask-WTF
pip install -U WTForms

SQLite is a simple SQL data base engine that comes with flask and can handle all our needs
To connect python , flask and sql together we ill need an ORM (object relation mapper).An ORM will allow us to directly use python instead of SQL syntax to create,edit and update and delete from our data bases. The most common ORM for python is SQL alchemy. Flask-SQLAlchemy is an extension that allows for an easy connection of flask with SQL Alchemy.

When creating a model for a database table you will sometimes need make adjustments to the model, such as adding a new column. Upon making these changes you will need to migrate these changes in order to update the database table .We can do this with Flask –Migrate 

commands to set up flask migrate 
open Command prompt 
Set the Flask_App environment variable- this allows flask migrate to no what your actual Pi script is your flask application .
MacOS/Linux
Export Flask_APP=myapp.py
Windows
Set Flask_App=myapp.py


flask db init - ##Sets up the migrations directory
flask db migrate-m “some message” - ##Sets up the migration file
Flask db upgrade - ##Updates the database with the migration

Other commands to run the main application, open the direcotry from command prompt 
python app.py
