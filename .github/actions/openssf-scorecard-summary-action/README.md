<!--
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 The Linux Foundation
-->

# 📄 OpenSSF Scorecard Summary Output

Provides summary output with a URL/link to the scorecard report.

Note: The upstream action neglects to implement this feature.

## openssf-scorecard-summary-action

## Implementation Notes

The summary output must be called/referenced in a separate job section. This is
because the OpenSSF upstream action performs a number of security checks before
it will upload any results. Any additional calls in the calling workflow will
be audited and can block the reporting of results. Care must therefore be taken
in the implementation of any surrounding action/workflow code.

## Usage Example: Reusable Workflow

<!-- markdownlint-disable MD013 -->

```yaml
jobs:
  openssf-scorecard: [...]

  # Summary output MUST be in a separate job, as per the ossf/scorecard-action documentation
  summary-output:
    name: "Link"
    needs: openssf-scorecard
    runs-on: ubuntu-24.04
    steps:
      - name: "Provide link to scorecard"
        # The upstream action does not provide any useful summary output
        # the action below adds a hyperlink to the OpenSSF Scorecard/report
        uses: lfit/releng-reusable-workflows/.github/actions/openssf-scorecard-summary-action@main
```

<!-- markdownlint-enable MD013 -->

See: <https://github.com/lfit/releng-reusable-workflows/blob/main/.github/workflows/reuse-openssf-scorecard.yaml>
