#!/bin/bash

expected="fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7"

for file in files/*; do
    # Compute the SHA-256 hash for the current file
    computed=$(sha256sum "$file" | awk '{print $1}')

    if [[ $expected == $computed ]]; then
        # Print the filename and the computed checksum
        echo -e "Match found: $(basename "$file")\nComputed checksum: $computed"
    else
        echo "Doesn't match: $(basename "$file")"
    fi
done

