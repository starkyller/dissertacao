# Sub Project - hmobiweb - backend

[Go back to Primary README](../README.md)
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>
    <h2 style="display: inline-block">Table of Contents</h2>
  </summary>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#build-with">Built With</a></li>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
        <a href="#usage">Usage</a>
    </li>
</details>





<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Build With

* [Django](https://github.com/django/django)

### Prerequisites

This is an example of how to list things you need to use the software.
* Python 3.6.9+
* [pipenv](https://pypi.org/project/pipenv/)


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/starkyller/dissertacao.git
   ```
2. Change Directory to backend
   ```sh
   cd backend
   ```
3. Install dependencies
   ```sh
   pipenv install --dev
   ```
4. Generate SQLite Database
    ```sh
   ./hmobiweb/manage.py migrate
   ```
5. Create a superuser
    ```sh
   ./hmobiweb/manage.py createsuperuser
   ```
6. Run the local server
    ```sh
   ./hmobiweb/manage.py runserver
   ```
7. Navigate to /admin on a browser and have fun

<!-- USAGE EXAMPLES -->
## Production instalation

### Installation

1. Update system and install general dependencies
   ```sh
   sudo apt update && sudo apt upgrade && sudo apt install nginx libpq-dev pip3-pip
   sudo -H pip3 install pipenv
   ```

2. Clone the repo
   ```sh
   git clone https://github.com/starkyller/dissertacao.git
   ```
3. Change Directory to backend and create
   ```sh
   cd backend && mkdir.venv
   ```
4. Install dependencies
   ```sh
   pipenv install
   pipenv install psycopg2
   pipenv install gunicorn
   ```
5. Change settings file on src/manage.py

   os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev") -> os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.prod")
6. Change settings file on src/core/wsgi.py
   
   os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev") -> os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.production")
7. Change settings file on src/core/wsgi.py
   
   os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev") -> os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.production")
8. On core/settings/production.py

   Input your desired postgresql credentials and change the ALLOWED_HOSTS 

   ps: dont forget to create the database before running the migrations.
9. Run the migrations, collect static files, create super user
   ```sh
   ./manage.py migrate
   ./manage.py collectstatic
   ./manage.py createsuperuser
   ```
10. Change the ownership of the project
   ```sh
   sudo chown -R :www-data backend
   ```
11. Exit of the virtualenv
   ```sh
   exit
   ```
12. Add the config files

   In the production_config_files you have the files and the path they should be in, it is just a matter of copying them, just ignore the load_testing folder.

13. Make the gunicorn log folder with the needed permissions

   ```sh
   sudo mkdir /var/log/gunicorn 
   sudo chown -R :www-data /var/log/gunicorn/
   sudo chmod g+w -R  /var/log/gunicorn/
   ```

14. Start the webservice
   ```sh
   sudo ln -s /etc/nginx/sites-available/hmobiweb /etc/nginx/sites-enabled
   sudo nginx -s reload
   sudo systemctl start hmobiweb
   sudo systemctl enable hmobiweb
   ```
   