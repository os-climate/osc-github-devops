<!--
SPDX-License-Identifier: Apache-2.0
SPDX-FileCopyrightText: 2024 The Linux Foundation
-->

# Check for Python Dynamic Versioning

Parses pyproject.toml to check if the project uses dynamic versioning.

## python-dynamic-version-action

## Usage Example

```yaml
- name: "Check for dynamic versioning"
  uses: lfit/releng-reusable-workflows/.github/actions/python-dynamic-version-action@main
```

## Outputs

<!-- markdownlint-disable MD013 -->

| Variable Name   | Description                              |
| --------------- | ---------------------------------------- |
| DYNAMIC_VERSION | Set true when dynamic versioning enabled |

<!-- markdownlint-enable MD013 -->
