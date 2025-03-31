<!--
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 The Linux Foundation
-->

# 🐍 Python Dependency Audit

Check a Python project's dependencies for known security vulnerabilities.

## python-audit-action

## Usage Example

<!-- markdownlint-disable MD046 -->

Below is a sample matrix job configuration for this action:

```yaml
  python-audit:
    name: "Python Audit"
    runs-on: "ubuntu-24.04"
    needs:
      - python-build
    # Matrix job
    strategy:
      fail-fast: false
      matrix: ${{ fromJson(needs.python-build.outputs.matrix_json) }}
    permissions:
      contents: read
    steps:
      - name: "Audit project dependencies"
        uses: lfreleng-actions/python-audit-action@main
        with:
          python_version: ${{ matrix.python-version }}
```

In the above example, a prior Python build job has run (not shown).

<!-- markdownlint-enable MD046 -->

## Inputs

<!-- markdownlint-disable MD013 -->

| Variable Name   | Required | Default | Description                                                 |
| --------------- | -------- | ------- | ----------------------------------------------------------- |
| PYTHON_VERSION  | True     | N/A     | Matrix job Python version                                   |
| ARTEFACT_NAME   | False    |         | Build artefacts from previous job(s) have this name/label   |
| ARTEFACT_PATH   | False    | "dist"  | Build artefacts will download to this folder/directory      |
| NEVER_FAIL      | False    | False   | Even if a test fails, the workflow will NOT stop on error   |
| ARTEFACT_PATH   | False    | "dist"  | Stores the test coverage report bundle as an artefact       |
| SUMMARY         | False    | True    | Whether pypa/gh-action-pip-audit generates summary output   |
| PATH_PREFIX     | False    | ""      | Path/directory to Python project code                       |

<!-- markdownlint-enable MD013 -->

## Audit Implementation

The audit process uses an external public action:

[https://github.com/pypa/gh-action-pip-audit](https://github.com/pypa/gh-action-pip-audit)
