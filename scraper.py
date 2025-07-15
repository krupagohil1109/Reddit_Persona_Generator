import praw
import json
import os
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT

def init_reddit():
    return praw.Reddit(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        user_agent = USER_AGENT
    )

def extract_username(profile_url: str) -> str:
    return profile_url.strip("/").split("/")[-1]

def fetch_user_data (username: str, post_limit = 50, coment_limit = 100):
    reddit = init_reddit()
    try: 
        redditor = reddit.redditor(username)
        posts, comments = [], []

        for submission in redditor.submissions.new(limit = post_limit):
            posts.append({
                "type": "post",
                "title": submission.title,
                "body": submission.selftext,
                "subreddit": str(submission.subreddit),
                "url": f"https://www.reddit.com{submission.permalink}"
            })
            for comment in redditor.comments.new(limit = coment_limit):
                comments.append({
                    "type": "comment",
                    "body": comment.body,
                    "subreddit": str(comment.subreddit),
                    "url": f"https://www.reddit.com{comment.permalink}"
                })
        return posts, comments
    except Exception as e:
        print(f"Error: {e}")
        return [], []

def save_data_as_json(username: str, posts, commments):
    os.makedirs("data", exist_ok = True)
    data = {
        "username": username, 
        "posts": posts, 
        "comments": comments
    }
    with open(f"data/{username}.json", "w", encoding = "utf-8") as f:
        json.dump(data, f, indent = 2, ensure_ascii = False)
    print(f"Data saved to: data/{username}.json")

if __name__ == "__main__":
    profile_url = input("Paste Reddit profile URL: ")
    username = extract_username(profile_url)
    posts, comments = fetch_user_data(username)
    save_data_as_json(username, posts, comments)
