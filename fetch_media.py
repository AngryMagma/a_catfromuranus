import time
import random

def get_user_id(api, username):
    try:
        return api.username_info(username)['user']['pk']
    except Exception as e:
        print(f"Failed to fetch user ID for {username}: {e}")
        return None

def calculate_engagement_score(likes, comments, shares, views):
    weight_likes = 1
    weight_comments = 2
    weight_shares = 1.5
    weight_views = 2
    engagement_score = ((likes * weight_likes) + (comments * weight_comments) + (shares * weight_shares) )/(views*weight_views)
    return engagement_score

def get_recent_media(api, user_id, media_type):
    """Gets recent media of a given type (1: photo, 2: reel)."""
    try:
        time.sleep(random.uniform(1, 2))
        media_items = api.user_feed(user_id)['items'][:10]
        media_list = []

        for item in media_items:
            if int(item['media_type']) == media_type:
                url = item['image_versions2']['candidates'][0]['url'] if media_type == 1 else item['video_versions'][0]['url']
                views = int(item.get('view_count', 1))  # Avoid division by zero
                likes =  int(item['like_count'])
                comments = int(item['comment_count'])
                score = calculate_engagement_score(likes, comments , )
                media_list.append((url, score, item['id']))

        return media_list
    except Exception as e:
        print(f"Error fetching media for user {user_id}: {e}")
        return []

