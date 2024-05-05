# MovieRaterAPI

APIs
1. Add new movie
   POST http://127.0.0.1:8000/api/movies/
   Body:
     "title": "",
     "description": ""


3. Get list of movies
   GET http://127.0.0.1:8000/api/movies/


4. Editing specific movie
   PUT http://127.0.0.1:8000/api/movies/1/
   Body:
     "title": "",
     "description": ""


6. Delete Movie
   DELETE http://127.0.0.1:8000/api/movies/3/


7. Add new rating
   POST http://127.0.0.1:8000/api/ratings/
   Body:
     "stars": 5,
     "movie": 1,
     "user": 1


8. Get list of ratings
   GET http://127.0.0.1:8000/api/ratings/


9. Update rating
   PUT http://127.0.0.1:8000/api/ratings/1/
   Body:
     "stars": 4,
     "movie": 1,
     "user": 1

   
