#!/bin/bash
# compiler.sh
OUTPUT="ai_context.md"

echo "# Codebase Context Document" > $OUTPUT

# 1. Add the structure
echo "## Directory Tree" >> $OUTPUT
find . -type d -not -path "*/\.*" | sort >> $OUTPUT

# 2. Add all Interfaces, Traits, or Base Classes ONLY
echo "## Core Interfaces" >> $OUTPUT
find . -name "*interface*.py" -o -name "*_types.go" | while read file; do
    echo "### File: $file" >> $OUTPUT
    echo '```' >> $OUTPUT
    cat "$file" >> $OUTPUT
    echo '```' >> $OUTPUT
done
