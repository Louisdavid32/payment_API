from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'email est obligatoire.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Champs personnalisés
    email = models.EmailField(unique=True, verbose_name="Adresse email")
    username = models.CharField(max_length=150, unique=True, verbose_name="Nom d'utilisateur")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True, verbose_name="Photo de profil")
    numero_telephone = models.CharField(
        max_length=15,
        unique=True,
        verbose_name="Numéro de téléphone",
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Le numéro de téléphone doit être au format international. Exemple : +123456789"
            )
        ]
    )
    ville = models.CharField(max_length=100, verbose_name="Ville de résidence")
    adresse = models.CharField(max_length=255, blank=True, null=True, verbose_name="Adresse postale")
    emploi = models.CharField(max_length=100, blank=True, null=True, verbose_name="Profession")
    employeur = models.CharField(max_length=100, blank=True, null=True, verbose_name="Employeur")
    is_verified = models.BooleanField(default=False, verbose_name="Compte vérifié")
    verification_code = models.CharField(max_length=6, blank=True, null=True, verbose_name="Code de vérification")
    verification_code_expires_at = models.DateTimeField(blank=True, null=True, verbose_name="Expiration du code de vérification")
    iban = models.CharField(max_length=34, blank=True, null=True, verbose_name="IBAN")
    bic = models.CharField(max_length=11, blank=True, null=True, verbose_name="BIC")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Date d'inscription")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")

    # Champs requis pour AbstractBaseUser
    is_staff = models.BooleanField(default=False, verbose_name="Accès à l'admin")
    is_superuser = models.BooleanField(default=False, verbose_name="Superutilisateur")

    # Utiliser l'email comme identifiant de connexion
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Champs requis pour créer un superutilisateur

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username} ({self.email})"

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"