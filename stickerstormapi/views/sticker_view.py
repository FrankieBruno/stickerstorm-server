from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from stickerstormapi.models import Sticker


class StickerView(ViewSet):
    """sticker storm sticker view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single sticker

        Returns:
            Response -- JSON serialized sticker
        """
        sticker = Sticker.objects.get(pk=pk)
        serializer = StickerSerializer(sticker)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all stickers

        Returns:
            Response -- JSON serialized list of stickers
        """
        sticker = Sticker.objects.all()
        serializer = StickerSerializer(sticker, many=True)
        return Response(serializer.data)


class StickerSerializer(serializers.ModelSerializer):
    """JSON serializer for sticker model
    """
    class Meta:
        model = Sticker
        fields = ('id', 'user', 'name', 'image', 'finish_type', 'sticker_size')