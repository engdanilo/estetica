from django.db import models

class Base(models.Model):
    
    created = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Modified', auto_now=True)
    active = models.BooleanField('Active', default=True)
    
    class Meta:
        abstract = True
        
        
class SiteData(Base):
    
    title = models.CharField('Title', max_length=200)
    logo = models.CharField('Logo', max_length=1000)
    name = models.CharField('Name', max_length=100)
    site_description = models.TextField('Description')
    email = models.CharField('Email', max_length=100)
    instagram = models.CharField('Instagram', max_length=200)
    instagram_nick = models.CharField('Instagram @', max_length=50)
    phone = models.CharField('Phone', max_length=30)
    whatsapp = models.CharField('Link_whatsapp', max_length=100, default='https://wa.me/')
    keywords = models.TextField('Keywords')
    img_hero = models.CharField('Image1', max_length=1000)
    
    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Infos'
    
    
class Services(Base):
    
    service_name = models.CharField('Service_name', max_length=200)
    img_service = models.CharField('Image_service', max_length=1000)
    service_text = models.TextField('Service')
    benefits = models.TextField('Benefits')
    routines = models.TextField('Routines')
    warnings = models.TextField('Warnings')
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    
class Testemonials(Base):
    
    customer_name = models.CharField('Customer_name', max_length=100)
    profession = models.CharField('Profession', max_length=100)
    testemonial = models.TextField('Testemonial', max_length=1500)
    img_customer = models.CharField('Customer_img', max_length=1000)
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    
    
class FAQ(Base):
    
    question = models.CharField('Question', max_length=200)
    answer = models.TextField('Answer')
    
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'