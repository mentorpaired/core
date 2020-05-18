[![Build Status](https://travis-ci.org/mentorpaired/core.svg?branch=staging)](https://travis-ci.org/mentorpaired/core) [![Coverage Status](https://coveralls.io/repos/github/mentorpaired/core/badge.svg?branch=staging)](https://coveralls.io/github/mentorpaired/core?branch=staging)

# CORE
Core is the backend of MentorPaired, an app which connects software engineering mentors to mentees who seek to learn any programming language.

#### Tech
Core is written in Python3 and Django 3.0.3.

## Installation

#### Ubuntu 18.04 Users

 Please install and set up the following packages first. Upgrade if you find the package is already installed:

* Python3. Run the 'python3 -V' command to see the version you have installed.

* Git

* [PostgreSQL](https://www.postgresql.org/) (Make sure to note Database name, Database Username and Password. Ensure the server is running).

* It is advisable to install Django in a virtual environment. The README uses [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation) to create this environment. You could use any virtualenv package of your choice or install this wrapper with:

```sh
pip install virtualenvwrapper
```

* Add these lines at the end of your shell startup script (`.bashrc`, `.zshrc`, etc)

```sh
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

* After editing, reload the startup file (e.g., run `source ~/.bashrc`).

* Create a new virtual environment:

```sh
mkvirtualenv <envname>
```

* Install requirements in the virtual environment created:

```sh
pip install -r requirements.txt
```

* Create a database with PostgresQL if you installed it earlier. If not, installation instructions can be found [here](https://www.postgresql.org/download/linux/ubuntu/)

* Create a .env file and copy the content of `.env.example` file to it. 

* Replace
  - `DB_NAME` with your database name,
  - `DB_USER` with your database username,
  - `DB_PASSWORD` with your database password,
  - `SECRET_KEY` with the value gotten when you run this script/command in the terminal 
```sh
python3 scripts/secret_key.py
```

* Run database migrations with this command

```sh
python3 manage.py migrate
```

* Run server to ensure everything is working properly.

```sh
python3 manage.py runserver
```

To run tests:

```sh
python manage.py test
```

```sh
flake8 .
```

### Windows 10 Users
 Please install and set up the following packages first. Upgrade if you find the package is already installed:

* Download [Python3](https://www.python.org/downloads/). It is advisable to install the python package as an administrator. Click on the 'Add path' checkbox before moving on to the next step of the installation process. Run this command in your terminal to see the version you have installed.
  ```sh
  python3 -V
  ```

* Download [pip](https://pip.pypa.io/en/latest/installing/) and follow the instructions in the link as an installation guide.

* Download and install [Git](https://git-scm.com/download/win). Clone the project to a fresh directory/folder from the `staging` branch. 

* [PostgreSQL](https://www.postgresql.org/download/windows/) (Ensure the server is running). 

* It is advisable to install Django in a virtual environment. The README uses [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation) to create this environment. You could use any virtualenv package of your choice but for Windows, install this wrapper with:

  ```sh
  py -m pip install virtualenvwrapper-win
  ```

* Then, create a new virtual environment:

  ```sh
  mkvirtualenv <envname>
  ```

* Activate the virtual environment with: 
  ```sh
  workon <envname>
  ```

* Install requirements in the virtual environment created:

  ```sh
  py -m pip install Django
  ```

  ```sh
  pip install -r requirements.txt
  ```

* Create a database with PostgresQL, if you installed it earlier. If not, installation instructions can be found [here](https://www.postgresql.org/download/windows/). Make sure to note Database name, Database Username and Password.

* Create a .env file and copy the content of `.env.example` file to it. Place this file in the folder named `core`.

* Replace 
  - `DB_NAME` with your database name,
  - `DB_USER` with your database username,
  - `DB_PASSWORD` with your database password,
  - `SECRET_KEY` with the value gotten when you run this script in the terminal `python3 scripts/secret_key.py`.

* Run database migrations with this command

```sh
python manage.py migrate
```

* Run server to ensure everything is working properly.

```sh
python manage.py runserver
```

To run tests:

```sh
python manage.py test
```

```sh
flake8 .
```

### Python installation instructions for Windows, macOS and other Linux distro Users

* The following may serve as a guide:
  * (https://www.python.org/downloads/)
  * (https://realpython.com/installing-python/)
  * (https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
  * (https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment)

### Collaboration
You need to have PostgresQL installed and set up on your machine.

Clone the repository from the `staging` branch and please read the [contributing guide](/CONTRIBUTING.md).

You may also need to have `Heroku`, `Ruby` and `Travis CI` installed and signed in. 
Contact [Kosy](https://github.com/kosyfrances), [Delores](https://github.com/Del-sama) or [Nkoli](https://github.com/Nkoli) for more details.

### License
This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for more details.

### Acknowledgements
Special thanks to [Kosy](https://github.com/kosyfrances) and [Delores](https://github.com/Del-sama) for guiding me through this entire app creation process and being my mentors.
