from git import Repo
from branch import create_branch

class Git:
    def __init__(self, repo_name:str):
        self._repo = Repo(repo_name)
    
    def get_branches(self, *args, **kwargs):
        return self._repo.branches
    
    def create_branch(self, branch_name):
        return create_branch(self._repo, branch_name)
    
    def delete_branches(self, branches):
        [self._repo.delete_head(name) for name in branches]