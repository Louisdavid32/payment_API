from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Pour ne pas renvoyer le mot de passe dans la réponse

    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'password', 'nom', 'prenom', 'ville', 'adresse',
            'numero_telephone', 'emploi', 'employeur', 'iban', 'bic', 'image',
            'is_verified', 'verification_code', 'verification_code_expires_at',
            'date_joined', 'last_updated'
        ]
        extra_kwargs = {
            'password': {'write_only': True},  # Masquer le mot de passe dans les réponses
            'verification_code': {'write_only': True},  # Masquer le code de vérification
            'verification_code_expires_at': {'write_only': True},  # Masquer la date d'expiration du code
        }

    def create(self, validated_data):
        # Créer un utilisateur avec un mot de passe hashé
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            nom=validated_data.get('nom', ''),
            prenom=validated_data.get('prenom', ''),
            ville=validated_data.get('ville', ''),
            adresse=validated_data.get('adresse', ''),
            numero_telephone=validated_data.get('numero_telephone', ''),
            emploi=validated_data.get('emploi', ''),
            employeur=validated_data.get('employeur', ''),
            iban=validated_data.get('iban', ''),
            bic=validated_data.get('bic', ''),
            image=validated_data.get('image', None),
        )
        return user

    def update(self, instance, validated_data):
        # Mettre à jour les champs de l'utilisateur
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.nom = validated_data.get('nom', instance.nom)
        instance.prenom = validated_data.get('prenom', instance.prenom)
        instance.ville = validated_data.get('ville', instance.ville)
        instance.adresse = validated_data.get('adresse', instance.adresse)
        instance.numero_telephone = validated_data.get('numero_telephone', instance.numero_telephone)
        instance.emploi = validated_data.get('emploi', instance.emploi)
        instance.employeur = validated_data.get('employeur', instance.employeur)
        instance.iban = validated_data.get('iban', instance.iban)
        instance.bic = validated_data.get('bic', instance.bic)
        instance.image = validated_data.get('image', instance.image)

        # Mettre à jour le mot de passe si fourni
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])

        instance.save()
        return instance