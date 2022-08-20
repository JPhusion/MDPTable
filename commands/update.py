import os
import git
import sys

def update():
    repo = git.Repo('./')
    print(repo.git.rev_list('--left-right', '--count', f'{"main"}...{"main"}@{{u}}').split('\t')[1])
    print(repo.git.rev_list('--left-right', '--count', f'{"main"}...{"main"}@{{u}}').split('\t')[0])
    if "0" not in repo.git.rev_list('--left-right', '--count', f'{"main"}...{"main"}@{{u}}').split('\t')[1]:
        repo.remotes.origin.pull()
        os.execl(sys.executable, sys.executable, *sys.argv)
# test
