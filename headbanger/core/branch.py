
def create_branch(repo, branch_name):
    '''
     creating of the new branch
    '''
    if not branch_name:
        raise Exception('branch_name is not defined')
    repo.create_head(branch_name)

def get_branches(self, *args, **kwargs):
    ''' 
    return list of active branches
    '''
    return self._repo.branches