import sys
from github import GitHub

def main(token, whitelist):
    git_hub = GitHub(token)
    current_page = 1

    while True:
        followed = git_hub.followed_users(current_page)
        if not followed:
            break

        for user in followed:
            target_user = user['login']
            if target_user not in whitelist:
                follows_back = git_hub.check_follow_back(target_user)
                if not follows_back:
                    git_hub.unfollow_user(target_user)

        current_page += 1

    print("Unfollow script completed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 unfollow.py <TOKEN> [user1 user2 user3 ...]")
        sys.exit(1)

    token = sys.argv[1]
    whitelist = sys.argv[2:]
    main(token, whitelist)
