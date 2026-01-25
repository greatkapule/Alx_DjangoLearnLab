# Managing Permissions and Groups in Django

This project implements role-based access control using Django permissions and groups.

## Custom Permissions
The following custom permissions are defined in the Book model:
- can_view
- can_create
- can_edit
- can_delete

## Groups Configuration
The following groups are used:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

## Permission Enforcement
Access control is enforced in views using Django's permission_required decorator.
Only users with the appropriate permissions can view, create, edit, or delete books.
