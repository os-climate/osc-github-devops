<!--
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2024 The Linux Foundation
-->

# 🗞️ Report on last GIT commit

Extracts information and changes from the last two commits

## git-last-commit-action

## Recommended Event Triggers

```yaml
on:
    workflow_dispatch:
    push:
        branches:
            - main
            - master
        paths:
            - "**"
```

## Usage Example

<!-- markdownlint-disable MD013 -->

```yaml
jobs:
    pull-request-merged:
        name: "Pull Request Merged"
        runs-on: "ubuntu-24.04"
        permissions:
            contents: read
        steps:
            # yamllint disable-line rule:line-length
            - uses: os-climate/osc-github-devops/.github/actions/git-last-commit@ea8bbd5f4f817abe64b2498e0f1393ca15b86c0e # v1.0.0
```

<!-- markdownlint-enable MD013 -->

## Behaviour

When run on a merged pull request, will report on the content and changes in
the last two commits.
