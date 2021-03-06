import uuid

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api_yamdb.settings import EMAIL_ADMIN

from .models import UserProfile
from .permissions import IsAdmin
from .serializers import (EmailConfirmSerializer, TokenSerializer,
                          UserSerializer)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def email_confirmation(request):
    user_code = uuid.uuid4()
    serializer = EmailConfirmSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data['email']
    user = get_object_or_404(UserProfile, email=email)
    if user:
        user.user_code = user_code
        user.save()
        send_mail(
            'Код подтверждения',
            f'Ваш код подтверждения: {user_code}',
            EMAIL_ADMIN,
            (email,),
            fail_silently=False
        )
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return None


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def get_token(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data['email']
    user_code = serializer.validated_data['user_code']
    user = get_object_or_404(
        UserProfile,
        email=email,
        user_code=user_code,
    )
    if not user:
        return Response(
            serializer.errors, status=status.HTTP_404_NOT_FOUND
        )
    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)
    return Response({'token': token})


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsAdmin,)

    @action(detail=False, methods=['get', 'patch'], url_path='me',
            permission_classes=[permissions.IsAuthenticated])
    def user_profile(self, request):
        if request.method == 'GET':
            serializer = self.get_serializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PATCH':
            serializer = self.get_serializer(
                request.user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return None
