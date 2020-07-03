
def create_branch(repo, branch_name):
    '''
     creating of the new branch
    '''
    if not branch_name:
        raise Exception('branch_name is not defined')
    repo.create_head(branch_name)

def get_branches(repo, *args, **kwargs):
    ''' 
    return list of active branches
    '''
    return repo.branches

def delete_branches(repo, branches):
    [repo.delete_head(name) for name in branches]