from django_auth_ldap.backend import LDAPBackend

#change default behaviour of LDAPBackend
#remove doamin, if UPN is used

class CustomLDAPBackend(LDAPBackend):
    def ldap_to_django_username(self, username):
        user = username.split("@")[0]
        return user
