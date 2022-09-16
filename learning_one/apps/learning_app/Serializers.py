from rest_framework import serializers
from .models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    # review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('watchlist', 'review_user')


class WatchListSerializer(serializers.ModelSerializer):
    reviewList = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True, read_only=True)
    watchlist = serializers.StringRelatedField(many=True, read_only=True)

    def validate(self, data):
        if data['name'] == data['about']:
            raise serializers.ValidationError('title and storyline are the same')
        else:
            return data

    class Meta:
        model = StreamPlatform
        fields = '__all__'

