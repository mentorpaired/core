[![Build Status](https://travis-ci.org/mentorpaired/core.svg?branch=staging)](https://travis-ci.org/mentorpaired/core) [![Coverage Status](https://coveralls.io/repos/github/mentorpaired/core/badge.svg?branch=staging)](https://coveralls.io/github/mentorpaired/core?branch=staging)

# CORE
Core is the backend of MentorPaired, an app which connects software engineering mentors to mentees who seek to learn any programming language.

### Tech
Core is written in Python3 and Django 3.0.3.

### Installation

**Ubuntu 18.04 Users**
Please install and set up the following packages first, upgrade if you find the package is already installed:
* Python3. Run the 'python3 -V' command to see the version you have installed.
* PostgreSQL (Ensure the server is running). Alternatively, if your project is a small one or you find you don't need PostgreSQL, Python includes a lightweight database called SQLite so you won't need to set up a database, however it cannot support a high level of concurrency.

* It is advisable to install Django in a virtual environment and the library for doing this is called virtualenvwrapper (https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation). Install this library with:
```
sudo pip install virtualenvwrapper
```
* Add these lines at the end of your shell startup script (```.bashrc```, ```.zshrc```, etc)
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```
* After editing, reload the startup file(e.g., run ```source ~/.bashrc```).
* Create a new virtual environment:
```
mkvirtualenv <envname>
```
* Install requirements in the virtual environment created:
```
pip install -r requirements.txt
```

* Create a database with PostgresQL, if you installed it earlier. If not, installation instructions can be found here (https://www.postgresql.org/download/linux/ubuntu/)
* Create a .env file and copy the content of `.env.example` file to it.
* Replace
  - `DB_NAME` with your database name,
  - `DB_USER` with your database username,
  - `DB_PASSWORD` with your database password,
  - `SECRET_KEY` with the value gotten when you run this script in the terminal `python3 scripts/secret_key.py`.

* Run database migrations with this command
```
python3 manage.py migrate
```

* Run server to ensure everything is working properly.
```
python3 manage.py runserver
```

To run tests:
```
$ python manage.py test
```
```
$ flake8 .
```

### Collaboration
You need to have PostgresQL installed and set up on your machine.

Fork the repository and please read the CONTRIBUTING.md guide.
