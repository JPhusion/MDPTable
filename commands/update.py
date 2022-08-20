import os
import git
import sys

def update():
    # TEST
    repo = git.Repo('./')
    print(list(repo.iter_commits('main..main@{u}')))
    print(list(repo.iter_commits('main@{u}..main')))
    if list(repo.iter_commits('main..main@{u}')):
        repo.remotes.origin.pull()
        os.execl(sys.executable, sys.executable, *sys.argv)
