from django.contrib import admin
from .models import Author,Book,Review,Rating
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name',)


class BookAdmin(admin.ModelAdmin):
    list_display=('author','title')
    list_filter=('title',)
    search_fields=('title',)
    sortable_by=('title',)


class ReviewAdmin(admin.ModelAdmin):
    list_display=('comment',)


class RatingAdmin(admin.ModelAdmin):
    list_display=('stars',)


admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Rating,RatingAdmin)
