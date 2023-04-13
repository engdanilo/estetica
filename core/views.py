from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import SiteData, Services, Testemonials, FAQ


class IndexView(TemplateView):
    template_name = 'index.html'
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['site_info'] = SiteData.objects.order_by().all()
        context['service'] = Services.objects.order_by('?').all()
        context['testemonial_random'] = Testemonials.objects.order_by('?').all()
        context['faq_random'] = FAQ.objects.order_by('?').all()
        return context
   
        
class SitemapView(TemplateView):
    template_name='sitemap.xml'
        

class RobotsView(TemplateView):
    template_name='robots.txt'
    

class BingView(TemplateView):
    template_name = 'BingSiteAuth.xml'