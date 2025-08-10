#!/bin/bash

echo "Running setup.sh: downloading spaCy transformer model..."

python -m spacy download en_core_web_trf

if [ $? -eq 0 ]; then
  echo "Model downloaded successfully."
else
  echo "Failed to download the model."
  exit 1
fi
