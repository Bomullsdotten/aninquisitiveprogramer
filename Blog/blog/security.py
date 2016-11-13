from passlib.apps import custom_app_context as pwd_context


def hash_password(pwd):
    return pwd_context.encrypt(pwd, category='admin')


def check_password(pwd, expected_hash):
    return pwd_context.verify(pwd, expected_hash)

USERS = {'admin': hash_password('admin')}

GROUPS = {'admin': ['group:editors']}


def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])
