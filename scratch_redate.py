import subprocess
import datetime
import os

def run(cmd, env=None):
    res = subprocess.run(cmd, shell=True, text=True, capture_output=True, env=env)
    if res.returncode != 0:
        print(f"Error running: {cmd}\n{res.stderr}")
        exit(1)
    return res.stdout.strip()

def main():
    commits = run("git log --reverse --format=%H main").split('\n')
    print(f"Checking out {commits[0]}")
    run(f"git checkout {commits[0]}")

    base_time = datetime.datetime.now() - datetime.timedelta(minutes=len(commits))
    my_env = os.environ.copy()

    for i, commit in enumerate(commits):
        if i > 0:
            print(f"Cherry-picking {commit}")
            res = subprocess.run(f"git cherry-pick {commit}", shell=True, text=True, capture_output=True)
            if res.returncode != 0:
                if "empty commit" in res.stderr or "allow-empty" in res.stderr:
                    run("git cherry-pick --skip")
                    continue
                else:
                    print(f"Error: {res.stderr}")
                    exit(1)
        
        commit_time = base_time + datetime.timedelta(minutes=i)
        time_str = commit_time.strftime("%Y-%m-%dT%H:%M:%S")
        
        my_env["GIT_COMMITTER_DATE"] = time_str
        my_env["GIT_AUTHOR_DATE"] = time_str
        
        run(f"git commit --amend --no-edit --date={time_str}", env=my_env)

    print("Updating main")
    run("git branch -f main HEAD")
    run("git checkout main")
    print("Done")

if __name__ == "__main__":
    main()
