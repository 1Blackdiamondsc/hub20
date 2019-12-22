from rest_framework import serializers

from hub20.apps.blockchain.app_settings import CHAIN_ID

from . import models


class TokenValueField(serializers.DecimalField):
    def __init__(self, *args, **kw):
        kw.setdefault("max_digits", 32)
        kw.setdefault("decimal_places", 18)
        super().__init__(*args, **kw)


class CurrencyRelatedField(serializers.SlugRelatedField):
    queryset = models.EthereumToken.objects.filter(chain=CHAIN_ID)

    def __init__(self, *args, **kw):
        kw.setdefault("slug_field", "ticker")
        super().__init__(*args, **kw)


class EthereumTokenSerializer(serializers.ModelSerializer):
    code = serializers.CharField(source="ticker")

    class Meta:
        model = models.EthereumToken
        fields = ["code", "name", "address"]