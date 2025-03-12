<!--
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2024 The Linux Foundation
-->

# 🛠️ Python Project Metadata

Extracts Python project metadata from a repository.

## python-project-metadata-action

## Usage Example

<!-- markdownlint-disable MD013 -->

```yaml
  - name: "Get project supported Python versions"
    uses: lfit/releng-reusable-workflows/.github/actions/python-supported-versions-action@main
```

<!-- markdownlint-enable MD013 -->

## Outputs

<!-- markdownlint-disable MD013 -->

| Variable Name         | Description                                              |
| --------------------- | -------------------------------------------------------- |
| PYTHON_PROJECT_FILE   | File used to define/describe the project                 |
| PYTHON_PROJECT_NAME   | The name of the Python project                           |
| PYTHON_PACKAGE_NAME   | The name of the Python package                           |
| PROJECT_MATCH_PACKAGE | Set true when the project and package name match         |
| PROJECT_MATCH_REPO    | Set true when the project name and repository name match |
| VERSIONING_TYPE       | Can be either static or dynamic (determined by tags)     |
| BUILD_PYTHON          | Most recent Python version supported by project          |
| MATRIX_JSON           | All Python versions supported by project as JSON string  |

Python package names can be different from project names.

Note: dashes in the project name get replaced with underscores

<!-- markdownlint-enable MD013 -->

## Workflow Output Example

For a Python project with the content below in its pyproject.toml file:

```console
requires-python = "<3.13,>=3.10"
readme = "README.md"
license = { text = "Apache-2.0" }
keywords = ["Python", "Tool"]
classifiers = [
  "License :: OSI Approved :: Apache Software License",
  "Operating System :: Unix",
  "Programming Language :: Python",
  "Programming Language :: Python :: 3",
  "Programming Language :: Python :: 3.12",
  "Programming Language :: Python :: 3.11",
  "Programming Language :: Python :: 3.10",
]
```

A workflow calling this action will produce the output below:

```console
Build Python: 3.12 💬
Matrix JSON: {"python-version": ["3.10","3.11","3.12"]}
```

## Implementation Details

This action produces output by parsing the lines containing:

```console
  "Programming Language :: Python :: 3.12",
  "Programming Language :: Python :: 3.11",
  "Programming Language :: Python :: 3.10",
```

This may be different from other tooling that parses the pyproject.toml file
for information, such as GitHub's actions/setup-python. That appears to use
the "requires-python" string. Parsing that would require logic beyond the
current scope of this action, but may be desirable to improve behavioural
consistency.
