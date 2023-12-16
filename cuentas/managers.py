from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def crear_usuario(self, email, nombre_completo, contraseña):
        if not email:
            raise ValueError('Correo electronico obligatorio')
        if not nombre_completo:
            raise ValueError('Nombre obligatorio')
        
        user = self.model(email=self.normalize_email(email), nombre_completo=nombre_completo)
        user.set_password(contraseña)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, email, nombre_completo, contraseña):
        user = self.crear_usuario(email, nombre_completo, contraseña)
        user.is_admin = True
        user.save(using=self.db)
        return user