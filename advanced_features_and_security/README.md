## Permissions and Groups Setup

This application uses Django permissions and groups to control access.

### Custom Permissions
Defined in the Book model:
- can_view
- can_create
- can_edit
- can_delete

### Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

### Enforcement
Permissions are enforced in views using Django's @permission_required decorator.
