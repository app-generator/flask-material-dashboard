# [Flask Material Dashboard](https://appseed.us/admin-dashboards/flask-dashboard-material-design)

Open-Source and Free **[admin dashboard](https://appseed.us/admin-dashboards)** with Material Design coded in **[Flask](https://palletsprojects.com/p/flask/)**. **Dashboard** features:
- SQLite database, SQLAlchemy ORM
- Authentication flow (login, register)
- Static Build `python ./static.py` via Frozen-Flask
- **MIT License** 

<br />

![Flask Material Dashboard - Open-Source Flask Dashboard.](https://raw.githubusercontent.com/app-generator/static/master/products/flask-dashboard-material-design-intro.gif)

<br />

## Build from sources

```bash
$ # clone the sources
$ git clone https://github.com/app-generator/flask-material-dashboard.git
$ cd flask-material-dashboard
$
$ # install modules using a virtualenv
$ virtualenv --no-site-packages env
$ source env/bin/activate
$
$ # install deps
$ pip install -r requirements.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix) export FLASK_APP=app.py
$ (Windows) set FLASK_APP=app.py
$ (Powershell) $env:FLASK_APP = ".\app.py"
$ 
$ # Create SQLite database using the Flask console
$ flask shell
>> from app import db
>> db.create_all()
>> quit()
$ # SQLite database.db should be created in the app folder:
$ # app\database.db
$
$ flask run
$ # app is running on port 5000
```

<br />

## Want more? Go PRO!

<br />

| [Flask Dashboard Material](https://appseed.us/admin-dashboards/flask-dashboard-material-pro) | [Flask Dashboard Argon](https://appseed.us/admin-dashboards/flask-dashboard-argon-pro) | [Flask Dashboard Black](https://appseed.us/admin-dashboards/flask-dashboard-black-pro) |
| --- | --- | --- |
| [![Flask Dashboard Material PRO](https://raw.githubusercontent.com/app-generator/static/master/products/flask-dashboard-material-pro-intro.gif)](https://appseed.us/admin-dashboards/flask-dashboard-material-pro)  | [![Flask Dashboard Argon PRO](https://raw.githubusercontent.com/app-generator/static/master/products/flask-dashboard-argon-pro-intro.gif)](https://appseed.us/admin-dashboards/flask-dashboard-argon-pro) | [![Flask Dashboard Black PRO](https://raw.githubusercontent.com/app-generator/static/master/products/flask-dashboard-black-pro-intro.gif)](https://appseed.us/admin-dashboards/flask-dashboard-black-pro)

<br />

## Resources

1. [Flask Documentation](http://flask.pocoo.org/docs/)
2. [Flask Extensions](http://flask.pocoo.org/extensions/)
3. [More Flask Apps](https://appseed.us/apps/flask-apps)
4. [Read More about Flask Apps](https://blog.appseed.us/tag/flask)

<br />

---
[Flask Material Dashboard](https://appseed.us/admin-dashboards/flask-dashboard-material-design) provided by **AppSeed**
