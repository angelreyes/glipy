from rest_framework import serializers
from coa.models import Account


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('accno', 'description',)
