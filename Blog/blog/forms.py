import wtforms as wtf


strip_filter = lambda x: x.strip() if x else None


class BlogCreateForm(wtf.Form):
    title = wtf.StringField('Title', [wtf.validators.Length(min=1, max=255)],
                            filters=[strip_filter])
    body = wtf.TextAreaField('Content', [wtf.validators.Length(min=1)],
                             filters=[strip_filter])


class BlogUpdateForm(BlogCreateForm):
    id = wtf.HiddenField

