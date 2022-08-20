import os
import git
import sys

def update():
    repo = git.Repo('./')
    # print(repo.iter_commits('master..origin/master'))
    if repo.iter_commits('master..origin/master'):
        repo.remotes.origin.pull()
        os.execl(sys.executable, sys.executable, *sys.argv)
