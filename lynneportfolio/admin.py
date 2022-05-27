from django.contrib import admin
from .models import Certifications, Editor,Project,Skills

# Register your models here.

admin.site.register(Editor)
admin.site.register(Project)
admin.site.register(Skills)
admin.site.register(Certifications)

