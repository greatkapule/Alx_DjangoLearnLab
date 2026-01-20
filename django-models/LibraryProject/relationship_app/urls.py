from django.urls import path
from .views import admin_view, librarian_view, member_view
# ... keep your existing imports ...

urlpatterns = [
    # ... keep your existing paths ...
    path('admin_view/', admin_view, name='admin_view'),
    path('librarian_view/', librarian_view, name='librarian_view'),
    path('member_view/', member_view, name='member_view'),
]