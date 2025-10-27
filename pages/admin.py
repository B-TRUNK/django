from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Female)
admin.site.register(Male)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Course)

admin.site.register(Login)


admin.site.site_header = 'Welcome to New Gen'
admin.site.site_title  = 'New Gen'