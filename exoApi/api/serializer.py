from rest_framework import serializers

from .models import Categories, Souscategories, Article, Commentaires


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class SouscategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Souscategories
        fields = '__all__'

class CommentairesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaires
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

#votes = VoteSerializer(many=True, required=False)
#choices = ChoiceSerializer(many=True, read_only=True, required=False)

