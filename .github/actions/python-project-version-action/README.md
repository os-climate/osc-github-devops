<!--
SPDX-License-Identifier: Apache-2.0
SPDX-FileCopyrightText: 2025 The Linux Foundation
-->

# 🐍 Python Project Current Version

Returns the current version of a Python Project declared in the metadata
description/files. Supports both pyproject.toml and setup.py locations.

## python-project-version-action

## Usage Example

An example workflow step using this action:

```yaml
  # Code checkout performed in earlier workflow step
  - name: Retrieve the current Python Project version
    uses: lfreleng-actions/python-project-version-action@main
```

## Outputs

<!-- markdownlint-disable MD013 -->

| Output Variable        | Description                                                   |
| ---------------------- | ------------------------------------------------------------- |
| PYTHON_PROJECT_VERSION | Current version of the Python Project                         |
| SOURCE                 | Project metadata/description file [ pyproject.toml/setup.py ] |

<!-- markdownlint-enable MD013 -->
