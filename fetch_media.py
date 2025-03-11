import time
import random

def get_user_id(api, username):
    """Fetches user ID based on username."""
    try:
        return api.username_info(username)['user']['pk']
    except Exception as e:
        print(f"Failed to fetch user ID for {username}: {e}")
        return None

def get_recent_media(api, user_id, media_type):
    """Fetches recent media of a given type (1: photo, 2: reel)."""
    try:
        time.sleep(random.uniform(1, 2))
        media_items = api.user_feed(user_id)['items'][:10]
        media_list = []

        for item in media_items:
            if int(item['media_type']) == media_type:
                url = item['image_versions2']['candidates'][0]['url'] if media_type == 1 else item['video_versions'][0]['url']
                views = int(item.get('view_count', 1))  # Avoid division by zero
                interactions = int(item['like_count']) + (int(item['comment_count']) * 4)
                score = interactions / views  
                media_list.append((url, score, item['id']))

        return media_list
    except Exception as e:
        print(f"Error fetching media for user {user_id}: {e}")
        return []
