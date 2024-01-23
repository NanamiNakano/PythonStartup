import json

import requests

github_username = input("Enter GitHub username:")
print(f"Getting stats for {github_username}...")

user = json.loads(requests.get(f"https://api.github.com/users/{github_username}").text)


def get_pagination(link):
    targets = []
    response = requests.get(link)
    targets += json.loads(response.text)
    try:
        next_link = response.links["next"]
        targets += get_pagination(next_link["url"])
        return targets
    except KeyError:
        return targets


def get_repos():
    repos_url = user["repos_url"]
    repos = get_pagination(repos_url)
    return repos


def get_stars():
    repos = get_repos()
    count = 0
    for repo in repos:
        count += len(get_pagination(repo["stargazers_url"]))
    return count


print(f"Name: {user['name']}")
print(f"Company: {user['company']}")
print(f"Email: {user['email']}")
print(f"Bio: {user['bio']}")
print(f"{user['followers']} followers, {user['following']} following, {user['public_repos']} repos, {get_stars()} total star received")
