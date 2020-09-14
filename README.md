## Shares-BeginnerCrud-App-using-Flask

A Server Sided CRUD web application for the benefit of retail traderin shares/stock for storing the shares purchased  sold and balance stocks,  built  in, Python Flask and  Flask Blueprints for modulatory. Application which has the features of few input fields in input tab and other tabs like Delete and Display of the listed stocks. 

Built using Python, Flask,HTML,CSS and BootStrap.

install the following
```
pip install Flask
Pip install Flask-SQLAlchemhy
pip install Flask-Migrate
pip install Flask-WTF
pip install -U WTForms
```
Thoery

SQLite is a simple SQL data base engine that comes with flask and can handle all our needs
To connect python , flask and sql together we ill need an ORM (object relation mapper).An ORM will allow us to directly use python instead of SQL syntax to create,edit and update and delete from our data bases. The most common ORM for python is SQL alchemy. Flask-SQLAlchemy is an extension that allows for an easy connection of flask with SQL Alchemy.
When creating a model for a database table you will sometimes need make adjustments to the model, such as adding a new column. Upon making these changes you will need to migrate these changes in order to update the database table .We can do this with Flask –Migrate 

 
Commands to run
For MacOS/Linux
```
Export Flask_APP=myapp.py
```
For Windows
```
Set Flask_App=myapp.py
```

setting up migration Data base 
```
flask db init - ##Sets up the migrations directory
flask db migrate-m “some message” - ##Sets up the migration file
Flask db upgrade - ##Updates the database with the migration
```
commands to run the main Application
```
python app.py
```
