from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['firstname'] = user.first_name
        token['lastname'] = user.last_name
        token['email'] = user.email

        return token


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
