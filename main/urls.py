from django.views.generic import TemplateView
from django.conf.urls import url


app_name = 'main'


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='main/index.html'), name='index'),
]
