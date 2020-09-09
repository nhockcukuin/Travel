import django_filters
from django_filters import CharFilter
from django import forms
from.models import *

class PostFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr="icontains")
    #category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(),widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Posts
        fields = ['title','category']