<!--
SPDX-License-Identifier: Apache-2.0
SPDX-FileCopyrightText: 2024 The Linux Foundation
-->

# 📦 GitHub List Releases

Lists all the releases for the current repository.

## github-list-releases-action

## Usage Example

This action has no inputs; it provides results for the current repository.

```yaml
steps:
    - name: "GitHub List Releases"
      uses: os-climate/osc-github-devops/.github/actions/github-list-releases-action@main
```

## Inputs

<!-- markdownlint-disable MD013 -->

| Variable Name | Required | Default | Description                                   |
| ------------- | -------- | ------- | --------------------------------------------- |
| TAG           | False    | N/A     | Checks if release exists for the provided tag |

<!-- markdownlint-enable MD013 -->

## Outputs

<!-- markdownlint-disable MD013 -->

| Variable Name | Mandatory | Description                                                       |
| ------------- | --------- | ----------------------------------------------------------------- |
| RELEASED      | False     | When tag provided as input, set true if a matching release exists |

<!-- markdownlint-enable MD013 -->

Example output:

```json

```
