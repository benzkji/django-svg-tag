from django.conf.urls import url

from test_app.views import SVGView


urlpatterns = [
    url(r'^', SVGView.as_view(), name='svg_test'),
]
