<!--
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 The Linux Foundation
-->

# 🐍 Build Python Project

Builds a Python project, uploads build artefacts to GitHub.

Supports these optional features:

- GitHub Attestations (Build Provenance)
- SigStore Signing    (Signing of Build Artefacts)

## python-build-action

## Usage Example

<!-- markdownlint-disable MD046 -->

```yaml
  - name: "Build Python project"
    uses: lfreleng-actions/python-build-action@main
    with:
      tag: ${{ needs.repository.outputs.build_tag }}
```

<!-- markdownlint-enable MD046 -->

## Inputs

<!-- markdownlint-disable MD013 -->

| Variable Name       | Required | Description                                                |
| ------------------- | -------- | ---------------------------------------------------------- |
| ARTEFACT_PATH       | False    | Output path/directory to use for build artefacts           |
| PURGE_ARTEFACT_PATH | False    | Deletes any pre-existing content in build/target directory |
| TAG                 | False    | Version to use for Python project build artefacts          |
| ATTESTATIONS        | False    | Attest build artefacts using GitHub Attestations           |
| SIGSTORE_SIGN       | False    | Uses SigStyore application to sign binary build artefacts  |
| PATH_PREFIX         | False    | Path/directory to Python project code                      |

[Github Attestations](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds_)
[SigStore](https://www.sigstore.dev/)

<!-- markdownlint-enable MD013 -->

## Outputs

<!-- markdownlint-disable MD013 -->

| Variable Name | Description                      |
| ------------- | -------------------------------- |
| MATRIX_JSON   | Python version supported as JSON |
| ARTEFACT_NAME | Name/label for build artefacts   |
| ARTEFACT_PATH | Patch to build artefacts         |

<!-- markdownlint-enable MD013 -->

## Implementation Details

## Notes
