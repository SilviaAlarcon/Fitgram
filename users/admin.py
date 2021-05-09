#User admin classes 

#Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin #combinar datos de profile y user 
from django.contrib import admin

#Models
from django.contrib.auth.models import User
from users.models import Profile

#Register your models here.
#by convention 'admin' is always added to the class name
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #order in which the data will be presented
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    #generates links in user and pk that take us to the profile details
    list_display_link = ('pk', 'user')
    #To edit data without entering the profile
    list_editable = ('phone_number', 'website', 'picture')
    #add_search fields
    search_fields = (
        'user__username', 
        'user__first_name', 
        'user__last_name', 
        'user__email', 
        'phone_number'
    )
    #add_a table with different filters on the creation and modification of data
    list_filter = (
        'created', 
        'modified',
        'user__is_active',
        'user__is_staff'
    )
    #fieldsets receives two elements, a title that can be "none" and a dictionary
    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),) #esto pone los datos en direntes renglones, para ponerlos en columnas sería (('user', 'picture'),)
        }),

        ('Extra info', {
            'fields':(
                ('phone_number', 'website'),
                ('biography')
            )
        }),

        ('Metadata', {
            'fields': (('created', 'modified'),)
        }),

    )

    readonly_fields = ('created', 'modified')

#Para agregar los campos de profile a user 
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

#Add_ profile admin to base user admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username', 
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)