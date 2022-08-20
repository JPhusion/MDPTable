import os
import git
import sys

def update():
    repo = git.Repo('./')
    if len(list(repo.iter_commits('master@{u}..master'))) > 0:
        repo.remotes.origin.pull()
        os.execl(sys.executable, sys.executable, *sys.argv)
