# Mini-blog (Django)

| [Русская версия](https://github.com/KonstErz/DIY_Django_mini-blog/blob/master/README.ru.md) |

This is a small website written in Django.
It was created as a DIY as part of the Django tutorial from [MDN web docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/django_assessment_blog).


## Characteristics

This web application creates an very basic blog site.

The main implemented functionality:

+ There are models for blogs, bloggers and blog comments.
+ Blog authors can create text blogs using admin site.
+ Any logged user can add comments to the blog through the form.
+ Any user can view a list of all blogs, all bloggers, as well as detailed information about each blogger or blog, including comments.


## Quick Start

You can run this project locally on your computer by following these steps:

1. Set up the [Python development environment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment). It's recommended using a Python virtual environment.  

With python3 on your local machine, you can run this project in a virtual environment by following these steps:  

+ Create a folder for the project named 'test_django_project'. Go to this folder and clone the repository with the project:

    ```
    git clone https://github.com/KonstErz/DIY_Django_mini-blog.git .
    ```

+ Create a virtual python3 environment in the same folder using the following command:

    ```
    python3 -m venv env
    ```

where *'env'* is the name of the virtual environment.

+ Activate the created virtual environment:

    ```
    source env/bin/activate
    ```

2. After creating and activating the virtual environment from the root directory of the project, run the following commands in the terminal (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):

    ```
    pip3 install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py collectstatic
    python3 manage.py test      # Run the standard tests. These should all pass.
    python3 manage.py createsuperuser       # Create a superuser.
    python3 manage.py runserver
    ```

3. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin panel of the site.
4. You will need to create test bloggers and blogs under their authorship. You can also register other test users who can write comments on blogs after logging in the system.
5. Open tab to `http://127.0.0.1:8000/blog/` to see the main site, with your new objects.  
Ctrl+C - to exit debug mode of a web application and `deactivate` - command to exit the virtual environment.
