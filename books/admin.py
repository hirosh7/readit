from django.contrib import admin
from .models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Book Detail", {"fields": ["title", "authors"]}),
        ("Review", {"fields": ["is_favorite", "review", "date_reviewed"]})
    ]

    readonly_fields = ("date_reviewed",)

    def book_authors(self, obj):
        return obj.list_authors()

    book_authors.short_description = "Author(s)"
    list_editable = ("is_favorite",)
    list_filter = ("is_favorite",)
    search_fields = ("title", "authors__name",)

    list_display = ("title", "book_authors", "date_reviewed", "is_favorite",)

# Register your models here.
admin.site.register(Author)
