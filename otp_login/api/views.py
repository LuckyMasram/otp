from rest_framework.response import Response
from .serializer import *
from .models import *
from .utils import send_otp
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime, timedelta
import jwt


class LoginView(CreateAPIView):
    serializer_class = CreateUserSerializer
    def post(self, request, *args, **kwargs):
        mobile_number = request.data.get('mobile_number')
        if mobile_number is not None:
            otp = send_otp(mobile_number)
            TempUser.objects.create(mobile_number=mobile_number, otp=otp, created_time=datetime.utcnow(),
                                    expire_time=datetime.utcnow() + timedelta(hours=24))
            return Response({
                'otp generated': otp
            }, status=status.HTTP_201_CREATED)
        return Response('invalid number', status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(CreateAPIView):
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        mobile_number = request.data.get('mobile_number', False)
        otp = request.data.get('otp', False)

        if mobile_number and otp:
            old = TempUser.objects.filter(mobile_number = mobile_number)
            if old.exists():
                old = old.first()
                otp2 = old.otp
                if str(otp2) == str(otp):
                    old.validated = True
                    old.save()
                    user = TempUser.objects.filter(mobile_number=mobile_number).last()
                    payload = {
                        'id': user.id,
                        'exp': datetime.utcnow() + timedelta(minutes=60),
                        'iat': datetime.utcnow()
                    }

                    token = jwt.encode(payload, 'secret', algorithm='HS256')

                    Customer.objects.create(token=token)
                    return Response({
                        'status' : 1001,
                        'Token' : token,
                        })

                else:
                    return Response({
                        'status' : False,
                        'detail' : 'OTP incorrect.'
                        })
            else:
                return Response({
                    'status' : False,
                    'detail' : 'First proceed via sending otp request.'
                    })
        else:
            return Response({
                'status' : False,
                'detail' : 'Please provide both mobile_number and otp for validations'
                })



class CustomerProfileView(APIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        token = request.data.get('token')
        mobile = request.data.get('mobile')
        user = Customer.objects.filter(token=token).first()
        access_token = user.token
        if token == access_token:
            return Response({
                'status': 1006,
                'cust_id': user.cust_id,
                'customer_name': user.customer_name,
                'dob' : user.dob,
                'email': user.email,
                'is_active': user.is_active,
                'created' : user.created_date,

            })
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ProfileUploadView(APIView):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        image_path = request.data.get('image_path')
        if token:
            if image_path:
                ImageUpload.objects.update(image_path=image_path)
                return Response({
                    'status': 1005,
                    'Message': 'Profile Image Uploaded Successfully.'
                })
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class BookTradesmanView(APIView):
    queryset = BookTradesman.objects.all()
    serializer_class = BookTradesSerializer

    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        tm_id = request.data.get('tm_id')
        date = request.data.get('date')
        time = request.data.get('time')
        if token:
            if tm_id:
                return Response({
                    'status': 1004,
                    'Message': 'Request Added Successfully.'
                })
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

