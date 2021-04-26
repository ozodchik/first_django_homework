from django_filters import rest_framework as filters

from students.models import Course, Student


class StudentFilter(filters.FilterSet):
    id = filters.ModelMultipleChoiceFilter(
        field_name="id",
        to_field_name="id",
        queryset=Student.objects.all(),
    )

    birth_date = filters.DateFromToRangeFilter()

    class Meta:
        model = Student
        fields = ["id", "name", "birth_date"]


class CourseFilter(filters.FilterSet):

    id = filters.ModelMultipleChoiceFilter(
        field_name="id",
        to_field_name="id",
        queryset=Course.objects.all(),
    )
    name = filters.CharFilter(field_name="name", lookup_expr="iexact")

    class Meta:
        model = Course
        fields = ["id", "name", ]
