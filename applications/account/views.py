from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

from applications.account.serializers import RegisterSerializer

User = get_user_model()

class UserRegisterApiview(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    


