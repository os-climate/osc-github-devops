# Generates a synthetic Gerrit "Change-Id" string

Returns a unique value/string to be inserted in GIT COMMIT messages.

For further details, check the Gerrit documentation:

[https://gerrit-review.googlesource.com/Documentation/user-changeid.html](https://gerrit-review.googlesource.com/Documentation/user-changeid.html)

An example line from a commit message would look like:

    Change-Id: Ic8aaa0728a43936cd4c6e1ed590e01ba8f0fbf5b

## Outputs

This action generates two strings that can be used, exporting them to the
environment and also outputting them to be used explicitly in other steps.

| Variable        | Example Value                                        |
| --------------- | ---------------------------------------------------- |
| CHANGE_ID_LINE  | Change-Id: Ic8aaa0728a43936cd4c6e1ed590e01ba8f0fbf5b |
| CHANGE_ID_VALUE | Ic8aaa0728a43936cd4c6e1ed590e01ba8f0fbf5b            |

<!--
[comment]: # SPDX-License-Identifier: Apache-2.0
[comment]: # SPDX-FileCopyrightText: 2024 The Linux Foundation
-->
