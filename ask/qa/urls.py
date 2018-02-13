from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
	url(r'^login/', views.test, name='test'),
    url(r'^signup/', views.test, name='test'),
    url(r'^ask/', views.ask_question, name='ask'),
    url(r'^popular/', views.home,{'current': 'popular'}, name='popular'),
    url(r'^new/', views.test, name='test'),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
]
