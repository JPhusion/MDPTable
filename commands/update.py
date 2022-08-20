import os
import git
import sys

def update():
    repo = git.Repo('./')
    repo.remotes.origin.pull()
    os.execl(sys.executable, sys.executable, *sys.argv)
