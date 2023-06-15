"""

Django Auth Ldap
https://django-auth-ldap.readthedocs.io/en/latest/

Diese Settings müssen in die settings.py kopiert
und entsprechend angepasst werden.

Damit django_auth_ldap funktioniert, muss auch ldap selbst auf dem Client installiert 
werden.

In diesem fiktiven Beispiel gibt es eine Organisation dc=example,dc=com und einen
admin User mit dem Password password123.

Auf dem LDAP Server existieren die Gruppen 
enabled
active
staff
superuser

die mit den Settings des Django-User-Models korrespondieren 
(is_active, is_staff, is_superuser)


AUTH_LDAP_USER_FLAGS_BY_GROUP
------------------------------
hier werden die LDAP-Gruppen auf die spefischen Settings des Usermodels gemappt.
zb.
"is_active": "cn=active+gidNumber=500,ou=groups,dc=example,dc=com",

(CN=commmon name, gidNumber=Group number, ou=organizational unit, dc=Domain components)


AUTH_LDAP_USER_ATTR_MAP
--------------------------
hier werden spezifische LDAP-Settings mit den korrenspondierenden Django-Settings 
gemappt, zb. firstname (Django) und givenName (LDAP)


AUTHENTICATION_BACKENDS
--------------------------
Django kann mit mehreren Authentication Backends arbeiten. Im Beispiel ist ModelBackend
(default) und LDAP Auth Backend aktiv. Weitere Backends (zb. keycloak) wären denkbar.

für weitere Settings siehe Referenz
https://django-auth-ldap.readthedocs.io/en/latest/reference.html

"""
import ldap
from django_auth_ldap.config import (
    LDAPSearch,
    LDAPGroupQuery,
    GroupOfNamesType,
    PosixGroupType,
)

AUTH_LDAP_SERVER_URI = "ldap://192.168.111.40"
AUTH_LDAP_BIND_DN = "cn=admin,dc=example,dc=com"
AUTH_LDAP_BIND_PASSWORD = "password123"
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "dc=example,dc=com", ldap.SCOPE_SUBTREE, "(uid=%(user)s)"
)
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    "dc=example,dc=com", ldap.SCOPE_SUBTREE, "(objectClass=top)"
)
AUTH_LDAP_GROUP_TYPE = PosixGroupType(name_attr="cn")

# wenn eingeloggt, werden alle ldap groups und user unter Django als
# Gruppe angelegt. Kann auch abgeschaltet werden, wenn man dieses Verhalten nicht mag.
AUTH_LDAP_MIRROR_GROUPS = True

# Populate the Django user from the LDAP directory.
AUTH_LDAP_REQUIRE_GROUP = "cn=enabled+gidNumber=501,ou=groups,dc=example,dc=com"

# um User zu blockieren, kann man sie der DENY Gruppe zurordnen.
# Dazu muss die Gruppe disabled auf dem LDAP Server existieren
# AUTH_LDAP_DENY_GROUP = "cn=disabled+gidNumber=504,ou=groups,dc=example,dc=com"

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
    "username": "uid",
    "password": "userPassword",
}
AUTH_LDAP_PROFILE_ATTR_MAP = {"home_directory": "homeDirectory"}
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=active+gidNumber=500,ou=groups,dc=example,dc=com",
    "is_staff": "cn=staff+gidNumber=502,ou=groups,dc=example,dc=com",
    "is_superuser": "cn=superuser+gidNumber=504,ou=groups,dc=example,dc=com",
}

AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_TIMEOUT = 3600

AUTH_LDAP_FIND_GROUP_PERMS = True

# in
# Keep ModelBackend around for per-user permissions and maybe a local
# superuser.
AUTHENTICATION_BACKENDS = (
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",  # <= Default standard
    # 'ldaptest.backend_ldap.CustomLDAPBackend',
)
