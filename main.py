from auth import login
from fetch_media import get_user_id, get_recent_media
from download import download_media

if __name__ == "__main__":
    api = login('username', "password")
    if not api:
        exit()

    accounts = {"posts": ["catstagangsta"], "reels": ["kingcattos", "softcatmemes"]}

    all_posts = []
    all_reels = []

    # Collect all posts.
    for account in accounts["posts"]:
        user_id = get_user_id(api, account)
        if user_id:
            all_posts.extend(get_recent_media(api, user_id, 1))

    # Collect all reels.
    for account in accounts["reels"]:
        user_id = get_user_id(api, account)
        if user_id:
            all_reels.extend(get_recent_media(api, user_id, 2))

    # Sort media by engagement score in descending order.
    sorted_posts = sorted(all_posts, key=lambda x: x[1], reverse=True)
    sorted_reels = sorted(all_reels, key=lambda x: x[1], reverse=True)

    # Download 2 new posts and 2 new reels (if available).
    download_media(sorted_posts, "jpeg", target_count=2)
    download_media(sorted_reels, "mp4", target_count=2)
