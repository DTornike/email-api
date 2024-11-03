from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Email
from .serializers import EmailSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        user = self.request.user
        return Email.objects.filter(sender=user) | Email.objects.filter(recipients=user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    @action(detail=False, methods=['get'], url_path='sent')
    def sent_emails(self, request):
        user = request.user
        sent_emails = Email.objects.filter(sender=user).order_by('-sent_at')
        serializer = self.get_serializer(sent_emails, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='received')
    def received_emails(self, request):
        user = request.user
        received_emails = Email.objects.filter(recipients=user).order_by('-sent_at')
        serializer = self.get_serializer(received_emails, many=True)
        return Response(serializer.data)
