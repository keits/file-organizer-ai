class AIModel:
    def __init__(self, provider="mock"):
        self.provider = provider

    def ask(self, prompt):
        """
        模擬 AI 的邏輯。
        在不需要 API 的情況下，根據檔名關鍵字進行「擬真」分類。
        """
        if self.provider == "mock":
            # 模擬 AI 思考後的 JSON 回傳格式 (字串)
            # 在 Demo 時，這看起來就像是 AI 產出的結構化數據
            lines = prompt.split("\n")[1:] # 取得檔案清單
            suggestions = {}
            
            for file in lines:
                f_lower = file.lower()
                if any(k in f_lower for k in ["invoice", "bill", "發票", "帳單"]):
                    suggestions[file] = "財務單據"
                elif any(k in f_lower for k in ["jpg", "png", "jpeg", "img"]):
                    suggestions[file] = "多媒體_圖片"
                elif any(k in f_lower for k in ["pdf", "docx", "txt", "doc"]):
                    suggestions[file] = "文獻檔案"
                elif any(k in f_lower for k in ["mp4", "mov", "avi"]):
                    suggestions[file] = "多媒體_影片"
                else:
                    suggestions[file] = "一般文件"
            
            return suggestions
        
        return {}
