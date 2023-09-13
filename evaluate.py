def evaluate_repositories(repos):
    scores={}
    for repo in repos:
        code_files=filter_code_files(repo)
        repo_score=0
        for file in code_files:
            if file.endswith('.ipynb'):
                code=extract_code_from_notebook(file)
            else:
                code=file
            repo_score+=access_code_complexity(code)
        scores[repo['name']]=repo_score
    return max(scores,key-scores.get)