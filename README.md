# AI File Organizer

An open-source Python tool that automatically organizes messy folders (like Downloads) into categorized directories using AI.

[繁體中文說明文件 (README_zh-TW.md)](./README_zh-TW.md)

## 🌟 Overview
This project leverages Artificial Intelligence to understand the semantic meaning of your files—whether they are documents, images, or videos—and automatically organizes them into logical folder structures. It focuses on **privacy-first** local processing and smart categorization.

## ✨ Key Features
- **Semantic Categorization**: Uses LLMs to understand file context beyond just extensions.
- **Smart Renaming**: Automatically generates descriptive filenames based on content.
- **Privacy Centric**: Designed to support local models (Ollama/Llama.cpp) to keep your data safe.
- **Automated Cleanup**: Real-time monitoring and organization of target directories.

## 🚀 Quick Start
1. **Clone the repository**:
   ```bash
   git clone https://github.com/keits/file-organizer-ai.git
   cd file-organizer-ai
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Demo**:
   ```bash
   python make_demo.py
   python main.py --dir ./demo_folder --dry-run
   ```

## 🏗️ Architecture
See [ARCHITECTURE.md](./ARCHITECTURE.md) for detailed system design and roadmap.

## 🛡️ Privacy
We prioritize your data privacy. By default, the system can be configured to use local AI models so no sensitive information leaves your machine.

---
Created with ❤️ for smart digital governance.
