from flask_combo_jsonapi import ResourceList, ResourceDetail
from combojsonapi.event.resource import EventsResource
from blog.extensions import db
from blog.models import Article
from blog.schemas import ArticleSchema
from urllib import request
import requests


class ArticleListEvent(EventsResource):
    def event_get_count(self, **kwargs):
        return {'count': Article.query.count()}

    def event_get_api_server(self, **kwargs):
        return {'count': requests.get('https://ipconfig.io/ip').text}


class ArticleDeteilEvent(EventsResource):
    def event_get_count_by_author(self, **kwargs):
        return {'method': Article.query.filter(Article.author_id == kwargs['id']).count()}


class ArticleList(ResourceList):
    events = ArticleListEvent
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }


class ArticleDetail(ResourceDetail):
    events = ArticleDeteilEvent
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }
