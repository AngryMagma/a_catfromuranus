import requests

def download_media(data, file_ext, target_count=2):
    """Downloads media items until 'target_count' new items have been downloaded,
    skipping those already present in downloaded_posts.txt.
    
    Args:
        data (list): List of tuples (media_url, score, media_id) sorted by score.
        file_ext (str): File extension to use (e.g., 'jpg' for posts, 'mp4' for reels).
        target_count (int): Number of new media items to download.
    """
    downloaded_count = 0
    try:
        # Open the file in a+ mode to read previously downloaded IDs.
        with open("downloaded_posts.txt", "a+") as file:
            file.seek(0)
            downloaded_ids = set(file.read().splitlines())

        # Iterate over the media items until we reach the target count.
        for media_url, score, media_id in data:
            if downloaded_count >= target_count:
                break

            if media_id in downloaded_ids:
                print(f"Skipping already downloaded {media_id}")
                continue

            print(f"Downloading {media_id}...")
            response = requests.get(media_url, timeout=5)

            with open(f"media_{media_id}.{file_ext}", 'wb') as media_file:
                media_file.write(response.content)

            # Append the downloaded media_id to the file.
            with open("downloaded_posts.txt", "a") as file:
                file.write(f"{media_id}\n")

            print(f"Successfully downloaded {media_id}")
            downloaded_count += 1

        if downloaded_count < target_count:
            print(f"Only {downloaded_count} new media items were downloaded. Not enough new media available.")
    except Exception as e:
        print(f"Error downloading media: {e}")
