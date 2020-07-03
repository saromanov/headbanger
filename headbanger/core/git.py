from git import Repo

class Git:
    def __init__(self, repo_name:str):
        self._repo = Repo(repo_name)
    
    def get_branches(self, *args, **kwargs):
        return self._repo.branches
    
    def create_branch(self, branch_name):
        if not branch_name:
            raise Exception('branch_name is not defined')
        self._repo.create_head(branch_name)
    
    def delete_branches(self, branches):
        [self._repo.delete_head(name) for name in branches]