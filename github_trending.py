import requests
from datetime import datetime, timedelta


TOP_SIZE = 20
API_URL = "https://api.github.com/search/repositories"
DAYS_PERIOD = 7


def get_trending_repositories(top_size):
    since_date = datetime.today().date() - timedelta(DAYS_PERIOD)
    params = {
        "q": "created:>={}".format(since_date),
        "sort": "stars",
        "per_page": top_size
    }
    response = requests.get(API_URL, params)
    if response.ok:
        return response.json()["items"]
    return None


if __name__ == '__main__':
    repos = get_trending_repositories(TOP_SIZE)
    if not repos:
        exit("Can't fetch api.github.com")

    for repo in repos:
        print("{} has {} stars and {} issues. URL: {}".format(
            repo["full_name"],
            repo["stargazers_count"],
            repo["open_issues"],
            repo["html_url"]
        ))
