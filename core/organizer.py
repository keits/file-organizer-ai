import os
import shutil
from models.ai_interface import AIModel

class FileOrganizer:
    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.ai = AIModel()

    def list_files(self):
        """列出資料夾內所有非隱藏檔案"""
        return [f for f in os.listdir(self.target_dir) 
                if os.path.isfile(os.path.join(self.target_dir, f)) and not f.startswith('.')]

    def generate_plan(self, files):
        """將檔案清單傳送給 AI，產出分類建議"""
        # 調用 AI 接口 (目前是模擬模式)
        prompt = "請幫我分類以下檔案：\n" + "\n".join(files)
        ai_suggestions = self.ai.ask(prompt)
        
        plan = []
        for file in files:
            # 從 AI 的建議中取得分類，若無則設為預設
            suggested_folder = ai_suggestions.get(file, "未分類_需人工確認")
            plan.append({"file": file, "to": suggested_folder})
        return plan

    def display_plan(self, plan):
        """格式化顯示分類計畫"""
        print("\n" + "-"*10 + " AI 智慧分類計畫表 " + "-"*10)
        # 按資料夾群組化顯示，看起來更專業
        grouped_plan = {}
        for item in plan:
            grouped_plan.setdefault(item['to'], []).append(item['file'])
            
        for folder, files in grouped_plan.items():
            print(f"\n📁 目標資料夾：[{folder}]")
            for file in files:
                print(f"   ├── 📄 {file}")
        print("-" * 38)

    def execute_plan(self, plan):
        """實際執行檔案搬移 (補助展示版已解鎖)"""
        for item in plan:
            src = os.path.join(self.target_dir, item['file'])
            dst_dir = os.path.join(self.target_dir, item['to'])
            
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            
            dst = os.path.join(dst_dir, item['file'])
            
            # 使用 shutil.move 比 os.rename 更安全，可跨硬碟移動
            shutil.move(src, dst)
            print(f"✅ 已成功移動: {item['file']} -> {item['to']}/")
