from flask import render_template
from app import app

# Views
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    
    return render_template('movie.html',id = movie_id)




