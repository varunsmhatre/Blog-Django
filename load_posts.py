import json
from blog.models import Post

with open('posts.json') as f:
    posts_json = json.load(f)

print(posts_json)

for post in posts_json:
    p = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
    p.save()