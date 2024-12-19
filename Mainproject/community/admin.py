from django.contrib import admin
from .models import Contributor, Motive, group, IniatatorGroupContributor

# admin.site.register(Contributor)
admin.site.register(Motive)
admin.site.register(group)
admin.site.register(IniatatorGroupContributor)
