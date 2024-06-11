from rest_framework import serializers

from .models import Email,rating


class emailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Email
        fields = ('mail_name',)
class danhgiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = rating
        fields = ('id_category','name','text','rating',)





