from rest_framework import serializers

class KakaoPayReadySerializer(serializers.Serializer):
    partner_order_id = serializers.CharField(max_length=100)
    partner_user_id = serializers.CharField(max_length=100)
    item_name = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField()
    total_amount = serializers.IntegerField()
    vat_amount = serializers.IntegerField()
    tax_free_amount = serializers.IntegerField()
    approval_url = serializers.CharField()
    cancel_url = serializers.CharField()
    fail_url = serializers.CharField()
