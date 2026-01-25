# Managing Permissions and Groups in Django

This project demonstrates how to manage permissions and groups in Django.

## Custom Permissions
The Book model defines the following permissions:
- can_view
- can_create
- can_edit
- can_delete

## Groups
The following groups are used:
- Viewers
- Editors
- Admins

## Permission Usage
Permissions are enforced in views using the permission_required decorator.
Users must have can_view, can_create, can_edit, or can_delete permissions to access specific views.
