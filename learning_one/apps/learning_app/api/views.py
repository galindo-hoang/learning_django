from rest_framework import status, generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from ..Serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from ..models import WatchList, StreamPlatform, Review


class WatchListAV(APIView):
    def get(self, request):
        return Response(WatchListSerializer(WatchList.objects.all(), many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            watch = WatchList.objects.get(pk=pk)
            return Response(WatchListSerializer(watch).data, status=status.HTTP_200_OK)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        watch = WatchList.objects.get(pk=pk)
        watch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        watch = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(watch, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


class ReviewCreateAV(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        review_user = self.request.user
        review_query = Review.objects.filter(watchlist=watchlist, review_user=review_user)
        if review_query.exists():
            raise ValidationError("You have reviewed this movie")

        serializer.save(watchlist=watchlist, review_user=review_user)


class ReviewAV(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.all()

    def get_serializer_class(self):
        return ReviewSerializer


class ReviewDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# class ReviewWatchDetailAV()
