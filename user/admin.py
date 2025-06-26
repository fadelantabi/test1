from django.contrib import admin
from .models import User
from .models import Userinfo
from .models import Review
admin.site.register(User)
admin.site.register(Userinfo)
admin.site.register(Review)