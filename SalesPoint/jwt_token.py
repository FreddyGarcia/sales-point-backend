from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from core.models import Company

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(self, user):
        token = super().get_token(user)

        request = self.context["request"]

        company_id = request.data.get('company_id')

        if company_id is None:
            raise Exception('company_id required')

        if not Company.api_objects.filter(id=company_id).exists():
            raise Exception('Invalid company')

        # Add custom claims
        token['firstname'] = user.first_name
        token['lastname'] = user.last_name
        token['email'] = user.email
        token['company'] = company_id
        return token


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
