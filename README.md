# Reddit User Persona Generator

This project scrapes Reddit user data and generates a psychological and topical **Persona profile** based on their publicly available posts and comments. It uses NLP, sentiment analysis, and topic modeling to infer user traits, interests, and tone of voice. 

---

## Features
- Uses Reddit API to fetch recent posts and comments
- Extracts common **keywords**, **subreddits**, and **sentiment**
- Outputs a clean persona report with **citations from real posts**
- Built using Python and NLP libraries ('praw', 'spacy', 'nltk')

## Folder Structure 
GenAI_Assign/
├── config.py # Reddit API keys 
├── scraper.py # Collects Reddit posts/comments
├── persona_builder.py # Generates persona from JSON data
├── requirements.txt # List of dependencies
├── data/ # Stores raw scraped data
│ └── kojied.json
├── output/ # Final persona outputs
│ └── kojied_persona.txt
└── README.md # You’re reading it now!

## How to Run This Project

### 1. Install Dependencies
Open terminal and run:
pip install -r requirements.txt
python3 -m spacy download en_core_web_sm

### 2. Setup Reddit API
Create a file named config.py in the root folder:

# config.py
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
USER_AGENT = "ReditPersonaBot by u/your_reddit_username"

You can get these by creating a script app at:  https://www.reddit.com/prefs/apps

### 3. Scrape Reddit User Data
python3 scraper.py

Paste the Reddit user profile URL (e.g. https://www.reddit.com/user/kojied/) when prompted

This will generate:
data/kojied.json

### 4. Generate Persona from data
python3 persona_builder.py

This will create:
output/kojied_persona.txt

### Example Output:
User Persona for u/kojied
========================================

**Top Subreddits**: civ5, AskReddit, AskNYC, ManorLords, warriors
**Frequent Keywords**: like, people, know, good, think, build, game, going, hard, definitely

**Overall Sentiment**: positve (score: 1.00)

**Sample Clues (Citations):**
. "I feel violated by intern seasonThere's this bar that I frequent a few blocks away from my house. Technically different neighborhood, but generally has a mature vibe with people who like music and to ..." -> https://www.reddit.com/r/newyorkcity/comments/1lykkqf/i_feel_violated_by_intern_season/
. "H1B holders, what are your thoughts on the narrative that you are being exploited?..." -> https://www.reddit.com/r/AskReddit/comments/1hnx8j0/h1b_holders_what_are_your_thoughts_on_the/
. "H1B holders, do you feel exploited, or see it as an opportunity to build a better life for you in the US?..." -> https://www.reddit.com/r/AskReddit/comments/1hnx7lj/h1b_holders_do_you_feel_exploited_or_see_it_as_an/

# Use Cases
- Behavioral analysis for moderators
- AI-generated marketing personas
- Discourse research across subreddits
- Target audience profiling for brands

# Limitations
Currently processes only posts (not comments)

Can be extended with:
✅ Comment analysis
✅ Personality trait modeling (e.g., Big Five)
✅ Visualizations (word clouds, graphs)
✅ Bot/spam detection modules

# Author
Krupa Gohil
This project was built as part of Generative AI Analyst Assessment

