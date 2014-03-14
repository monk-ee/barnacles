from barnacles.modules.main import *
from barnacles.modules.fetch import *
from barnacles.modules.py_email import *
from barnacles.modules.cache import cache
from datetime import datetime
from dateutil import parser
from StringIO import *
from flask import Blueprint, request, redirect, url_for,  \
     render_template, flash, send_from_directory, send_file
from werkzeug import secure_filename

main  = Blueprint('main', __name__)
cache_timeout = int(app.config['CONFIG']['cache']['timeout'])

@main.route('/')
def list_reports():
    os.chdir(app.config['UPLOAD_FOLDER'])
    csv = list()
    for files in os.listdir("."):
        if files.endswith(".csv"):
            csv.append(files)    return render_template('main.html', csv=csv)


@main.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')