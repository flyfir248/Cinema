from flask import Flask, render_template, request
from imdb import IMDb

app = Flask(__name__)
ia = IMDb()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search_movies():
    query = request.args.get('query')
    if query:
        movies = ia.search_movie(query)
        return render_template('result.html', movies=movies)
    else:
        return render_template('result.html', movies=[])

@app.route('/genre/<genre_name>')
def genre_movies(genre_name):
    genre_id = ia.get_keyword(genre_name)
    movies = ia.get_keyword(genre_id, results=20)
    return render_template('result.html', movies=movies)

@app.route('/movie/<imdb_id>')
def movie_details(imdb_id):
    movie = ia.get_movie(imdb_id)
    return render_template('details.html', movie=movie)

if __name__ == '__main__':
    app.run(debug=True)
