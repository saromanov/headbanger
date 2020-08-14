
def create_branch(repo, branch_name):
    '''
     creating of the new branch
    '''
    if not branch_name:
        raise Exception('branch_name is not defined')
    repo.create_head(branch_name)

def get_branches(repo, *args, **kwargs):
    ''' 
    return list of active and remote branches
    '''
    remote_branches = prepare_branch_list(repo.remotes.origin.refs, True)
    branches = prepare_branch_list(repo.branches, False)
    branches.extend(remote_branches)
    return branches

def prepare_branch_list(branches, is_remote):
    return list(map(lambda x: {'name': x.name,'is_remote': is_remote},  branches))

def delete_branches(repo, branches):
    [repo.delete_head(name) for name in branches]