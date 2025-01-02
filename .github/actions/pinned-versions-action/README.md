<!--
[comment]: # SPDX-License-Identifier: Apache-2.0
[comment]: # SPDX-FileCopyrightText: 2024 The Linux Foundation
-->

# 📌 Actions Pinned Versions

Audits GitHub actions/workflows to ensure calls are pinned to SHA commit values.

## pinned-versions-action

## Recommended Event Triggers

```yaml
on:
  workflow_dispatch:
  pull_request:
    branches:
      - main
      - master
    paths: [".github/**"]
```

## Usage Example

```yaml
jobs:
  check-actions:
    name: Pinned Versions
    runs-on: ubuntu-22.04
    permissions:
      contents: read
    steps:
      - name: Check Pinned Versions
        uses: os-climate/osc-github-devops/.github/actions/pinned-versions-action@main
```

## Behaviour

### Pull Requests

When triggered against un-merged pull requests, will audit the change for any
calls to GitHub actions/workflows that are not pinned to a SHA commit value.
This only scans files in the pull request, and will NOT block merges where
GitHub actions elsewhere in the repository have not been pinned to SHA/commit
values.

### Manual Invocation

Operates differently when explicitly called using "workflow_dispatch" trigger.
Will scan the entire repository for action/workflow calls and report results.
