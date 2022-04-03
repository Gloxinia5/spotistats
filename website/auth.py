from secrets import token_bytes
from flask import Blueprint, Flask, request, url_for, session, redirect, blueprints
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

auth = Blueprint('auth', __name__)

client_id = 'd8bd30488784431daa992c3d49198ea4'
cliet_secret_id = '925388b2e0d7400ca086d65c1903a6da'
TOKEN_INFO = "token_info"
@auth.route('/login')
def hello_world():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@auth.route('/redirect')
def redirectPage():
    sp_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('views.profile'))

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id= client_id,
        client_secret= cliet_secret_id,
        redirect_uri= url_for('auth.redirectPage', _external=True),
        scope='user-read-recently-played user-read-private user-top-read user-read-currently-playing')

def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        raise "exception"
    now = int(time.time())

    is_expired = token_info['expires_at'] - now < 60
    if is_expired:
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.refresh_access_token(token_info=['refresh_token'])
    return token_info



