<!--
[comment]: # SPDX-License-Identifier: Apache-2.0
[comment]: # SPDX-FileCopyrightText: 2024 The Linux Foundation
-->

# 📦 PyPI Package Check

Checks the Python package index for the presence of a package (and
optionally a specific release/version)

## pypi-version-check-action

## Usage Example

Pass the index query URL, along with Python package name and optionally the
package release/version to check.

```yaml
steps:
  - name: "Checking package index for build/release"
    id: check-package-index
    # yamllint disable-line rule:line-length
    uses: os-climate/osc-github-devops/.github/actions/pypi-version-check-action@main
    with:
      index_url: "${{ env.base_url }}/simple"
      package_name: "/${{ steps.naming.outputs.python_project_name }}"
      package_version: "/${{ inputs.build_tag }}/"
```

Query URL examples:

- TestPyPI <https://test.pypi.org/simple>
- PyPI <https://pypi.org/simple>

## Inputs

<!-- markdownlint-disable MD013 -->

| Variable Name   | Required | Description                           |
| --------------- | -------- | ------------------------------------- |
| PACKAGE_NAME    | True     | Name of Python package to check       |
| PACKAGE_VERSION | False    | Optional release/version to check     |
| INDEX_URL       | False    | Defaults to <https://pypi.org/simple> |

<!-- markdownlint-enable MD013 -->

## Outputs

<!-- markdownlint-disable MD013 -->

| Variable Name | Mandatory | Description                                   |
| ------------- | --------- | --------------------------------------------- |
| PACKAGE_MATCH | True      | Always reports the presence of the project    |
| VERSION_MATCH | False     | Only reports a match when version is provided |

<!-- markdownlint-enable MD013 -->
