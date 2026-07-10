#!/bin/bash

# Generates a Mermaid architecture diagram of the target directory
DIR=${1:-"business-map/src"}
OUTPUT_FILE=".agents/skills/architecture_lens/architecture.mmd"

echo "Generating Mermaid dependency diagram for $DIR..."
npx --yes dependency-cruiser --no-config --include-only "^$DIR" --output-type mermaid $DIR > $OUTPUT_FILE

echo "Diagram saved to $OUTPUT_FILE"
echo "Agents can now use 'view_file $OUTPUT_FILE' to read the visual architecture graph."
