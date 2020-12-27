from django.contrib import admin

# Register your models here.
from .models import Question,Choices

admin.site.site_header = "Pollster admin"
admin.site.site_title = 'Pollster admin area'
admin.site.index_title = 'Welcome to the pollster admin'

# admin.site.register(Question)
# admin.site.register(Choices)

class ChoicesInline(admin.TabularInline):
    model = Choices
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['question']}),('Date Information',{'fields':['pub_date'],'classes':['collapse']}),]
    inlines=[ChoicesInline]


admin.site.register(Question,QuestionAdmin)