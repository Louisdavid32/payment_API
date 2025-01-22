from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import CustomUser
import random
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.utils import timezone



class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Créer l'utilisateur
            user = serializer.save()

            # Générer un code de vérification (exemple : 6 chiffres)
            verification_code = str(random.randint(100000, 999999))
            user.verification_code = verification_code
            user.verification_code_expires_at = timezone.now() + timezone.timedelta(minutes=10)  # Code valide 10 minutes
            user.is_verified = True  # Activer l'utilisateur immédiatement
            user.save()

            # Afficher le code de vérification dans la console (simuler l'envoi par SMS)
            print(f"Code de vérification pour {user.numero_telephone} : {verification_code}")

            return Response({
                'message': 'Inscription réussie. Utilisateur vérifié.',
                'user': UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs.get('email')
        username = attrs.get('username')
        password = attrs.get('password')

        if email:
            # Rechercher l'utilisateur par email
            user = CustomUser.objects.filter(email=email).first()
        elif username:
            # Rechercher l'utilisateur par nom d'utilisateur
            user = CustomUser.objects.filter(username=username).first()
        else:
            raise serializers.ValidationError("L'email ou le nom d'utilisateur est requis.")

        if user and user.check_password(password):
            if not user.is_verified:
                raise serializers.ValidationError("Ce compte n'est pas vérifié.")
            attrs['username'] = user.username  # Utiliser le nom d'utilisateur pour l'authentification
            return super().validate(attrs)
        else:
            raise serializers.ValidationError("Identifiants invalides.")

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer



class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class PasswordResetView(APIView):
    def post(self, request):
        email = request.data.get('email')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({"error": "Aucun utilisateur trouvé avec cet email."}, status=status.HTTP_404_NOT_FOUND)

        # Générer un code de vérification (exemple : 6 chiffres)
        verification_code = str(random.randint(100000, 999999))
        user.verification_code = verification_code
        user.verification_code_expires_at = timezone.now() + timezone.timedelta(minutes=10)  # Code valide 10 minutes
        user.save()

        # Afficher le code de vérification dans la console (simuler l'envoi par SMS)
        print(f"Code de vérification pour {user.numero_telephone} : {verification_code}")

        return Response({
            'message': 'Un code de vérification a été envoyé.',
        }, status=status.HTTP_200_OK)

    def put(self, request):
        email = request.data.get('email')
        code = request.data.get('code')
        new_password = request.data.get('new_password')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({"error": "Aucun utilisateur trouvé avec cet email."}, status=status.HTTP_404_NOT_FOUND)

        # Vérifier le code de vérification
        if user.verification_code != code or user.verification_code_expires_at < timezone.now():
            return Response({"error": "Code de vérification invalide ou expiré."}, status=status.HTTP_400_BAD_REQUEST)

        # Mettre à jour le mot de passe
        user.set_password(new_password)
        user.verification_code = None  # Réinitialiser le code de vérification
        user.verification_code_expires_at = None
        user.save()

        return Response({
            'message': 'Mot de passe réinitialisé avec succès.',
        }, status=status.HTTP_200_OK)
    


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({"error": "Le champ 'refresh' est requis."}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()  # Ajoute le token à la blacklist
            return Response({"message": "Déconnexion réussie."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)