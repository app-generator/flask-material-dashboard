# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from jinja2 import TemplateNotFound
from flask_login import login_required, current_user
from apps import db, config
from apps.models import *
from apps.tasks import *

@blueprint.route('/')
@blueprint.route('/index')
def index():
    return render_template('pages/index.html', segment='dashboard')

@blueprint.route('/tables')
def tables():
    context = {
        'segment': 'tables'
    }
    return render_template('pages/tables.html', **context)

@blueprint.route('/billing')
def billing():
    context = {
        'segment': 'billing'
    }
    return render_template('pages/billing.html', **context)

@blueprint.route('/virtual-reality')
def virtual_reality():
    context = {
        'segment': 'virtual_reality'
    }
    return render_template('pages/virtual-reality.html', **context)

@blueprint.route('/rtl')
def rtl():
    context = {
        'segment': 'rtl'
    }
    return render_template('pages/rtl.html', **context)

@blueprint.route('/notifications')
def notifications():
    context = {
        'segment': 'notifications'
    }
    return render_template('pages/notifications.html', **context)

@blueprint.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        address = request.form.get('address')
        bio = request.form.get('bio')

        current_user.first_name = first_name
        current_user.last_name = last_name
        current_user.address = address
        current_user.bio = bio

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()

        return redirect(url_for('home_blueprint.profile'))

    return render_template('pages/profile.html', segment='profile')
@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
