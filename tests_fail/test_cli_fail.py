#!/usr/bin/env python3

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 The Linux Foundation

from osc_github_devops.cli import app


def test_wrong(runner):
    """Example for a test that fails."""
    result = runner.invoke(app, ["wrong"])
    assert result.exit_code == 2
    assert "Missing argument 'NAME'" in result.stdout
