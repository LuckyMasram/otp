from rest_framework import serializers
from .models import *


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempUser
        fields = ['mobile_number']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempUser
        fields = ['mobile_number', 'otp']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['email','token', 'mobile']


class TradeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeType
        fields = ['trade_id', 'token']


class TradesmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tradesman
        fields = ['tm_id', 'token']


class BookTradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTradesman
        fields = ['token']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ['image_path','token']
