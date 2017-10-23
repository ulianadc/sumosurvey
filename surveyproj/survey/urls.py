from django.conf.urls import url

from . import views

app_name = 'survey'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^manage$', views.manage_index, name='manage/index'),
    # url(r'^manage/(?P<question_id>[0-9]+)/edit$', views.manage_edit, name='manage/edit'),
    url(r'^manage/new$', views.manage_new, name='manage/new'),
]
