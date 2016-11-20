from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound
)

from ..models import User, BlogPost
from ..actions.blog_post import BlogPostService

@view_config(route_name='home', renderer='blog:templates/index.jinja2')
def home(request):
    page = int(request.params.get('page', 1))
    paginator = BlogPostService.get_paginator(request, page)
    return dict(
        title='Home',
        paginator=paginator
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

