from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound
)

from ..models import User, BlogPost


@view_config(route_name='home', renderer='blog:templates/index.jinja2')
def home(request):
    return dict(
        title='Home',
        project='Blog'
    )


@view_config(route_name='blog_action', match_param='action=edit',
             renderer='blog:templates/edit_blog.jinja2')
def blog_update(request):
    return {}


@view_config(route_name='blog_action', match_param='action=create',
             renderer='blog:templates/edit_blog.jinja2')
def blog_create(request):
    return {}


@view_config(route_name='login', renderer='blog:templates/login.jinja2',
             request_method='POST')
def login(request):
    return {}


@view_config(route_name='logout', renderer='string')
def logout(request):
    return {}


@view_config(route_name='blog', renderer='blog:templates/view_blog.jinja2')
def view_blog(request):
    return {}

