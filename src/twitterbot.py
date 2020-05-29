from textgenrnn import textgenrnn
import tweepy

auth = tweepy.OAuthHandler(@, @)
auth.set_access_token(@, @)

api = tweepy.API(auth)

def generate_tweet():
    textgen = textgenrnn('../weights/tao.hdf5')

    tweet = ""
    generation = ""

    # avoid chance of empty tweet
    while len(generation) < 20:
        generation = textgen.generate(return_as_list=True, max_gen_length=300)[0]
    tweet += generation

    tweet += " \n#philosophy #wisdom #quotes"
    return tweet

def post_tweet():
    text = generate_tweet()
    api.update_status(status=text)

post_tweet()