# Keep track of to do issue, and learned things

- [Keep track of to do issue, and learned things](#keep-track-of-to-do-issue-and-learned-things)
  - [TO DO list](#to-do-list)
  - [I was last doing:](#i-was-last-doing)
  - [Learned things](#learned-things)
    - [Python Django tutorial](#python-django-tutorial)
      - [How to import files and functions](#how-to-import-files-and-functions)
      - [Bootstrap for CSS styling in Python:](#bootstrap-for-css-styling-in-python)
      - [Creating database tables](#creating-database-tables)
      - [The views send data to html files](#the-views-send-data-to-html-files)
      - [Django admin for adding data to the tables](#django-admin-for-adding-data-to-the-tables)
    - [Set up git repo locally](#set-up-git-repo-locally)

## TO DO list

## I was last doing:

    1. > Django tutorial, Blog App: Views  https://realpython.com/get-started-with-django-1/#blog-app-views
   
## Learned things 

### Python Django tutorial 
From this python tutorial about django: https://realpython.com/get-started-with-django-1/

#### How to import files and functions 
    Depends on the entry-point script.

    In a file system like this:

    ```
    application 
    ├── app
    │   └── folder
    │       └── file.py
    └── app2
        └── some_folder
            └── some_file.py
    ```

    We can import a function *function1* placed within *file.py* from *some_file.py* given that the main script is run in the **application** folder. In other words:
    *Python only searches the directory that the **entry-point** script is running from and sys.path*. 

    In the above example we would write inside the file *some_file.py*:

    `from app1.folder.file import function1`

    considering the main script is executed in the folder *application*.

    I had to do this for importing the *views.py* file while running the *urls.py* file placed withing my *hello_world* folder. My file system was the following:

    ```
    application 
    ├── db.sqlite3
    ├── hello_world
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── models.py
    │   ├── templates
    │   │   └── hello_world.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── LEARNED_things_and_TODO.md
    ├── manage.py
    ├── personal_portfolio
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ```

#### Bootstrap for CSS styling in Python:
 We can use **Boostrap** to style our front-end, without having to do all the details of CSS! Isn't this cool? https://getbootstrap.com/docs/4.1/getting-started/introduction/#quick-start

#### Creating database tables

1. A database table is a django *model*. Each model is a class (in python) where each property will be a column in the database table, and where each instance will be a new row of the table. By default Django uses *SQLite*.

2. In order to create a table, we create a **migration** using the command:
   `python3 manage.py makemigrations projects`
   where *projects* is the directory that contains the *models.py* file. Inside the *models.py* the classes (or database tables) are declared.

3. First we create a model class (or table), then a migration.

4. Finally we *apply the migrations* or database table creations, by runnin the command:
   `python3 manage.py migrate projects`

#### The views send data to html files

 As the tutorial says: *view functions to send the data from the database to the HTML templates*

#### Django admin for adding data to the tables

### Set up git repo locally

In order to start ur dir run

`git init .`

2. Then create a repo on github.com

3. Then run

```
git add .
git commit
git push origin url.of.repository
```
For storing your token run
`git config --global credential.helper store`

After running this command, do a commit and push, and when you input your password/token again, it will be saved forever.