from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url('', TemplateView.as_view(template_name='index.html')),
]
