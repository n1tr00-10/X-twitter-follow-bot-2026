import requests
import random
import time
import json
from requests_oauthlib import OAuth1

def load_config():
    with open("twitter_config.json", "r") as f:
        return json.load(f)

def load_proxies():
    try:
        with open("proxies.txt", "r") as f:
            lines = [l.strip() for l in f if l.strip() and not l.startswith('#')]
            return [f"http://{line}" for line in lines] if lines else []
    except:
        return []

def follow_user(oauth, target_id, proxy=None):
    url = "https://api.twitter.com/1.1/friendships/create.json"
    data = {
        "user_id": target_id,
        "follow": "true"
    }
    proxies = {"http": proxy, "https": proxy} if proxy else None
    try:
        r = requests.post(url, data=data, auth=oauth, proxies=proxies, timeout=10)
        if r.status_code == 200:
            return True, r.json().get("screen_name", target_id)
        else:
            return False, f"HTTP {r.status_code}"
    except Exception as e:
        return False, str(e)

def main():
    config = load_config()
    oauth = OAuth1(
        config["consumer_key"],
        client_secret=config["consumer_secret"],
        resource_owner_key=config["access_token"],
        resource_owner_secret=config["access_token_secret"]
    )
    proxies = load_proxies()
    target = input("Target user ID: ").strip()
    amount = int(input("How many follows (per account): "))
    
    print(f"Following {target} {amount} times (using {len(proxies)} proxies)")
    for i in range(amount):
        proxy = random.choice(proxies) if proxies else None
        ok, info = follow_user(oauth, target, proxy)
        if ok:
            print(f"[{i+1}/{amount}] Followed @{info}")
        else:
            print(f"[{i+1}/{amount}] Failed: {info}")
        time.sleep(random.uniform(2, 5))

if __name__ == "__main__":
    main()
