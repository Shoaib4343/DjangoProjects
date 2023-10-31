from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, phone, passweord=None, **extra_fields):
        if phone is None:
            raise ValueError("Phone field cannot be empty")
        extra_fields['email'] = self.normalize_email(extra_fields.get('email', ''))
        user = self.model(phone=phone, **extra_fields)
        user.set_password(passweord)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)   

        return self.create_user(phone, password, **extra_fields)     