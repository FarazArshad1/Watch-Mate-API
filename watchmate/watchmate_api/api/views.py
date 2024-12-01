from watchmate_api.api.serailizers import WatchListSerializer
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchmate_api.models import WatchList
from rest_framework.response import Response
from rest_framework import status


#---------------------------------Class Based Approach------------------------------

class WatchListAV(APIView):

    def get(self,request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)
        
class WatchDetailAV(APIView):
    
    def get(self,pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':'Movie Not Found'},status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data)

    def put(self,request,pk):
        watchlist = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self,resquest,pk):
        watchlist = WatchList.objects.get(pk=pk)
        watchlist.delete()
        return Response(status=status.HTTP_204)

class StreamPlatformAV(APIView):
    def get(self):


#---------------------------------Function Based Approach------------------------------
""" This whole code uses function based approach which is good but we want to implement 
    Class based approach which is better."""

# @api_view(["GET","POST"])
# def movie_list(request):
#     if request.method == "GET":
#         movies = WatchList.objects.all()
#         serializer = WatchListSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == "POST":
#         serializer = WatchListSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(["GET","PUT","DELETE"])
# def movies_details(request,pk):

    # if request.method == "GET":
    #     movie = WatchList.objects.get(pk=pk)
    #     serializer = WatchListSerializer(movie) 
    #     return Response(serializer.data)
    
    # if request.method == "PUT":
    #     movie = WatchList.objects.get(pk=pk)
    #     serializer = WatchListSerializer(movie,data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.error)
        
    # if request.method == "DELETE":
        # movie = WatchList.objects.get(pk=pk)
        # movie.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)