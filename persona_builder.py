import json
import os
import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nlp = spacy.load("en_core_web_sm")
sentiment_analyzer = SentimentIntensityAnalyzer()

def load_user_data(username: str):
    with open(f"data/{username}.json", "r", encoding = "utf-8") as f:
        return json.load(f)
    
def analyze_sentiment(text):
    return sentiment_analyzer.polarity_scores(text)["compound"]

def extract_topics(posts, comments):
    subreddits = {}
    keywords = {}

    for item in posts + comments:
        text = item.get("title", "") + " " + item.get("body", "")
        doc = nlp(text.lower())

        for token in doc:
            if token.is_alpha and not token.is_stop and len(token.text) > 3:
                keywords[token.text] = keywords.get(token.text, 0) + 1
        
        subreddit = item["subreddit"]
        subreddits[subreddit] = subreddits.get(subreddit, 0) + 1

    top_keywords = sorted(keywords.items(), key = lambda x: x[1], reverse = True) [:10]
    top_subreddits = sorted(subreddits.items(), key = lambda x: x[1], reverse = True) [:5]

    return [kw for kw, _ in top_keywords], [sr for sr, _ in top_subreddits]

def build_persona(username: str, posts, comments):
    citations = []
    persona = f"User Persona for u/{username}\n"
    persona += "=" * 40 + "\n\n"

    # Interests
    keywords, subreddits = extract_topics(posts, comments)
    persona += f"**Top Subreddits**: {', '.join(subreddits)}\n"
    persona += f"**Frequent Keywords**: {', '.join(keywords)}\n\n"
    # Tone
    all_text = " ".join([p.get("body", "") + p.get("title", "") for p in posts + comments])
    avg_sentiment = analyze_sentiment(all_text)
    if avg_sentiment >= 0.2:
        mood = "positve"
    elif avg_sentiment <= 0.2:
        mood = "negative"
    else:
        mood = "neutral"
    persona += f"**Overall Sentiment**: {mood} (score: {avg_sentiment:.2f})\n\n"
    # Writing style/ clues
    sample = (posts + comments) [:3]
    persona += "**Sample Clues (Citations):**\n"
    for item in sample:
        url = item["url"]
        excerpt = item.get("title", "") + item.get("body", "")
        excerpt = excerpt.strip().replace("\n", " ") [:200]
        persona += f". \"{excerpt}...\" -> {url}\n"
    return persona

def save_persona(username: str, persona_text: str):
    os.makedirs("output", exist_ok = True)
    path = f"output/{username}_persona.txt"
    with open(path, "w", encoding = "utf-8") as f:
        f.write(persona_text)
    print(f"Persona save to : {path}")

if __name__ == "__main__":
    username = input("Enter Reddit Username: ")
    data = load_user_data(username)
    persona = build_persona(username, data["posts"], data["comments"])
    save_persona(username, persona)