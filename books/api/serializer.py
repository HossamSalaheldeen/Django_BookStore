from django.contrib.auth.models import User
from books.models import Book
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']

    def save(self, **kwargs):
        user = User (
            email = self.validated_data.get('email'),
            username = self.validated_data.get('username')
        )
        
        user.set_password(self.validated_data.get('password'))
        user.save()

        # if self.validated_data.get('password') !=  self.validated_data.get('password2'):
        #     raise serializers.ValidationError({
        #         'password' : 'password does not match'
        #     })
        # else:
        #     user.set_password(self.validated_data.get('password'))
        #     user.save()

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title','description','creator']
