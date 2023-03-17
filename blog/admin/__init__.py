def register_views():
    from blog.extensions import admin, db
    from blog import models
    from blog.admin.views import TagAdminView, ArticleAdminView, UserAdmin

    admin.add_view(TagAdminView(models.Tag, db.session, category="Models"))
    admin.add_view(ArticleAdminView(models.Article, db.session, category="Models"))
    admin.add_view(UserAdmin(models.User, db.session, category="Models"))
