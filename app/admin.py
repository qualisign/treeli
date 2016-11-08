from django.contrib import admin

from .models import User, Tree, Trunk, Branch, Twig, Leaf, UserProfile

admin.site.register(Tree)
admin.site.register(Trunk)
admin.site.register(Branch)
admin.site.register(Twig)
admin.site.register(Leaf)
admin.site.register(UserProfile)