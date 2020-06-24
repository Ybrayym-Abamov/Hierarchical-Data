from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from hierarchical.models import Hierarchy

# Register your models here.
admin.site.register(Hierarchy, DraggableMPTTAdmin)
