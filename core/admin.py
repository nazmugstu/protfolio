from django.contrib import admin
from .models import ContactMessage, Skill, Project, ProjectImage, Technology

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3

class TechnologyInline(admin.TabularInline):
    model = Project.technologies.through
    extra = 1

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_replied', 'created_at']
    list_filter = ['created_at', 'is_replied']
    search_fields = ['name', 'email', 'message']
    actions = ['mark_as_replied']
    readonly_fields = ['created_at']

    def mark_as_replied(self, request, queryset):
        queryset.update(reply="Thank you for your message!", is_replied=True)
    mark_as_replied.short_description = "Mark selected messages as replied"

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'proficiency', 'icon']
    search_fields = ['name']
    list_editable = ['proficiency']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'has_live_demo']
    list_filter = ['created_at']
    search_fields = ['title', 'description']
    inlines = [ProjectImageInline, TechnologyInline]
    exclude = ['technologies']
    
    def has_live_demo(self, obj):
        return bool(obj.live_demo)
    has_live_demo.boolean = True
    has_live_demo.short_description = 'Live Demo'

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['project', 'caption']
    list_filter = ['project']
    search_fields = ['project__title', 'caption']