<!--
[comment]: # SPDX-License-Identifier: Apache-2.0
[comment]: # SPDX-FileCopyrightText: 2024 The Linux Foundation
-->

# 🔐 Scorecard Auditing

Implements [OpenSSF](https://openssf.org/) Scorecard reports.

Audits the contents of a given GitHub repository for standard best practices.
Provides detailed security reporting and optional badging, etc.

See:

- <https://openssf.org/projects/scorecard/>
- <https://github.com/ossf/scorecard>
- <https://github.com/ossf/scorecard?tab=readme-ov-file#scorecard-github-action>

## ossf-scorecard-action

## Usage Example

```yaml
jobs:
  analysis:
    name: Scorecard Analysis
    runs-on: ubuntu-22.04
    permissions:
      # Needed to upload the results to code-scanning dashboard.
      security-events: write
      # Needed to publish results and get a badge (see publish_results below).
      id-token: write
      contents: read
      actions: read
    steps:
      - name: Scorecard Action
        uses: os-climate/osc-github-devops/.github/actions/ossf-scorecard-action@main
```
