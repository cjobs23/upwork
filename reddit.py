import praw

reddit = praw.Reddit(
    client_id="your_client_id",
    client_secret="your_client_secret",
    username="your_bot_username",
    password="your_bot_password",
    user_agent="your_user_agent"
)
subreddit = reddit.subreddit("your_subreddit_name")
for post in subreddit.new(limit=10):
    print(post.title)
for post in subreddit.new(limit=10):
    post.reply("Your comment text here")
link = "https://your-website.com"
message = "Check out my website!"

for post in subreddit.new(limit=10):
    comment = f"Hi, thanks for posting! If you're interested, you can check out my website at {link} or send me a message with the link to learn more: {message}"
    post.reply(comment)
