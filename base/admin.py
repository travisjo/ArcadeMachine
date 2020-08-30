from django.contrib import admin

from .models import HighScore, Game, Machine


admin.site.register(HighScore)
admin.site.register(Game)
admin.site.register(Machine)
