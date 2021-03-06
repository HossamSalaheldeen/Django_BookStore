# BookStore sample application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/HossamSalaheldeen/Django_BookStore.git
$ cd Django_BookStore
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env
$ .\env\Scripts\activate
```

```sh
(env)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd Django_BookStore
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/books/`.
