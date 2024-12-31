<!--
[comment]: # SPDX-License-Identifier: Apache-2.0
[comment]: # SPDX-FileCopyrightText: 2024 The Linux Foundation
-->

# ⛔️ Linting Action

This action is designed to run as a standalone linting step. This is helpful
for tools that do not run well (or cannot run) under the GitHub marketplace
pre-commit.ci application.

## linting-action

## Usage Example

Can be called as a workflow step with:

```yaml
steps:
  - name: Linting action
    # yamllint disable-line rule:line-length
    uses: os-climate/osc-github-devops/.github/actions/linting-action@main
```

An example reusable workflow implementation:

```yaml
---
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2024 The Linux Foundation

name: "⛔️ [R] Standalone Linting"

# yamllint disable-line rule:truthy
on:
  workflow_call:

permissions: {}

jobs:
  linting:
    name: "Standalone linting check"
    runs-on: "ubuntu-24.04"
    permissions:
      contents: read
    steps:
      - name: Linting action
        # yamllint disable-line rule:line-length
        uses: os-climate/osc-github-devops/.github/actions/linting-action@main
```

## Inputs

<!-- markdownlint-disable MD013 -->

| Variable Name     | Required | Default											  											  											  				    |
| ----------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CONFIG_URL        | False    | [pre-commit-config.yaml](https://raw.githubusercontent.com/os-climate/osc-github-devops/refs/heads/main/.github/actions/linting-action/pre-commit-config.yaml) |
| DEPENDENCIES_URL  | False    | [requirements.txt](https://raw.githubusercontent.com/os-climate/osc-github-devops/refs/heads/main/linting/requirements.txt)                                    |

<!-- markdownlint-enable MD013 -->
