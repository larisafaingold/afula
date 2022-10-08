#!/usr/bin/env python3

import os

import gitlab


def main() -> None:
    gl = gitlab.Gitlab(private_token=os.getenv("GITLAB_TOKEN"))
    runners = gl.runners.list()
    for runner in runners:
        print(gl.runners.get(id=runner.id))
    print(len(runners))


if __name__ == "__main__":
    main()
