import subprocess

examples = ["3 + 5", "10 / 4", "2 + 3 * 4", "7.5 + 2.5", "100 / 3"]
for expr in examples:
    out = subprocess.run(
        ["python", "main.py", expr],
        capture_output=True,
        text=True,
    )
    print(f"$ python main.py {expr!r}")
    print(out.stdout, end="")
    if out.stderr:
        print("STDERR:", out.stderr)
    print("-" * 30)
