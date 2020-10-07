from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Email is compulsory')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password=password)
        user.save()
        return user
