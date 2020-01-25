from django.contrib import admin

# Register your models here.
from first_app.models import UserProfileInfo,AccessRecord,Topic, Webpage

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(UserProfileInfo)

