<!--
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 The Linux Foundation
-->

# 🐍 Test Python Project [Matrix Job]

Tests a Python project, generates coverage reports.

## python-project-test-matrix

## Usage Example

<!-- markdownlint-disable MD046 -->

Below is a sample matrix job configuration for this action:

```yaml
  python-tests:
    name: "Python Test"
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
      - name: "Test Python project"
        uses: lfreleng-actions/python-project-test-matrix@main
        with:
          python_version: ${{ matrix.python-version }}
          report_artefact: true
```

In the above example, a prior Python build job has run (not shown).

<!-- markdownlint-enable MD046 -->

## Inputs

<!-- markdownlint-disable MD013 -->

| Variable Name   | Required | Description                                               |
| --------------- | -------- | --------------------------------------------------------- |
| PYTHON_VERSION  | True     | Matrix job Python version                                 |
| NEVER_FAIL      | False    | Even if a test fails, the workflow will NOT stop on error |
| REPORT_ARTEFACT | False    | Stores the test coverage report bundle as an artefact     |
| PATH_PREFIX     | False    | Path/directory to Python project code                     |

<!-- markdownlint-enable MD013 -->

## Coverage Reports

The test action will create HTML coverage reports as ZIP file bundles.

Upload coverage reports as artefacts by setting the REPORT_ARTEFACT input.
