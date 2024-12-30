<!--
[comment]: # SPDX-License-Identifier: Apache-2.0
[comment]: # SPDX-FileCopyrightText: 2024 The Linux Foundation
-->

# 📦 GitHub Release

Creates a new GitHub release for a given repository

## github-release-action

## Usage Example

Pass the required server and authentication details/credentials.
Other inputs are discretionary and set to useful defaults.

```yaml
steps:
  - name: "GitHub Release"
    uses: os-climate/osc-github-devops/.github/actions/github-release-action@main
    with:
      build_tag: ${{ github.ref_name }}
      github_token: ${{ secrets.GITHUB_TOKEN }}
```

## Inputs

<!-- markdownlint-disable MD013 -->

| Variable Name     | Required | Default | Description                                 |
| ----------------- | -------- | ------- | ------------------------------------------- |
| BUILD_TAG         | True     | N/A     | Fixed preamble/string to embed/inject       |
| GITHUB_TOKEN      | True     | N/A     | Mandatory token for content write access    |
| PRERELEASE        | False    | False   | Marks the release as a development release  |
| ARTEFACT_LOCATION | False    | None    | When not set, no artefacts will be packaged |
| MAKE_LATEST       | False    | True    | Marks the release as the latest release     |

<!-- markdownlint-enable MD013 -->

Note: the GITHUB_TOKEN passed to the action must have repository write permissions
