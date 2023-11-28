from django.contrib import admin
from .models import Articles
from .models import edu
from .models import award

admin.site.register(Articles)
admin.site.register(edu)
admin.site.register(award)
# Register your models here.
