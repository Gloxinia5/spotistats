from flask import Blueprint, Flask, jsonify, render_template, request, url_for, session, redirect, blueprints
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from . import auth
import random

views = Blueprint('views', __name__)

y = random.randint(1,9)

@views.route('/')
def homepage():
    return render_template('homepage.html')

@views.route('/profile', methods=['POST', 'GET'])
def profile(): 
    try:
        token_info = auth.get_token()
    except:
        return redirect('/login')
    sp = spotipy.Spotify(auth = token_info['access_token'])
    user = sp.current_user() 
    user_ta = sp.current_user_top_artists(limit=10)
    user_tt = sp.current_user_top_tracks(limit=10)
    curr_play = sp.currently_playing()
    x = sp.current_user_recently_played(limit=1)
    return render_template('profile.html', user=user, curr_play=curr_play, recplay=x, ta=user_ta, tt=user_tt)

@views.route('/update', methods=['POST', 'GET'])
def update():
    try:
        token_info = auth.get_token()
    except:
        return redirect('/login')
    sp = spotipy.Spotify(auth = token_info['access_token'])
    user = sp.current_user()
    curr_play = sp.currently_playing()
    rec_play = sp.current_user_recently_played(limit=1)
    print(curr_play)
    return jsonify(curr_play, rec_play)
