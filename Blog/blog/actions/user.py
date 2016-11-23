from ..models.user import User

class UserQueries(object):
    @classmethod
    def by_name(cls, name, request):
        return request.dbsession.query(User).filter(User.name == name).first()