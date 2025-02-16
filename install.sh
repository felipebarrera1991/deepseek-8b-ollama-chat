# Installation script (install.sh)
# This script installs Ollama and downloads the DeepSeek 8B model.

#!/bin/bash

# Install Ollama if not already installed
if ! command -v ollama &> /dev/null
then
    echo "Installing Ollama..."
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "Ollama is already installed."
fi