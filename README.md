# DeepSeek 8B Chatbot with Ollama

This repository provides a chatbot powered by the **DeepSeek 8B** model, running locally using **Ollama** and a **Streamlit UI**.

## 🚀 Features
- **Runs Locally**: No cloud dependencies.
- **DeepSeek 8B Model**: Optimized for interactive conversations.
- **Simple Setup**: Install dependencies and start chatting.
- **Streamlit-based UI**: Easy-to-use interface for chat interactions.

## 🛠️ Installation
### Prerequisites
- **Python 3.8+** is required.
- **Ollama** must be installed to run the model.

### Setup Instructions
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/deepseek-8b-ollama-chat.git
   cd deepseek-8b-ollama-chat
   ```

2. Run the installation script:
   ```sh
   chmod +x install.sh && ./install.sh
   ```

3. Install required Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Start the chatbot:
   ```sh
   python chat_deepseek.py
   ```

## Usage
- Enter messages into the chat interface.
- The chatbot will respond using the DeepSeek 8B model.
- Runs locally with no external API calls.

## Troubleshooting
- Ensure Ollama is running:
  ```sh
  ollama serve
  ```
- If the model isn't loading, try pulling again:
  ```sh
  ollama pull deepseek-r1:8b
  ```

## 📌 Notes
- The chatbot runs on `http://localhost:8501` by default.
- Make sure Ollama is running before starting the chatbot.

## License
This project is open-source and available under the MIT License.
