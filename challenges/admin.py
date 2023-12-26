from django.contrib import admin
from .models import Exercise, Challenge, Submit

class ChallengeAdmin(admin.ModelAdmin):
    fieldsets = [
        ("基本情報", {"fields": ["identifier", "title", "exerciseName", "category", "score", "flag", "visible"]}),
        ("問題文", {"fields": ["problem"]}),
        ("ヒント", {"fields": ["hint_one", "hint_two", "hint_three"]}),
        ("その他情報", {"fields": ["cleared_counts", "created_at", "updated_at"]}),
    ]
    list_display = ["title", "exerciseName", "score", "visible"]
    list_filter = ["exerciseName", "visible"]
    search_fields = ["title", "exerciseName", "score", "visible"]
    ordering = ["title", "exerciseName", ]
    list_per_page = 20
    readonly_fields = ["cleared_counts", "created_at", "updated_at"]
    
class ExerciseAdmin(admin.ModelAdmin):
    fieldsets = [
        ("基本情報", {"fields": ["exercise", "category", "visible"]}),
        ("演習の説明", {"fields": ["disription"]}),
        ("教科書・解説URL", {"fields": ["reference_url" , "explanation_url"]}),
        ("その他情報", {"fields": ["created_at", "updated_at"]}),
    ]
    list_display = ["exercise", "category", "visible"]
    list_filter = ["exercise", "visible"]
    search_fields = ["exercise"]
    ordering = ["exercise", ]
    readonly_fields = [ "created_at", "updated_at"]
    
class SubmitAdmin(admin.ModelAdmin):
    readonly_fields = [ "user", "identifier"]
    

admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Submit, SubmitAdmin)