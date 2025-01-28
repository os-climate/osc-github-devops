# OS-Climate GitHub Actions and Reusable Workflows

<!-- prettier-ignore-start -->
<!-- markdownlint-disable-next-line MD013 -->
[![OS-Climate](https://img.shields.io/badge/OS-Climate-blue)](https://os-climate.org/) [![Slack](https://img.shields.io/badge/slack-osclimate-blue.svg?logo=slack)](https://os-climate.slack.com) [![Source Code](https://img.shields.io/badge/GitHub-100000?logo=github&logoColor=white&color=blue)](https://github.com/os-climate/osc-github-devops) [![PyPI](https://img.shields.io/pypi/v/osc-github-devops?logo=python&logoColor=white&color=blue)](https://pypi.org/project/osc-github-devops) [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

<!-- markdownlint-disable-next-line MD013 -->
 [![pre-commit.ci status badge]][pre-commit.ci results page] [![TestPyPI](https://img.shields.io/pypi/v/osc-github-devops?logo=python&label=TestPyPi&logoColor=white&color=32C955&pypiBaseUrl=https://test.pypi.org)](https://test.pypi.org/project/osc-github-devops) [![🧪 GitHub Actions CI/CD workflow tests badge]][GHA workflow runs list] [![🔐 CodeQL](https://github.com/os-climate/osc-github-devops/actions/workflows/codeql.yml/badge.svg)](https://github.com/os-climate/osc-github-devops/actions/workflows/codeql.yml) [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/os-climate/osc-github-devops/badge)](https://scorecard.dev/viewer/?uri=github.com/os-climate/osc-github-devops)
<!-- prettier-ignore-end -->

## Composite actions and reusable workflows for Python projects

### OS-Climate and FINOS are both Linux Foundation projects

- [https://os-climate.org/](https://os-climate.org/)
- [https://www.finos.org/](https://www.finos.org/)
- [https://www.linuxfoundation.org/](https://www.linuxfoundation.org/)

### Description

This repository contains a number of GitHub composite actions, reusable workflows,
and workflows. The purpose of these is to provide small modular components and
larger pieces of shared DevOps functionality which may be helpful to the OS-Climate
community, and indeed other open-source projects. Right now, the current focus is
on Python and the tooling around Python projects, since that is the language
currently used for the vast majority of OS-Climate projects and repositories.

### Python Template Code

The repository also contains some sample Python code which is published to the Python
package index repository and is installable with the Python "pip" command. The
dummy sample project ensures Python packages can be built, tested and published
using the supplied GitHub composite actions, reusable workflows, and workflows.

Relevant link to the Python package index project page:

- [osc-github-devops](https://pypi.org/project/osc-github-devops)

Detailed documentation will be supplied here, once further development is done.

In the meantime, here is some general documentation covering the relevant topics:

- [Reusing workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)
- [How to start using reusable workflows with GitHub Actions](https://github.blog/2022-02-10-using-reusable-workflows-github-actions/)
- [Create reusable workflows in GitHub Actions](https://resources.github.com/learn/pathways/automation/intermediate/create-reusable-workflows-in-github-actions/)
- [The Ultimate Guide to GitHub Reusable Workflows](https://www.dhiwise.com/post/the-ultimate-guide-to-github-reusable-workflows-maximize-efficiency-and-collaboration)

<!--
[comment]: # SPDX-License-Identifier: Apache-2.0
[comment]: # SPDX-FileCopyrightText: 2024 The Linux Foundation
-->

<!--
[comment]: # Section below is sourced by the badges displayed under the project heading
-->

[🧪 GitHub Actions CI/CD workflow tests badge]: https://github.com/os-climate/osc-github-devops/actions/workflows/merge-build-test-release.yaml/badge.svg?branch=main&event=push
[GHA workflow runs list]: https://github.com/os-climate/osc-github-devops/actions/workflows/merge-build-test-release.yaml?query=branch%3Amain
[pre-commit.ci results page]: https://results.pre-commit.ci/latest/github/os-climate/osc-github-devops/main
[pre-commit.ci status badge]: https://results.pre-commit.ci/badge/github/os-climate/osc-github-devops/main.svg
