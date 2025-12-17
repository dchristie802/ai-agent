# AI Agent

This project is a learning exercise in building an AI agent using the Google Gemini API. The agent is designed to autonomously analyze, read, and modify code within a specific sandboxed environment using function calling.

## ⚠️ Security Warning & Disclaimer

**This project is for educational and learning purposes only.**

This program is **not** a production-ready AI agent and lacks the standard security, sandboxing, and safety features required for safe deployment. 

* **Do not distribute** this tool to others for general use.
* **Risk of Data Loss:** The agent is designed to operate within a specific, hardcoded working directory. While currently restricted to a sandbox, modifying the codebase to change this target directory can allow the agent to read, modify, or delete files anywhere on your system. 
* **User Responsibility:** You are responsible for ensuring the code is run in a safe environment. Always review the code before execution.

## 🚀 Overview

The goal of this project is to demonstrate how an AI model can leverage defined tools (functions) to interact with a local file system.

The agent operates with a specific constraint: it is limited to the `calculator` directory. This directory contains a small calculator application (provided by the [boot.dev](https://boot.dev) course) which serves as a safe sandbox for the agent to:
1.  **Read** files to understand the codebase.
2.  **Analyze** the code for logic or bugs.
3.  **Write** changes to fix issues or add features.
4.  **Return** a summary of the actions taken.

## 🛠️ Prerequisites

To run this project, you will need:
* **Python 3.x**
* **[uv](https://github.com/astral-sh/uv)** (used for dependency management and execution)
* **Google Gemini API Key**

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dchristie802/ai-agent.git
    cd ai-agent
    ```

2.  **Set up your API Key:**
    Ensure you have your Gemini API Key available in your environment variables.
    ```bash
    export GEMINI_API_KEY="your_api_key_here"
    ```

3.  **Install Dependencies:**
    This project uses `uv` to manage dependencies.
    ```bash
    uv sync
    ```

## 🏃 Usage

You interact with the agent by passing a prompt to the `main.py` script.

**Basic Example:**
Ask the agent to analyze the code.
```bash
uv run main.py "Explain how the calculator renders the result to the console."
```
**Verbose Output:**
Use the verbose flag to see the agent's internal thought process and tool usage loops:
```bash
uv run main.py "Explain how the calculator renders the result to the console." --verbose
```

## 🧪 Testing

This project includes a test suite to ensure the agent's tools (file reading, writing, etc.) are working correctly. You can run the tests with the following command:
```bash
uv run python -m unittest discover -s tests/
```

## 📚 Credits
This project was built for educational purposes and relies on the following resources:
* **Calculator Application**: The target application located in the `calculator/` directory (used as the sandbox environment) was provided by the [boot.dev](https://boot.dev) course materials.
* **AI Logic**: The agent's reasoning and code generation capabilities are powered by the [Google Gemini API](https://ai.google.dev/).


