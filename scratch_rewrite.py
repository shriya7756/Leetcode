import subprocess
import os

def run(cmd):
    res = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if res.returncode != 0:
        print(f"Error running: {cmd}\n{res.stderr}")
        exit(1)
    return res.stdout.strip()

def main():
    commits = run("git log --reverse --format=%H main").split('\n')

    # Checkout first commit
    print(f"Checking out first commit: {commits[0]}")
    run(f"git checkout {commits[0]}")

    for i, commit in enumerate(commits):
        if i > 0:
            print(f"Cherry-picking {commit}")
            # If there's a conflict or empty commit, cherry-pick might fail.
            # Usually for simple history, it's fine.
            res = subprocess.run(f"git cherry-pick {commit}", shell=True, text=True, capture_output=True)
            if res.returncode != 0:
                print(f"Error cherry-picking {commit}:\n{res.stderr}\n{res.stdout}")
                # Sometimes cherry-pick fails if it's an empty commit. We can skip.
                if "empty commit" in res.stderr or "empty commit" in res.stdout or "allow-empty" in res.stderr:
                    run(f"git cherry-pick --skip")
                    continue
                else:
                    exit(1)
        
        msg = run("git log -1 --format=%B HEAD")
        files = run("git show --name-only --format= HEAD").strip().split('\n')
        files = [f for f in files if f]
        
        skip = False
        if len(files) == 1 and files[0] in msg:
            skip = True
        if "Files: " in msg:
            skip = True
            
        if not skip and len(files) > 0:
            new_msg = f"{msg.strip()}\n\nFiles: {', '.join(files)}"
            with open("temp_msg.txt", "w") as f:
                f.write(new_msg)
            run("git commit --amend -F temp_msg.txt")

    # Move main to here
    print("Updating main branch")
    run("git branch -f main HEAD")
    run("git checkout main")
    print("Done")

if __name__ == "__main__":
    main()
