#!/usr/bin/env bash

# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 The Linux Foundation <matthew.watkins@linuxfoundation.org>

# Script to check if actions are referenced in workflows

set -eu -o pipefail

GITHUB_ACTIONS=$(ls actions)

for ACTION in $GITHUB_ACTIONS; do
    # Recursive grep to check for references
    if ! (grep -rq "$ACTION"); then
        echo "Not referenced: $ACTION"
    fi
done
