from Gsheets import parse_dict
import tweepy
import twt_kets as keys

def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str, image_path = None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print('tweeted successfully')

def post_twt():
    api = api()
    tweet(api, parse_dict())