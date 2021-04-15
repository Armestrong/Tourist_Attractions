def disapproved_comments(modeladmin, request, queryset):
    queryset.update(approved=False)


def approved_comments(modeladmin, request, queryset):
    queryset.update(approved=True)


disapproved_comments.short_description = 'disapproved comments'
approved_comments.short_description = 'approved comments'
