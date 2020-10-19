import sys

# add your project directory to the sys.path
project_home = u'/app'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from werkzeug.wsgi import DispatcherMiddleware
from run import app as app1

app = DispatcherMiddleware(None, {
    '/app':    app1
})