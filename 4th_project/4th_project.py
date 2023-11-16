#9. Create a RESTful API using Flask to perform CRUD operations on resources like books or movies.
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to simulate a database
movies = [
    {'id': 1, 'title': 'Movie 1', 'genre': 'Action'},
    {'id': 2, 'title': 'Movie 2', 'genre': 'Comedy'},
    {'id': 3, 'title': 'Movie 3', 'genre': 'Drama'},
]

# Read a specific movie
@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if movie:
        return jsonify({'movie': movie})
    return jsonify({'message': 'Movie not found'}), 404


# Create a new movie
@app.route('/movies', methods=['POST'])
def create_movie():
    new_movie = {'id': len(movies) + 1, 'title': request.json['title'], 'genre': request.json['genre']}
    movies.append(new_movie)
    return jsonify({'movie': new_movie}), 201

    # Update a movie
@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if movie:
        movie['title'] = request.json.get('title', movie['title'])
        movie['genre'] = request.json.get('genre', movie['genre'])
        return jsonify({'movie': movie})
    return jsonify({'message': 'Movie not found'}), 404

# Delete a movie
@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    global movies
    movies = [m for m in movies if m['id'] != movie_id]
    return jsonify({'message': 'Movie deleted successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)