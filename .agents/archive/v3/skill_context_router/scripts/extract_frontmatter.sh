#!/bin/bash

echo "=== CONTEXT ROUTER AUTOMATION ==="
echo ""
echo "[1] Extracting Specification Frontmatter from .agents/project/context/:"
find .agents/project/context -name "*.md" -exec awk '/^---$/{if(++c==2){print FILENAME; print ""; c=0; next}} c==1' {} +

echo ""
echo "[2] Discovering Local Agent Rules (.agents.md) in business-map/:"
find business-map -name ".agents.md" -exec echo -e "\nFound Local Rule: {}\nContents:" \; -exec cat {} \; -exec echo "---" \;
