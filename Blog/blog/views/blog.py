from pyramid.view import view_config

from pyramid.httpexceptions import  HTTPNotFound
from pyramid.httpexceptions import HTTPFound

from ..models.blog_post import BlogPost
from ..actions.blog_post import BlogPostService


@view_config(route_name='blog',
             renderer='blog:templates/view_blog.jinja2')
def view_blog(request):
    blog_id = int(request.matchdict.get('id', -1))
    entry = BlogPostService.by_id(blog_id, request)

    if not entry:
        return HTTPNotFound()
    return dict(
        entry=entry
    )

