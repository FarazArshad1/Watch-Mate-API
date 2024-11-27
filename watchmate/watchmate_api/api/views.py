from watchmate_api.api.serailizers import MovieSerialzier
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchmate_api.models import Movie
from rest_framework.response import Response
from rest_framework import status


#---------------------------------Class Based Approach------------------------------

class MovieListAV(APIView):

    def get(self,request):
        movies = Movie.objects.all()
        serializer = MovieSerialzier(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerialzier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)
        
class MovieDetailAV(APIView):
    
    def get(self,request,pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error':'Movie Not Found'},status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerialzier(movie)
        return Response(serializer.data)

    def put(self,request,pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerialzier(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self,resquest,pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204)

#---------------------------------Function Based Approach------------------------------
""" This whole code uses function based approach which is good but we want to implement 
    Class based approach which is better."""

# @api_view(["GET","POST"])
# def movie_list(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerialzier(movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == "POST":
#         serializer = MovieSerialzier(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(["GET","PUT","DELETE"])
# def movies_details(request,pk):

    # if request.method == "GET":
    #     movie = Movie.objects.get(pk=pk)
    #     serializer = MovieSerialzier(movie) 
    #     return Response(serializer.data)
    
    # if request.method == "PUT":
    #     movie = Movie.objects.get(pk=pk)
    #     serializer = MovieSerialzier(movie,data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.error)
        
    # if request.method == "DELETE":
        # movie = Movie.objects.get(pk=pk)
        # movie.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)