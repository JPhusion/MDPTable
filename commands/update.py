import os
import git
import sys

def update():
    repo = git.Repo('./')
    if list(repo.iter_commits('main..main@{u}')):
        repo.remotes.origin.pull()
        os.execl(sys.executable, sys.executable, *sys.argv)
