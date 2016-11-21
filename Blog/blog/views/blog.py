from pyramid.view import view_config

from pyramid.httpexceptions import  HTTPNotFound
from pyramid.httpexceptions import HTTPFound

from ..models.blog_post import BlogPost
from ..actions.blog_post import BlogPostService
from ..forms import BlogCreateForm
from ..forms import BlogUpdateForm


@view_config(route_name='blog_action', match_param='action=create',
             renderer='blog:templates/edit_blog.jinja2')
def blog_create(request):
    entry = BlogPost()
    form = BlogCreateForm(request.POST)
    if validate_form_request(request, form):
        form.populate_obj(entry)
        request.dbsession.add(entry)
        return HTTPFound(location=request.route_url('home'))

    return dict(
        form=form,
        action=request.matchdict.get('action')
    )


@view_config(route_name='blog_action', match_param='action=edit',
             renderer='blog:templates/edit_blog.jinja2')
def blog_update(request):
    blog_id = int(request.params.get('id', -1))
    blog_post = BlogPostService.by_id(blog_id, request)
    if not blog_post:
        return HTTPNotFound()
    form = BlogUpdateForm(request.POST, blog_post)
    if validate_form_request(request, form):
        form.populate_obj(blog_post)
        return HTTPFound(location=request.route_url('blog', id=blog_post.id, slug=blog_post.slug))

    return dict(
        form=form,
        action=request.matchdict.get('action')
    )



@view_config(route_name='blog',
             renderer='blog:templates/view_blog.jinja2')
def view_blog(request):
    blog_id = int(request.matchdict.get('id', -1))
    post = BlogPostService.by_id(blog_id, request)

    if not post:
        return HTTPNotFound()
    return dict(
        post=post
    )

def validate_form_request(request, form):
    if request.method == 'POST' and form.validate():
        return True

    return False