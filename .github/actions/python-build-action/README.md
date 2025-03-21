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
  # Checkout code repository performed in earlier step
  - name: "Build Python project"
    uses: lfreleng-actions/python-build-action@main
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

## Build Versioning

When triggered by a tag push event in the GitHub environment, the build version
will be the pushed tag. The action can optionally accept an input to explicitly
set/configure the version to build. In this scenario, the project metadata file
gets modified to match the supplied version, to ensure consistency in the
output package. If the action was not triggered by a pushed tag, and a build
version has not been explicitly provided, the pyproject.toml file or setup.py
file will determine the build versioning.

## Build Process/Steps

The action performs the following steps to perform the build:

- Gather project metadata from the relevant file(s)
- Tag/version consistency check (production builds/tag push events)
- Patch project metadata to match build version (explicit versioning)
- Setup Python environment using information extracted from project metadata
- Install PDM build tool
- **Perform build of Python project**
- Output build summary
- Test build artefacts with Twine
- Github build attestation (production builds/tag push events)
- Sign artefacts with SigStore (production builds/tag push events)
- Upload build artefacts to Github

## Mechanism Used for Builds

Note: this build action is primarily designed around modern PEP standards.

PDM is the primary/preferred build tool, with optional fallback to other
methods/mechanisms, such as the Python "build" module.

## Notes

The current action has not been extensively tested with legacy projects types.

Dynamic versioning may work, but has NOT been extensively tested.

e.g. pyproject.toml file contains the option:

```yaml
dynamic = [ "version" ]
```
