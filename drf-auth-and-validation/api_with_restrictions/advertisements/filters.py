from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    id = filters.ModelMultipleChoiceFilter(
        field_name="id",
        to_field_name="id",
        queryset=Advertisement.objects.all()
    )
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ["id", "title", "description", "creator", "status", "created_at"]
