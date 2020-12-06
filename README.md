![MentorPaired Core CI](https://github.com/mentorpaired/core/workflows/MentorPaired%20Core%20CI/badge.svg) [![Coverage Status](https://coveralls.io/repos/github/mentorpaired/core/badge.svg?branch=staging)](https://coveralls.io/github/mentorpaired/core?branch=staging)

# CORE

Core is the backend of MentorPaired, an app which connects software engineering mentors to mentees who seek to learn any programming language.

#### Tech

Core is written in Python3 and Django 3.0.3.

## Installation

#### Using docker-compose

- Run `$ docker-compose up -d --build` to build the container the first time. Run `$ docker-compose up -d` for subsequent start-ups. To stop the server, run `$ docker-compose down`.

- To create a super user within the docker container, run `$ docker-compose exec web python manage.py createsuperuser`.

#### Ubuntu 18.04 Users

Please install these packages and set up your environment in the order listed below. Run an upgrade or update if you find that the package is already installed:

- Python3. Run the 'python3 -V' command to see the version you have installed.

- Create a virtual environment in order to install packages. The README uses [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation) to create this environment. You could use any virtualenv package of your choice or install this wrapper with:

```sh
pip install virtualenvwrapper
```

- Add these lines at the end of your shell startup script (`.bashrc`, `.zshrc`, etc)

```sh
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

- After editing, reload the startup file (e.g., run `source ~/.bashrc`).

- Create a new virtual environment:

```sh
mkvirtualenv <your_preferred_envname>
```

- Install requirements in the virtual environment created:

```sh
pip install -r requirements.txt
```

- Install [PostgreSQL](https://www.postgresql.org/).

- Create a database with PostgresQL, the installation instructions for Ubuntu can be found [here](https://www.postgresql.org/download/linux/ubuntu/). Make sure to note Database name, Database Username and Password and also ensure that the server is running

- Create a .env file in the root directory of the project and copy the content of `.env.example` file to it. Other values not listed below but present in the .env.example file should also be replaced with your own values in your .env file.

- Replace
  - `DB_NAME` with your database name,
  - `DB_USER` with your database username,
  - `DB_PASSWORD` with your database password,
  - `SECRET_KEY` with the value gotten when you run this script/command in the terminal

```sh
python3 scripts/secret_key.py
```

- Run database migrations with this command

```sh
python3 manage.py migrate
```

- Run server to ensure everything is working properly.

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

- Download [Python3](https://www.python.org/downloads/). It is advisable to install the python package as an administrator. Click on the 'Add path' checkbox before moving on to the next step of the installation process. Run this command in your terminal to see the version you have installed.

  ```sh
  python3 -V
  ```

- Download [pip](https://pip.pypa.io/en/latest/installing/) and follow the instructions in the link as an installation guide.

- [PostgreSQL](https://www.postgresql.org/download/windows/) (Ensure the server is running).

- It is advisable to install Django in a virtual environment. The README uses [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation) to create this environment. You could use any virtualenv package of your choice but for Windows, install this wrapper with:

  ```sh
  py -m pip install virtualenvwrapper-win
  ```

- Create a new virtual environment:

  ```sh
  mkvirtualenv <envname>
  ```

- Activate the virtual environment with:

  ```sh
  workon <envname>
  ```

- Install requirements in the virtual environment created:

  ```sh
  py -m pip install Django
  ```

  ```sh
  pip install -r requirements.txt
  ```

- Create a database with PostgresQL, if you installed it earlier. If not, installation instructions can be found [here](https://www.postgresql.org/download/windows/). Make sure to note database name, database username and password.

- Create a .env file and copy the content of `.env.example` file to it. Place this file in the root directory of the core project.

- Replace

  - `DB_NAME` with your database name,
  - `DB_USER` with your database username,
  - `DB_PASSWORD` with your database password,
  - `SECRET_KEY` with the value gotten when you run this script in the terminal `python3 scripts/secret_key.py`.

- Run database migrations with this command

```sh
python manage.py migrate
```

- Run server to ensure everything is working properly.

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

### Using the API endpoint

- Create a superuser account

  ```sh
  python manage.py createsuperuser
  ```

- Send a POST request as a JSON object with the username and password values to this [URL](http://localhost:8000/api/token/)

- Enter your access token value which was generated as part of the response in the request authorization tab in the following format:
  ```sh
  Authorization: Bearer <Access_Token_Value>
  ```

### OAuth setup instructions

- Your local development environment needs to be set up correctly before you can use the oauth login flow through Postman or the React frontend.

  - Log in to your Django admin with your superuser credentials.

    ```
    http://localhost:8000/admin
    ```

  - Select `Applications` in the Django Oauth Toolkit section.
  - Click on `Add Application`.
  - Do not modify the client id and client secret values, these values will be used to populate your .env file.
  - For `User` field, select your superuser.
  - For `Redirect uris`, input `http://localhost:3000/login` as its value.
  - Select any client type.
  - Select `Authorization code` as the authorization grant type.
  - Type in any names of your choice as your app name.
  - `Skip authorization` should be left unchecked.
  - Save the app.

- Navigate to your Github personal settings section to create a Github OAuth app.

  - Click on `Developer settings`, select `OAuth Apps`.
  - Click `New OAuth App` and create a new app.
  - For `Homepage URL` and `Authorization callback URL`, use the values `http://localhost:3000` and `http://localhost:3000/login` respectively.
  - Click the `register application` button to save the app.

- Update your .env file with the values in the oauth apps you created.

### Python installation instructions for Windows, macOS and other Linux distro Users

- The following may serve as a guide:
  - (https://www.python.org/downloads/)
  - (https://realpython.com/installing-python/)
  - (https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
  - (https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment)

#### Collaboration

- You need to have PostgresQL installed and set up on your machine.

- Clone the repository from the `staging` branch and please read the [contributing guide](/CONTRIBUTING.md).

- You may also need to have [Heroku](https://devcenter.heroku.com/articles/heroku-cli) and [Travis CI](https://github.com/travis-ci/travis.rb#installation) installed.

- Run `Travis` and `Heroku` login commands in your terminal after installation
  ```sh
  travis login
  ```
  ```sh
  heroku login
  ```

Contact [Kosy](https://github.com/kosyfrances), [Delores](https://github.com/Del-sama) or [Nkoli](https://github.com/Nkoli) for more details.

### License

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for more details.

### Acknowledgements

Special thanks to [Kosy](https://github.com/kosyfrances), [Delores](https://github.com/Del-sama) and [Tunde](https://github.com/toystars) for guiding us through the entire app creation process, reviewing our code and unblocking us when we are stuck with an issue, and especially for taking the time out of their busy lives to provide free mentorship to us.
