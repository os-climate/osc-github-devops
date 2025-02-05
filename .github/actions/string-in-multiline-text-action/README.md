<!--
[comment]: # SPDX-License-Identifier: Apache-2.0
[comment]: # SPDX-FileCopyrightText: 2024 The Linux Foundation
-->

# 📃 Multi-line Text String Matching

Checks for the presence of a string in multiline text.

Supports a number of optional matching parameters:

- Plain or base64 encoded multiline strings accepted as input
- Case-insensitive matching
- Sub-string matching

## Usage Example

<!-- markdownlint-disable MD013 -->

```yaml
steps:
    - name: "Check multiline text string for TODO"
      id: check-todo
      uses: os-climate/osc-github-devops/.github/actions/string-in-multiline-text@main
      with:
          string: "TODO"
          multiline-text: "${{ env.multiline_text }}"
          case_insensitive: "true"
```

<!-- markdownlint-enable MD013 -->
