# coding: utf-8

from .. import db
from ..models import Role, User

def get_role_names():
    roles = Role.query.all()
    return [role.name for role in roles]