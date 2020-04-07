# [Flask Dashboard Material](https://appseed.us/admin-dashboards/flask-dashboard-material-design)

**Open-Source Admin Dashboard** coded in **[Flask Framework](https://palletsprojects.com/p/flask/)** on top of **Material Dashboard** design (free version) - Provided by **AppSeed** [Web App Generator](https://appseed.us/app-generator).

<br />

> **[Feedback/Suggest Feature](https://appseed.nolt.io/)**

This product is **built based on community feedback**. Feel free (anonymously) to **[suggest/vote features](https://appseed.nolt.io/3)**. For more information, please access the [Facebook](https://www.facebook.com/webappseed/) page or chat with us on [Discord](https://discord.gg/fZC6hup).

<br />

## Dashboard Features:

- SQLite, PostgreSQL, SQLAlchemy ORM
- Alembic (DB schema migrations)
- Modular design with **Blueprints**
- Session-Based authentication (via **flask_login**)
- Forms validation
- Deployment scripts: Docker, Gunicorn
- UI Kit: **[Material Dashboard](https://www.creative-tim.com/product/material-dashboard?ref=appseed)** provided by **[Creative-Tim](https://www.creative-tim.com/?ref=appseed)**
- **MIT License**
- Support: Free support via **Github** and (Paid) **24/7 LIVE Support** via [Discord](https://discord.gg/fZC6hup)

<br />

## Dashboard Links

- [Flask Dashboard Material](https://appseed.us/admin-dashboards/flask-dashboard-material-design) - Product page
- [Flask Dashboard Material](https://docs.appseed.us/admin-dashboards/flask-dashboard-material/) - Documentation
- [Flask Dashboard Material](https://flask-dashboard-material.appseed.us/login) - LIVE demo
- **[Flask Dashboard Material PRO](https://appseed.us/admin-dashboards/flask-dashboard-material-pro)** - Premium Version - [LIVE Demo](https://flask-dashboard-material-pro.appseed.us/login)

<br />

## Want more? Go PRO!

PRO versions include **Premium UI Kits**, Lifetime updates and **24/7 LIVE Support** (via [Discord](https://discord.gg/fZC6hup))

| [Flask Dashboard Material PRO](https://appseed.us/admin-dashboards/flask-dashboard-material-pro) | [Flask Dashboard Dashkit PRO](https://appseed.us/admin-dashboards/flask-dashboard-dashkit-pro) | [Premium Flask Dashboards](https://appseed.us/bundles/flask-admin-dashboards-pro) |
| --- | --- | --- |
| [![Flask Dashboard Material PRO](https://raw.githubusercontent.com/app-generator/static/master/products/flask-dashboard-material-pro-screen.png)](https://appseed.us/admin-dashboards/flask-dashboard-material-pro)  | [![Flask Dashboard Dashkit PRO](https://raw.githubusercontent.com/app-generator/static/master/products/flask-dashboard-dashkit-pro-screen.png)](https://appseed.us/admin-dashboards/flask-dashboard-dashkit-pro) | [![Premium Flask Dashboards - Provided by AppSeed](https://raw.githubusercontent.com/app-generator/static/master/products/flask-dashboard-black-pro-screen.png)](https://appseed.us/bundles/flask-admin-dashboards-pro)

<br />
<br />

![Flask Dashboard Material - Open-Source Dashboard.](https://raw.githubusercontent.com/app-generator/static/master/products/flask-dashboard-material-design-screen.png)

<br />

## How to use it

```bash
$ # Get the code
$ git clone https://github.com/app-generator/flask-material-dashboard.git
$ cd flask-material-dashboard
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv --no-site-packages env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv --no-site-packages env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Database
$ pip3 install -r requirements.txt
$
$ # OR with PostgreSQL connector
$ # pip install -r requirements-pgsql.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Start the application (development mode)
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the dashboard in browser: http://127.0.0.1:5000/
```

<br />

## Deployment

The app is provided with a basic configuration to be executed in [Docker](https://www.docker.com/), [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

<br />

### [Docker](https://www.docker.com/) execution
---

The application can be easily executed in a docker container. The steps:

> Get the code

```bash
$ git clone https://github.com/app-generator/flask-material-dashboard.git
$ cd flask-material-dashboard
```

> Start the app in Docker

```bash
$ sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d
```

Visit `http://localhost:5005` in your browser. The app should be up & running. 

<br />

### [Gunicorn](https://gunicorn.org/)
---

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

> Install using pip

```bash
$ pip install gunicorn
```
> Start the app using gunicorn binary

```bash
$ gunicorn --bind 0.0.0.0:8001 run:app
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.


<br />

### [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/)
---

Waitress (Gunicorn equivalent for Windows) is meant to be a production-quality pure-Python WSGI server with very acceptable performance. It has no dependencies except ones that live in the Python standard library.

> Install using pip

```bash
$ pip install waitress
```
> Start the app using [waitress-serve](https://docs.pylonsproject.org/projects/waitress/en/stable/runner.html)

```bash
$ waitress-serve --port=8001 run:app
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

## Credits & Links

<br />

## What is [Flask](https://www.palletsprojects.com/p/flask/)

**Flask** is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

<br />

## [What is a dashboard](https://en.wikipedia.org/wiki/Dashboard_(business))

A dashboard is a set of pages that are easy to read and offer information to the user in real-time regarding his business. A dashboard usually consists of graphical representations of the current status and trends within an organization. Having a well-designed dashboard will give you the possibility to act and make informed decisions based on the data that your business provides - *definition provided by [Creative-Tim - Free Dashboard Templates](https://www.creative-tim.com/blog/web-design/free-dashboard-templates/?ref=appseed)*.

<br />

## [Material Dashboard](https://www.creative-tim.com/product/material-dashboard?ref=appseed)

**[Material Dashboard](https://www.creative-tim.com/product/material-dashboard?ref=appseed)** is a free Material Bootstrap 4 Admin with a fresh, new design inspired by Google's Material Design. Material Dashboard was built over the popular Bootstrap 4 framework and it comes with a couple of third-party plugins redesigned to fit in with the rest of the elements.

<br />

---
**[Flask Dashboard Material](https://appseed.us/admin-dashboards/flask-dashboard-material-design)** - Provided by **AppSeed** [Web App Generator](https://appseed.us/app-generator).
