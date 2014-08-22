from django.conf.urls import pattern, url

urlpatterns = patterns('jtweet.jtweetapp.views',
  url(r'^', 'index', name = 'index'),
)
