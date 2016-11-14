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

