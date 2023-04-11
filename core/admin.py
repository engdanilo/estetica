from django.contrib import admin
from .models import SiteData, Services, Testemonials, FAQ


@admin.register(SiteData)
class SiteDataAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'logo',
        'name',
        'site_description',
        'email',
        'instagram',
        'instagram_nick',
        'phone',
        'whatsapp',
        'keywords',
        'img_hero',
        'created',
        'modified',
        'active',
    )


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'service_name',
        'img_service',
        'service_text',
        'benefits',
        'routines',
        'warnings',
        'created',
        'modified',
        'active',
    )
    

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
        'created',
        'modified',
        'active',
    )
    

@admin.register(Testemonials)
class TestemonialsAdmin(admin.ModelAdmin):
    list_display = (
        'customer_name',
        'profession',
        'testemonial',
        'img_customer',
        'created',
        'modified',
        'active',
    )
