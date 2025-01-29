#!/usr/bin/env bash

# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 The Linux Foundation <matthew.watkins@linuxfoundation.org>

# Checks whether GitHub actions are referenced in this repository

set -eu -o pipefail

GITHUB_ACTIONS=$(ls actions)

for ACTION in $GITHUB_ACTIONS; do
    # Recursive grep to check for references
    if ! (grep -r "$ACTION" | grep -vq 'lfit/releng-reusable-workflows'); then
        echo "Not referenced: $ACTION"
    fi
done
