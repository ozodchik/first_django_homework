
from rest_framework import serializers

from advertisements.models import Advertisement, User


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        http_methods = ["update", "partial_update"]
        print(self.context["view"].action)

        if self.context["view"].action in http_methods:
            advertisement = Advertisement.objects.get(pk=self.context["view"].kwargs["pk"])
            if not advertisement:
                raise serializers.ValidationError("Не правильное айди поста!")

            if advertisement.creator.pk != self.context["request"].user.id:
                raise serializers.ValidationError("Вы не являетесь владельцем поста!")

        else:
            get_creator_posts = Advertisement.objects.filter(status="OPEN").all()
            if len(get_creator_posts) > 10:
                raise serializers.ValidationError("У вас не может быть более чем 10 открытых обявлений!")

        return data
