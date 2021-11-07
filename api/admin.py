from django.contrib import admin
from .models import Student, Feedback, State, Standard, Country, Place, Parent, Location, Certification, Goal, School, Staff

# customize models
class StudenModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'sex')
    search_fields = ['name']
    list_filter = ('age', 'sex')

class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'standard', 'feedback')
    search_fields = ['name__name', 'feedback']  # __name cz name is relation to student
    list_filter = ('standard',)


# Register your models here.
myModels = [State, Standard, Country, Location, Place, School, Certification, Goal, Parent, Staff]
admin.site.register(myModels)
admin.site.register(Student, StudenModelAdmin)
admin.site.register(Feedback, FeedbackModelAdmin)