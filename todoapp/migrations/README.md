# Migrations 

- Migrations deal with how we manage modifications to our data schema, over time.
- Mistakes to our database schema are very expensive to make. The entire app can go down, so we want to
    + quickly roll back changes, and
    + test changes before we make them
- A Migration is a file that keeps track of changes to our database schema (structure of our database).
- Offers version control on our schema.

## Migrations in the real world
Sample solution: Imagine you are a database administrator for a university. You have a large database of student records, but the government has mandated a new requirement for vaccinations for all students. This column must be added to the database. Because the database is already live, this allows you to alter both the schema as well as repopulate with default data. By using the migration tool, should this requirement ever become not required, we could easily downgrade. It is useful for auditing as there is a record.

## Flask-Migrate
### Installing Flask-Migrate
- Do a pip install of Flask-Migrate, or if you're using a custom Python 3, Python version you could do pip three install Flask-Migrate to install it for Python 3.

- `pip3 install Flask-Migrate`


>```Terminal 
> (make sure you are in the todoapp folder)
> sudo -u postgres -i
> dropdb todoapp
> createdb todoapp
> exit
> 
> flask db init
>
> flask db migrate # to create new version upgrade script
> 
> flask db upgrade # run the newest version upgrade script
> flask db downgrade
> ```
# References
- https://www.youtube.com/watch?v=Sr-QQluNUFo
- https://www.youtube.com/watch?v=3vlK5FUdW_I&t=50s
- https://www.youtube.com/watch?v=lTgA05lcIHA&t=89s
- https://www.youtube.com/watch?v=H-PWJ5p-SpM&t=228s
- https://alembic.sqlalchemy.org/en/latest/
    + The main documentations site for Alembic with complete references for everything
- https://flask-migrate.readthedocs.io/en/latest/
    + The main documentations site for Flask-Migrate with complete references for everything
- https://flask.palletsprojects.com/en/2.2.x/
- https://jinja.palletsprojects.com/en/2.10.x/templates/#if
