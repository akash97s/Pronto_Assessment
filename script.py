from git import Repo
from datetime import datetime, timedelta
import sys


def git_status(git_dir): 
    try:
        # Open existing repo
        repo = Repo(git_dir)
    except:
        print("Git repo is not present/ not a git repo")
        return

    # 1. Active branch
    print("active branch: ", repo.active_branch)
    print('------------------------------------------')

    # 2. Check if contents have been modified
    print("local changes: ", len(repo.git.diff()) > 0 )
    print('------------------------------------------')

    # 3. Current head commit was authored in the last week
    commits = list(repo.iter_commits(repo.active_branch ))
    if len(commits) == 0:
        print("No commits in current branch")
        return

    currentAuthoredDate = commits[0].authored_datetime.date()
    lastWeekStartDate = (datetime.now() - timedelta(days = 7)).date()
    lastWeekEndDate = (datetime.now().date() )
    print("recent commit: ", (lastWeekStartDate <= currentAuthoredDate and currentAuthoredDate <= lastWeekEndDate) )
    print('------------------------------------------')

    # 4. Current head commit was authored by Rufus
    print("blame Rufus: ", str(commits[0].author) == "Rufus")


if __name__=="__main__":
    git_status(sys.argv[1])