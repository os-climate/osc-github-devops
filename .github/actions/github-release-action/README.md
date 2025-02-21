<!--
SPDX-License-Identifier: Apache-2.0
SPDX-FileCopyrightText: 2024 The Linux Foundation
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
          tag: ${{ github.ref_name }}
          github_token: ${{ secrets.GITHUB_TOKEN }}
```

## Inputs

<!-- markdownlint-disable MD013 -->

| Variable Name | Required | Default   | Description                                  |
| ------------- | -------- | --------- | -------------------------------------------- |
| TAG           | True     | N/A       | Fixed preamble/string to embed/inject        |
| GITHUB_TOKEN  | True     | N/A       | Mandatory token for content write access     |
| PROJECT_NAME  | False    | See Below | Project/product name                         |
| RELEASE_TITLE | False    | See Below | Title for the release                        |
| PRERELEASE    | False    | False     | Marks the release as a development release   |
| ARTEFACT_PATH | False    | None      | Unless set, will not package build artefacts |
| MAKE_LATEST   | False    | True      | Marks the release as the latest release      |

<!-- markdownlint-enable MD013 -->

Note: GITHUB_TOKEN requires repository write permissions to create a release

### Project Name

When not provided, the project/product title will default to the repository name.

### Release Title

When not explicitly provided, the default release title is:

`[Python Project Name] [Tag]`
