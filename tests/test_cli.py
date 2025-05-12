#!/usr/bin/env python3

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 The Linux Foundation

import os
import subprocess
import sys
from osc_github_devops.cli import app


def test_help_empty(runner):
    try:
        result = runner.invoke(app, [])
    except TypeError:
        assert result.exit_code == 1
        assert (
            "Parameter.make_metavar() missing 1 required positional argument: 'ctx'"
            in result.stderr
        )


def test_hello(runner):
    result = runner.invoke(app, ["hello", "Matt"])
    assert result.exit_code == 0
    assert "Hello Matt" in result.stdout


def test_dinosaur(runner):
    """Test unicode characters like 🦖."""
    result = runner.invoke(app, ["hello", "🦖"])
    assert result.exit_code == 0
    assert "Hello 🦖" in result.stdout


def test_hello_empty(runner):
    try:
        result = runner.invoke(app, ["goodbye"])
    except TypeError:
        assert result.exit_code == 2
        assert (
            "TyperArgument.make_metavar() takes 1 positional argument but 2 were given"
            in result.stderr
        )


def test_goodbye(runner):
    result = runner.invoke(app, ["goodbye", "Xv"])
    assert result.exit_code == 0
    assert "Bye Xv!" in result.stdout


def test_goodbye_formal(runner):
    result = runner.invoke(app, ["goodbye", "Xv", "--formal"])
    assert result.exit_code == 0
    assert "Goodbye Ms. Xv. Have a good day." in result.stdout


def test_goodbye_empty(runner):
    try:
        result = runner.invoke(app, ["goodbye"])
    except TypeError:
        assert result.exit_code == 2
        assert (
            "TyperArgument.make_metavar() takes 1 positional argument but 2 were given"
            in result.stderr
        )


def test_script_completion_run():
    file_path = os.path.normpath("src/osc_github_devops/cli.py")
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", "-m", "typer", file_path, "run"],
        capture_output=True,
        encoding="utf-8",
    )
    assert "" in result.stdout
