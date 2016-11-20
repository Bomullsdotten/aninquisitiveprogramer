import sqlalchemy
from ..models.blog_post import BlogPost


class BlogPostService(object):
    @classmethod
    def all(cls, request):
        query = request.dbsession.query(BlogPost)
        return query.order_by(sqlalchemy.desc(BlogPost.created))

    @classmethod
    def by_id(cls, _id, request):
        query = request.dbsession.query(BlogPost)
        return query.get(_id)
