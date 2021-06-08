from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


# Register your models here.

@admin.register(Web)
class WebAdmin(ImportExportModelAdmin):
    pass


@admin.register(DIY_FYI)
class DIY_FYIAdmin(ImportExportModelAdmin):
    pass

@admin.register(Sponsors)
class sponsorsAdmin(ImportExportModelAdmin):
    pass

@admin.register(Emails)
class emailsAdmin(ImportExportModelAdmin):
    pass

@admin.register(Gallery)
class GalleryAdmin(ImportExportModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    pass