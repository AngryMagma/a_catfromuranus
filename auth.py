import time
import random
from instagram_private_api import Client

def login(username, password):
    """Logs in to Instagram with randomized delays to reduce detection."""
    try:
        time.sleep(random.uniform(1, 3))  
        return Client(username, password, auto_patch=True)
    except Exception as e:
        print(f"Login failed: {e}")
        return None
