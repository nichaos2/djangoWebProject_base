## Django project for learning

It would be to nice have the following

* Users authentication – sign in / sign out
* Something like a blog
    - Articles
    - Rating
    - Comments
* Contact with email etc
* Chat box to search what you need to find
* REST API

And later on and very ambitious

* Load your data file + functionallities
* Explore it in tables
* Present it with graphs (interactive)
    - Is it possible from graph manipulation to data manipulation in the back end?

Then it gets more “personal” depending on the need of what you want to do with the data
* ML -  AI – Analytics

## 🚀 Quick start

**How to install and run**

I suggest you insall VSCode editor and WSL Ubuntu for Windows
Then, Install python and git

In terminal
-----------

Install python


Clone the project from github

**To clone only one branch, use:** 

```shell
git clone --branch <branchname> --single-branch <remote-repo-url>
```

go to the project folder and open VSCode with code .


In VSCode
---------

shift+P select python 

open a terminal in VSCode

In this terminal
----------------

```shell
sudo apt install pipenv

sudo pipenv shell

pip install --upgrade django-crispy-forms

python manage.py migrate
```

Create superuser/admin
----------------------

```shell
python manage.py createsuperuser
username: admin
password:
```

Run it
------

Run the command
```shell
python manage.py runserver <port number>
```

Open it
-------

In a browser open the site localhost:port_number

You can see the admin page on localhost:port_ number/admin