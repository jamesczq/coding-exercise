"""
Compute disk usage of a folder that may contain subfolders and files.

Created on Sat Jun 25 2022
"""

import os


def disk_usage(path: str, show_trace=False) -> float:
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath, show_trace=show_trace)
    if show_trace:
        print(f"{total:<7}", path)
    return total


def main():
    cwd = os.getcwd()
    print(cwd)
    disk_usage(cwd, show_trace=True)


if __name__ == "__main__":
    main()
