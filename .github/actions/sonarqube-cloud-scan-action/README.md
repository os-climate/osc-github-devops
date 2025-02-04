<!--
[comment]: # SPDX-License-Identifier: Apache-2.0
[comment]: # SPDX-FileCopyrightText: 2024 The Linux Foundation
-->

# 🔐 SonarQube Cloud Scan

Performs a SonarQube Cloud security scan of a given repository's code base.

Uploads the results to either the cloud service or an on-premise/hosted server.

## sonarqube-cloud-scan-action

## Usage Example: Action

<!-- markdownlint-disable MD013 -->

```yaml
# Scan results are found at: https://sonarcloud.io/login
sonarqube-cloud:
  name: "SonarQube Cloud Scan"
  runs-on: ubuntu-24.04
  permissions:
    # Needed to upload the results to code-scanning dashboard.
    security-events: write
    # Needed to publish results and get a badge (see publish_results below).
    id-token: write
    # Uncomment the permissions below if installing in a private repository.
    # contents: read
    # actions: read
  steps:
    - name: "SonarQube Cloud Scan"
      # yamllint disable-line rule:line-length
      uses: os-climate/osc-github-devops/.github/actions/sonarqube-cloud-scan-action@main # 2025-02-04
      with:
        SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

<!-- markdownlint-enable MD013 -->

## Usage Example: Reusable Workflow

See: <https://github.com/lfit/releng-reusable-workflows/blob/main/.github/workflows/reuse-sonarqube-cloud.yaml>

# Upstream Documentation

See: <https://github.com/SonarSource/sonarqube-scan-action>

For information on the build wrapper for C language based projects:

<https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/c-family/prerequisites/#using-build-wrapper>

## Inputs

<!-- markdownlint-disable MD013 -->

| Variable Name         | Required | Default     | Description                                            |
| --------------------- | -------- | ----------- | ------------------------------------------------------ |
| SONAR_TOKEN           | True     | N/A         | Mandatory authentication token to upload results       |
| SONAR_ROOT_CERT       | False    | N/A         | PEM encoded server root certificate (for HTTPS upload) |
| BUILD_WRAPPER_URL     | False    | N/A         | Download location of build wrapper/shell script        |
| BUILD_WRAPPER_OUT_DIR | False    | N/A         | Local filesystem location of build artefacts           |
| LC_ALL                | False    | en_US.UTF-8 | Locale for code base (if not covered by en_US.UTF-8)   |

<!-- markdownlint-enable MD013 -->
