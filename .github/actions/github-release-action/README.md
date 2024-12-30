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

| Variable Name     | Required | Default   | Description                                 |
| ----------------- | -------- | --------- | ------------------------------------------- |
| BUILD_TAG         | True     | N/A       | Fixed preamble/string to embed/inject       |
| GITHUB_TOKEN      | True     | N/A       | Mandatory token for content write access    |
| PROJECT_NAME      | False    | See Below | Project/product name                        |
| RELEASE_TITLE     | False    | See Below | Title for the release                       |
| PRERELEASE        | False    | False     | Marks the release as a development release  |
| ARTEFACT_LOCATION | False    | None      | When not set, no artefacts will be packaged |
| MAKE_LATEST       | False    | True      | Marks the release as the latest release     |

<!-- markdownlint-enable MD013 -->

Note: GITHUB_TOKEN requires repository write permissions to create a release

### Project Name

When not provided, the project/product title will default to the repository name.

### Release Title

When not explicitly provided, the release title will be set to the compound value:

`[Project Name] [Build Tag]`

So, when the following values are enumerated by the release action:

```console
repository = osc-github-devops
build_tag  = v1.0.1
```

The GitHub release title would be presented as:

osc-github-devops v1.0.1
