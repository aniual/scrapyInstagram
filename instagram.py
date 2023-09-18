import requests
import json

# 您的应用程序的客户端ID和访问令牌
client_id = '615373264133878'
access_token = 'EAAIvrcDQHvYBO40ozeOYFPdONPF5FVH9DGDKgJ6wmQOFuq2ZCJrBbzakiNyHoPgKu9KUG9xZCudSLcRHO5oTYGEzp9U3qh5XleQSJybIfrufk2SBOn6u8qZCoby7JCgu80wgKEwyD9mD5UsL1N0zA0nLtXF7YOiMf5IMWEmkWUrCoKnjoEZAhUmB2ij2YL91A8bYMGNlYg2wG9M4xA9Sowl6TvXFjwEb2DZC5IaZBmTMC1Qg5f4jt2N4Ea0q5wwu1zyTPmMQZDZD'

# API请求的基本URL
base_url = 'https://graph.instagram.com/v12.0/'

# 用户名或标签名称
username = 'jeuliajewelry'
tag_name = 'jewelry'

# 获取用户的公开帖子
user_posts_url = f'{base_url}{username}/media?access_token={access_token}'
user_response = requests.get(user_posts_url)
print(user_response.content)
exit()
user_data = user_response.json()

# 获取标签的帖子
tag_posts_url = f'{base_url}tag/{tag_name}/media/recent?access_token={access_token}'
tag_response = requests.get(tag_posts_url)
tag_data = tag_response.json()

# 处理返回的数据
if 'data' in user_data:
    user_posts = user_data['data']
    for post in user_posts:
        print(f"User Post: {post['caption']['text']}")

if 'data' in tag_data:
    tag_posts = tag_data['data']
    for post in tag_posts:
        print(f"Tag Post: {post['caption']['text']}")
