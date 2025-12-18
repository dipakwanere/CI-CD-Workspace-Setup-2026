import subprocess


def run(cmd):
    subprocess.run(cmd, shell=True, check=True)


def install():
    run("pip install -r requirements.txt")


def test():
    run("pytest -vv test_hello.py")


def lint():
    run("pylint --disable=R,C hello.py")


def format():
    run("black *.py")


def all():
    install()
    lint()
    test()


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python cli.py [install|test|lint|format|all]")
        sys.exit(1)

    task = sys.argv[1]

    if task not in globals():
        print(f"Unknown task: {task}")
        sys.exit(1)

    globals()[task]()
