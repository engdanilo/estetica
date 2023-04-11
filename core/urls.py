from django.urls import path
from .views import IndexView, SitemapView, RobotsView, BingView


urlpatterns =[
    path('', IndexView.as_view(), name='index'),
    path('sitemap.xml', SitemapView.as_view(), name='sitemap.xml'),
    path('robots.txt', RobotsView.as_view(), name='robots.txt'),
    path('BingSiteAuth.xml', BingView.as_view(), name='BingSiteAuth.xml'),
]