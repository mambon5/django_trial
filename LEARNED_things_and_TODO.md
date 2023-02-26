# Keep track of to do issue, and learned things

- [Keep track of to do issue, and learned things](#keep-track-of-to-do-issue-and-learned-things)
  - [TO DO list](#to-do-list)
  - [I was last doing:](#i-was-last-doing)
  - [Learned things](#learned-things)
    - [How to import files and functions](#how-to-import-files-and-functions)
    - [Bootstrap for CSS styling in Python:](#bootstrap-for-css-styling-in-python)

## TO DO list

## I was last doing:

    1. > Django tutorial, showcase projects>  https://realpython.com/get-started-with-django-1/#showcase-your-projects


## Learned things 

From this python tutorial about django: https://realpython.com/get-started-with-django-1/

### How to import files and functions 
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

### Bootstrap for CSS styling in Python:
 We can use **Boostrap** to style our front-end, without having to do all the details of CSS! Isn't this cool? https://getbootstrap.com/docs/4.1/getting-started/introduction/#quick-start



