from django.contrib import admin

from notes.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "text_preview", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("text",)

    def text_preview(self, obj):
        return obj.text[:50] + ("..." if len(obj.text) > 50 else "")

    text_preview.short_description = "Text"
