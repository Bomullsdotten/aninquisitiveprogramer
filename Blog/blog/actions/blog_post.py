import sqlalchemy
from ..models.blog_post import BlogPost
from paginate_sqlalchemy import SqlalchemyOrmPage

class BlogPostService(object):
    @classmethod
    def all(cls, request):
        query = request.dbsession.query(BlogPost)
        return query.order_by(sqlalchemy.desc(BlogPost.created))

    @classmethod
    def by_id(cls, _id, request):
        query = request.dbsession.query(BlogPost)
        return query.get(_id)

    @classmethod
    def get_paginator(cls, request, page=1):
        query = request.dbsession.query(BlogPost)
        query = query.order_by(sqlalchemy.desc(BlogPost.created))
        query_params = request.GET.mixed()

        def url_maker(link_page):
            query_params['page'] = link_page
            return request.current_route_url(_query=query_params)

        titels_per_page = 5
        return SqlalchemyOrmPage(query, page, items_per_page=titels_per_page,
                                 url_maker=url_maker)
