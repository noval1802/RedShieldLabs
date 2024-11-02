import tweepy

# Masukkan Bearer Token dari Twitter Developer
bearer_token = "YOUR_BEARER_TOKEN"

# Inisialisasi client Tweepy
client = tweepy.Client(bearer_token=bearer_token)

# Fungsi untuk mengambil tweet berdasarkan kata kunci
def get_tweets(keyword, max_results=10):
    tweets = client.search_recent_tweets(query=keyword, max_results=max_results)
    for tweet in tweets.data:
        print(f"{tweet.text}\n")

# Mengambil tweet terkait dengan kata kunci
get_tweets("python", max_results=5)
