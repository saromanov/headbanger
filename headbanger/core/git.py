from git import Repo

class Git:
    def __init__(self, repo_name:str):
        self._repo = Repo(repo_name)
    
    def get_branches(self, *args, **kwargs):
        return self._repo.branches