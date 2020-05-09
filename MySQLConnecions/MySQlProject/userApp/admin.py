from django.contrib import admin
from userApp.models import Details
# Register your models here.
admin.site.register(Details)
admin.site.site_title='my login page'
admin.site.site_header = 'my DJango Page'
admin.site.index_title='index title'