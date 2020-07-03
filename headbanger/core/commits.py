def get_commits(repo, branch_name:str):
    '''
    return first 100 commits from selected branch
    '''
    return list(repo.iter_commits(branch_name, max_count=100))