<!--
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2024 The Linux Foundation
-->

# 📦 Verify Build Artefacts with Twine

Call before package publishing to ensure validity of Python build artefacts.

## python-project-metadata-action

## Usage Example

<!-- markdownlint-disable MD013 -->

```yaml
  - name: "Verify Python build artefacts with Twine"
    uses: lfit/releng-reusable-workflows/.github/actions/python-twine-check-action@main
```

<!-- markdownlint-enable MD013 -->

## Inputs

<!-- markdownlint-disable MD013 -->

| Variable Name | Description                    | Default |
| ------------- | ------------------------------ | ------- |
| PATH          | Path to Python build artefacts | dist    |

<!-- markdownlint-enable MD013 -->

## Outputs

This action has no outputs, but will exit with an error when artefact
validation fails.

## Notes

When calling this action from a separate job, perform a download artefacts step
before calling the action to ensure build products are available.

## Action Output Example

```console
Run # Verify artefacts with Twine
Installing: twineRunning: twine check dist/*
Checking dist/osc_github_devops-0.1.28.dev1-py3-none-any.whl: PASSED
Checking dist/osc_github_devops-0.1.28.dev1.tar.gz: PASSED
Verified build artefacts with Twine ✅
```
