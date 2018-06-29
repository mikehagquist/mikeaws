{"filter":false,"title":"admin.py","tooltip":"/Projects/myauthemail/admin.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.contrib import admin","","# Register your models here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":28,"column":25},"action":"insert","lines":["\"\"\"Integrate with admin module.\"\"\"","","from django.contrib import admin","from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin","from django.utils.translation import ugettext_lazy as _","","from .models import User","","","@admin.register(User)","class UserAdmin(DjangoUserAdmin):","    \"\"\"Define admin model for custom User model with no email field.\"\"\"","","    fieldsets = (","        (None, {'fields': ('email', 'password')}),","        (_('Personal info'), {'fields': ('first_name', 'last_name')}),","        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',","                                       'groups', 'user_permissions')}),","        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),","    )","    add_fieldsets = (","        (None, {","            'classes': ('wide',),","            'fields': ('email', 'password1', 'password2'),","        }),","    )","    list_display = ('email', 'first_name', 'last_name', 'is_staff')","    search_fields = ('email', 'first_name', 'last_name')","    ordering = ('email',)"]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["\"\"\"Integrate with admin module.\"\"\"",""],"id":3},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1530212115826,"hash":"0bc816de3ffcbecbdfab0c4f3a8f8d06c5c7c0ed"}