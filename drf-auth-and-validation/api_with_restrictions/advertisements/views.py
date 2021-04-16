from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "patch", "put", "delete"]

    def get_permissions(self):
        """Получение прав для действий."""

        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []

    def destroy(self, request, *args, **kwargs):
        if not request.user.id:
            return Response("Вы не авторизованы", status=status.HTTP_403_FORBIDDEN)
        advertisement = Advertisement.objects.filter(pk=kwargs["pk"]).first()
        if not advertisement:
            raise ValidationError("Такого поста нет!")

        if advertisement.creator.pk != request.user.id:
            raise ValidationError("Вы не являетесь владельцем поста!")
        return super(AdvertisementViewSet, self).destroy(request, *args, **kwargs)
