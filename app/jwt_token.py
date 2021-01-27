from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.crm.models import Company
from django.contrib.auth.models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(self, user):
        token = super().get_token(user)

        request = self.context["request"]
        company_id = request.data.get('company')

        # Add custom claims
        token['firstname'] = user.first_name
        token['lastname'] = user.last_name
        token['email'] = user.email
        token['company'] = company_id

        if user.is_superuser:
            return token

        if company_id is None:
            raise Exception('company_id required')

        if not Company.active.filter(id=company_id).exists():
            raise Exception('Invalid company')

        return token


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
