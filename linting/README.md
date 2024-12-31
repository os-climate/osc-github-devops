<!--
[comment]: # SPDX-License-Identifier: Apache-2.0
[comment]: # SPDX-FileCopyrightText: 2024 The Linux Foundation
-->

# 🛠️ Standalone Linting Configuration

This folder contains a configuration file for a standalone linting setup. It is
designed to be run and invoked as a separate step from pre-commit.ci. It
exists because in certain circumstances, MyPy is unable to run correctly and
in the GitHub application and it then has to be broken out into a separate step.

## pre-commit-config.yaml

## Usage Example

See: <https://github.com/os-climate/osc-github-devops/blob/main/.github/workflows/linting.yaml>
