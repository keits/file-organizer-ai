# File Organizer AI - AI 協作規範 (GEMINI.md)

## 🎯 專案使命
建立一個「懂內容」的檔案整理系統，核心競爭力在於 **「語意理解」** 與 **「隱私保護」**。

## 🛡️ 隱私與安全限制 (最高優先級)
1. **API Key 保護**：嚴禁將 `OPENAI_API_KEY` 或任何憑證寫死在程式碼中。必須使用 `.env`。
2. **路徑脫敏**：在產出範例、日誌或 Demo 截圖時，必須將使用者的系統路徑（如 `C:\Users\keits\...`）替換為佔位符（如 `/home/user/...`）。
3. **本地模型優先**：在實作功能時，應優先考慮如何支援 Ollama 等本地端 AI 調用。

## 🏗️ 專案結構
- `core/`: 存放分類與命名的核心邏輯。
- `utils/`: 檔案處理、日誌紀錄與設定讀取。
- `models/`: 模型介面封裝（OpenAI, Ollama 等）。
- `tests/`: 單元測試與 Dummy 資料夾生成。

## 🤖 AI 協作指南
- **新功能提案**：當你要新增功能時，請先更新此檔案的 Roadmap。
- **Commit 規範**：請使用繁體中文描述 Commit message，並區分 `feat`, `fix`, `docs`。
- **文件同步**：修改程式碼邏輯後，必須同步更新 `README_zh-TW.md`。

## 📈 Roadmap (短期目標)
1. 實作 `organizer.py`：具備讀取檔名並詢問 LLM 應歸類到哪個資料夾的功能。
2. 建立 `.gitignore` 防線：排除所有實體檔案整理產出的 Log 與資料夾。
