#!/usr/bin/env python3

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2024 The Linux Foundation
import pytest

from typer.testing import CliRunner


@pytest.fixture(scope="module")
def runner():
    return CliRunner()
