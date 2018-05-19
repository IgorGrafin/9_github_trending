import requests
from datetime import datetime, timedelta


def get_trending_repositories(top_size, days):
    api_url = "https://api.github.com/search/repositories"
    since_date = datetime.today().date() - timedelta(days)
    params = {
        "q": "created:>={}".format(since_date),
        "sort": "stars",
        "per_page": top_size
    }
    response = requests.get(api_url, params)
    if response.ok:
        return response.json()["items"]


def get_open_issues_amount(repo_full_name):
    api_url = "https://api.github.com/repos/{}/issues".format(repo_full_name)
    response = requests.get(api_url)
    return len(response.json())


if __name__ == "__main__":
    days_period = 7
    top_size = 20
    repos = get_trending_repositories(top_size, days_period)
    if not repos:
        exit("Can't fetch api.github.com")

    print("Top {} repositories created for last {} days:".format(
        top_size, days_period))

    for repo in repos:
        print("Project {} has {} stars and {} issues. URL: {}".format(
           repo["name"],
           repo["stargazers_count"],
           get_open_issues_amount(repo["full_name"]),
           repo["html_url"]
       ))
