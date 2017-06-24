from git import Repo

repo_dir = 'MSBIC'
repo = Repo(repo_dir)
file_list = [
    '/home/abhishek/Pictures/Ananse.png'
]
commit_message = 'Add file programmatically'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()