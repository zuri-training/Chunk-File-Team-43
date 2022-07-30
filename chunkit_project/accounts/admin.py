from django.contrib import admin
from .models import chunkit_users
from .models import authentication
from .models import Chunkedfile

# Register your models here.
admin.site.register(chunkit_users)
admin.site.register(authentication)
admin.site.register(Chunkedfile)