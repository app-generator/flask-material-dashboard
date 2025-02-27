# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import wtforms
from apps.home import blueprint
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from jinja2 import TemplateNotFound
from flask_login import login_required, current_user
from apps import db, config
from apps.models import *
from apps.tasks import *
from apps.authentication.models import Users
from flask_wtf import FlaskForm

@blueprint.route('/')
@blueprint.route('/index')
def index():
    context = {
        'segment': 'dashboard',
        'parent': 'dashboard',
        'title':'HOME'
    }    
    return render_template('pages/index.html', segment='dashboard', parent='dashboard')

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

@blueprint.route('/icons')
def icons():
    context = {
        'segment': 'icons'
    }
    return render_template('pages/icons.html', **context)


@blueprint.route('/map')
def map():
    context = {
        'segment': 'map'
    }
    return render_template('pages/map.html', **context)

@blueprint.route('/typography')
def typography():
    context = {
        'segment': 'typography'
    }
    return render_template('pages/typography.html', **context)

@blueprint.route('/template')
def template():
    context = {
        'segment': 'template'
    }
    return render_template('pages/template.html', **context)


@blueprint.route('/landing')
def landing():
    context = {
        'segment': 'landing'
    }
    return render_template('pages/landing.html', **context)


def getField(column): 
    if isinstance(column.type, db.Text):
        return wtforms.TextAreaField(column.name.title())
    if isinstance(column.type, db.String):
        return wtforms.StringField(column.name.title())
    if isinstance(column.type, db.Boolean):
        return wtforms.BooleanField(column.name.title())
    if isinstance(column.type, db.Integer):
        return wtforms.IntegerField(column.name.title())
    if isinstance(column.type, db.Float):
        return wtforms.DecimalField(column.name.title())
    if isinstance(column.type, db.LargeBinary):
        return wtforms.HiddenField(column.name.title())
    return wtforms.StringField(column.name.title()) 


@blueprint.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():

    class ProfileForm(FlaskForm):
        pass

    readonly_fields = Users.readonly_fields
    full_width_fields = {"bio"}

    for column in Users.__table__.columns:
        if column.name == "id":
            continue

        field_name = column.name
        if field_name in full_width_fields:
            continue

        field = getField(column)
        setattr(ProfileForm, field_name, field)

    for field_name in full_width_fields:
        if field_name in Users.__table__.columns:
            column = Users.__table__.columns[field_name]
            field = getField(column)
            setattr(ProfileForm, field_name, field)

    form = ProfileForm(obj=current_user)

    if form.validate_on_submit():
        readonly_fields.append("password")
        excluded_fields = readonly_fields
        for field_name, field_value in form.data.items():
            if field_name not in excluded_fields:
                setattr(current_user, field_name, field_value)

        db.session.commit()
        return redirect(url_for('home_blueprint.profile'))
    
    context = {
        'segment': 'profile',
        'form': form,
        'readonly_fields': readonly_fields,
        'full_width_fields': full_width_fields,
    }
    return render_template('pages/profile.html', **context)



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



# Custom template filter

@blueprint.app_template_filter("replace_value")
def replace_value(value, arg):
    return value.replace(arg, " ").title()