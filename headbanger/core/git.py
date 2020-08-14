from git import Repo
from .branch import create_branch, get_branches, delete_branches, checkout_branch
from .commits import get_commits

class Git:
    def __init__(self, repo_name:str):
        self._repo = Repo(repo_name)
    
    def get_branches(self, *args, **kwargs):
        return get_branches(self._repo)
    
    def create_branch(self, branch_name:str):
        return create_branch(self._repo, branch_name)
    
    def delete_branches(self, branches):
        delete_branches(self._repo, branches)

    def get_commits(self, branch_name:str):
        return get_commits(self._repo, branch_name)
    
    def checkout_branch(self, branch_name:str):
        return checkout_branch(self._repo, branch_name)