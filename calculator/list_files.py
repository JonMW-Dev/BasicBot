import os

for root, dirs, files in os.walk("."):
    # skip hidden directories
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    for f in files:
        print(os.path.join(root, f))
