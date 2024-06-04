# from rest_framework.decorators import api_view
# import requests
# import json
# from requests.models import Response


# @api_view(['POST'])
# def kakaoPay(request):
#     url = "https://kapi.kakao.com/v1/payment/ready"
#     headers = {
#         'Authorization': "KakaoAK " + "PRD34E14554881CD7151B375365546C201A88AA3",
#         'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
#     }
#     params = {
#         "cid": "TC0ONETIME",
#         "partner_order_id": "partner_order_id",
#         "partner_user_id": "partner_user_id",
#         "item_name": "초코파이",
#         "quantity": "1",
#         "total_amount": "2200",
#         "vat_amount": "200",
#         "tax_free_amount": "0",
#         "approval_url": "https://developers.kakao.com/success",
#         "fail_url": "https://developers.kakao.com/fail",
#         "cancel_url": "https://developers.kakao.com/cancel"
#     }
#     response = requests.post(url, params=params, headers=headers)
#     response = json.loads(response.text)
#     return Response(response)  


import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import KakaoPayReadySerializer
from django.conf import settings
# from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# @method_decorator(csrf_exempt, name='dispatch')

class KakaoPayReadyView(APIView):
    def post(self, request):
        print("Received request with headers:", request.headers)
        print("Received data:", request.data)  # 요청 데이터 확인 (디버그용)

        serializer = KakaoPayReadySerializer(data=request.data)
        if serializer.is_valid():
            url = "https://open-api.kakaopay.com/online/v1/payment/ready"
            headers = {
                "Authorization": f"SECRET_KEY {settings.KAKAO_SECRET_KEY}",
                "Content-Type": "application/json",
            }
            data = {
                "cid": "TC0ONETIME",
                "partner_order_id": serializer.validated_data["partner_order_id"],
                "partner_user_id": serializer.validated_data["partner_user_id"],
                "item_name": serializer.validated_data["item_name"],
                "quantity": serializer.validated_data["quantity"],
                "total_amount": serializer.validated_data["total_amount"],
                "vat_amount": serializer.validated_data["vat_amount"],
                "tax_free_amount": serializer.validated_data["tax_free_amount"],
                "approval_url": serializer.validated_data["approval_url"],
                "cancel_url": serializer.validated_data["cancel_url"],
                "fail_url": serializer.validated_data["fail_url"],
            }
            print("Sending data to KakaoPay:", data)  # 전송 데이터 확인 (디버그용)
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                return Response(response.json())
            else:
                print("KakaoPay API error:", response.status_code, response.text)  # API 오류 확인 (디버그용)
                return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        else:
            print("Serializer validation errors:", serializer.errors)  # 검증 오류 메시지 출력 (디버그용)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
@csrf_exempt
def ready(request):
    if request.method == "POST":
        print("Received request with headers:", request.headers)
        print("Received data:", request.data)  # 요청 데이터 확인 (디버그용)

        serializer = KakaoPayReadySerializer(data=request.data)
        if serializer.is_valid():
            url = "https://open-api.kakaopay.com/online/v1/payment/ready"
            headers = {
                "Authorization": f"SECRET_KEY {settings.KAKAO_SECRET_KEY}",
                "Content-Type": "application/json",
            }
            data = {
                "cid": "TC0ONETIME",
                "partner_order_id": serializer.validated_data["partner_order_id"],
                "partner_user_id": serializer.validated_data["partner_user_id"],
                "item_name": serializer.validated_data["item_name"],
                "quantity": serializer.validated_data["quantity"],
                "total_amount": serializer.validated_data["total_amount"],
                "vat_amount": serializer.validated_data["vat_amount"],
                "tax_free_amount": serializer.validated_data["tax_free_amount"],
                "approval_url": serializer.validated_data["approval_url"],
                "cancel_url": serializer.validated_data["cancel_url"],
                "fail_url": serializer.validated_data["fail_url"],
            }
            print("Sending data to KakaoPay:", data)  # 전송 데이터 확인 (디버그용)
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                return Response(response.json())
            else:
                print("KakaoPay API error:", response.status_code, response.text)  # API 오류 확인 (디버그용)
                return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        else:
            print("Serializer validation errors:", serializer.errors)  # 검증 오류 메시지 출력 (디버그용)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)