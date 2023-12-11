from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from .models import Account
from .serializers import AccountSerializer
import serializers


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(account_number=self.request.GET.get('account_number'))
        return queryset

    @action(detail=True, methods=['post'])
    def update(self, request, pk=None):
        account = self.get_object()
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            raise serializers.ValidationError(serializer.errors)
