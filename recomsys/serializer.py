from rest_framework import serializers
from .models import Favlist,Wishlist,Recommend,Item

class FavListSerial(serializers.ModelSerializer):
    class Meta:
        model = Favlist
        fields = '__all__'

class WishListSerial(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

class RecomSerial(serializers.ModelSerializer):
    class Meta:
        model = Recommend
        fields = '__all__'

class ItemSerial(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'