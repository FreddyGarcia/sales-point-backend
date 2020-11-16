from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(self, user):
        token = super().get_token(user)

        request = self.context["request"]

        company_id = request.POST.get('company_id')

        if company_id is None:
            raise Exception('company_id required')

        # Add custom claims
        token['firstname'] = user.first_name
        token['lastname'] = user.last_name
        token['email'] = user.email
        token['company'] = company_id
        return token


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
