# payment_API
Cette API de paiement mobile offre une solution complète et sécurisée pour les transactions financières. Elle permet aux utilisateurs d'effectuer des paiements en toute simplicité, de gérer leurs comptes de manière autonome et d'intégrer les avantages de la blockchain pour une validation transparente des transactions.

# Mobile Payment API with Blockchain Integration

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)  
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)  
[![Django](https://img.shields.io/badge/Django-4.2%2B-green)](https://www.djangoproject.com/)  
[![DRF](https://img.shields.io/badge/Django%20Rest%20Framework-3.14%2B-orange)](https://www.django-rest-framework.org/)

Une API de paiement mobile moderne, sécurisée et scalable, conçue pour gérer les transactions, les recharges, et l'intégration de la blockchain pour la validation des transactions.

---

## **Fonctionnalités**

- **Authentification sécurisée** : Utilisation de JWT (JSON Web Tokens) pour l'authentification des utilisateurs.
- **Gestion des transactions** :
  - Transferts entre utilisateurs.
  - Recharges via Stripe.
  - Historique des transactions.
- **Intégration blockchain** :
  - Validation des transactions via des smart contracts.
  - Utilisation de Web3.js/Web3.py pour interagir avec la blockchain.
- **Gestion des bénéficiaires** :
  - Ajout, suppression, et consultation des bénéficiaires.
- **Chatbot intelligent** :
  - Assistance utilisateur via un chatbot intégré (Gemini AI ou autre).
- **Sécurité renforcée** :
  - Chiffrement des données sensibles.
  - Rate limiting pour prévenir les abus.
  - Validation des entrées utilisateur.

---

## **Technologies utilisées**

- **Backend** : Django, Django Rest Framework (DRF)
- **Base de données** : PostgreSQL (ou SQLite pour le développement)
- **Authentification** : JWT (JSON Web Tokens)
- **Blockchain** : Ethereum (ou autre blockchain compatible avec Web3.js/Web3.py)
- **Paiements** : Stripe pour les recharges
- **Chatbot** : Gemini AI (Google)
- **Conteneurisation** : Docker
- **Tests** : Pytest, Unittest
- **Documentation** : Swagger/OpenAPI

---

## **Installation**

### **Prérequis**
- Python 3.9+
- Docker (optionnel)
- Compte Stripe (pour les recharges)
- Compte Gemini AI (pour le chatbot)

### **Étapes d'installation**

1. **Cloner le repository** :
   ```bash
   git clone https://github.com/ton-username/payment_API.git
   cd payment_API
   ```

2. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurer les variables d'environnement** :
   Créer un fichier `.env` à la racine du projet avec le contenu suivant :
   ```env
   SECRET_KEY=ta_clé_secrète_django
   DATABASE_URL=postgres://user:password@localhost:5432/mobile_payment
   STRIPE_SECRET_KEY=ta_clé_secrète_stripe
   GEMINI_API_KEY=ta_clé_api_gemini
   BLOCKCHAIN_NODE_URL=https://mainnet.infura.io/v3/projet_id
   ```

4. **Appliquer les migrations** :
   ```bash
   python manage.py migrate
   ```

5. **Démarrer le serveur** :
   ```bash
   python manage.py runserver
   ```

---

## **Endpoints API**

| Méthode | Endpoint              | Description                                   |
|----------|-----------------------|-----------------------------------------------|
| POST     | `/api/auth/register/` | Inscription d'un nouvel utilisateur.         |
| POST     | `/api/auth/login/`    | Connexion et obtention d'un JWT.             |
| POST     | `/api/transfer/`      | Effectuer un transfert.                      |
| GET      | `/api/transactions/`  | Historique des transactions.                 |
| POST     | `/api/stripe-payment/`| Recharger son compte via Stripe.             |
| POST     | `/api/chatbot/`       | Interagir avec le chatbot.                   |

---

## **Documentation API**

Accédez à la documentation Swagger en visitant :

[http://localhost:8000/swagger/](http://localhost:8000/swagger/)

---

## **Tests**

Lancer les tests unitaires :
```bash
python manage.py test
```

---

## **Contribuer**

1. Forkez le projet.
2. Créez une branche pour votre fonctionnalité :
   ```bash
   git checkout -b nouvelle-fonctionnalite
   ```
3. Soumettez une pull request.

---

## **Licence**

Ce projet est sous licence [MIT](https://opensource.org/licenses/MIT).

---

## **Auteur**

Projet développé par omgba louis david.

---

## **Prochaines étapes**

1. Créer un repository sur GitHub.
2. Copier ce fichier README.md dans le repository.
3. Structurer le projet en suivant la roadmap ci-dessus.

