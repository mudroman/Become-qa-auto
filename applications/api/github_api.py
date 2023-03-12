import requests

class GitHubAPI:
                        
    def __init__(self, base_url) -> None:
        self.base_url = base_url

    def get_user(self, username):
        r = requests.get(f'{self.base_url}/users/{username}')
        r.raise_for_status()
        # above /\ does this code
        # if r.status_code != 200:
        # raise HTTPError
        return r.json()
    def get_repos(self, repos_search_param):
        r = requests.get(
        f'{self.base_url}/search/repositories', #?q={repos_search_param}
        params={'q': repos_search_param}
        )
        r.raise_for_status()
        # /search/repositories
        return r.json()