from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound
)

from pyramid.httpexceptions import HTTPFound

from pyramid.security import remember
from pyramid.security import forget

from ..models import User, BlogPost
from ..actions.blog_post import BlogPostService
from ..actions.user import UserQueries


@view_config(route_name='home', renderer='blog:templates/index.jinja2')
def home(request):
    page = int(request.params.get('page', 1))
    paginator = BlogPostService.get_paginator(request, page)
    return dict(
        title='Home',
        paginator=paginator
    )


@view_config(route_name='login', renderer='blog:templates/login.jinja2',
             request_method=['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            user = UserQueries.by_name(username, request=request)
            if user and user.check_password(request.POST.get('password')):
                headers = remember(request, user.name)
            else:
                headers =  forget(request)
        else:
            headers = forget(request)

        return HTTPFound(location=request.route_url('home'), headers=headers)
    elif request.method == 'GET':
        return {}


@view_config(route_name='logout', renderer='string')
def logout(request):
    headers = forget(request)
    return HTTPFound(location=request.route_url('home'), headers=headers)

