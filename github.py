import requests

class GitHub:
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
        }
        self.username = self.profile()["login"]

    def profile(self):
        url = "https://api.github.com/user"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def followed_users(self, current_page=1):
        url = f"https://api.github.com/user/following?page={current_page}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def unfollow_user(self, target):
        url = f"https://api.github.com/user/following/{target}"
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            print(f"Unfollowed {target}")
        else:
            print(f"Error unfollowing {target}: {response.text}")

    def check_follow_back(self, target):
        url = f"https://api.github.com/users/{target}/following/{self.username}"
        response = requests.get(url, headers=self.headers)
        return response.status_code == 204
