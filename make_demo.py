import os

def create_demo_files():
    demo_dir = "demo_folder"
    if not os.path.exists(demo_dir):
        os.makedirs(demo_dir)
        print(f"✨ 已建立展示資料夾: {demo_dir}")

    # 定義要測試的模擬檔案
    test_files = [
        "2024_Q2_財務報表.pdf",
        "台電五月繳費單_invoice.pdf",
        "IMG_20240602_台北車站.jpg",
        "工作紀錄_meeting_notes.docx",
        "昨晚跟朋友聚餐的影片.mp4",
        "不知名的雜物檔案.tmp",
        "六月工作計畫表.txt",
        "公司旅遊合照_01.png"
    ]

    for file_name in test_files:
        file_path = os.path.join(demo_dir, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("這是一個模擬檔案內容，用於 AI 智慧分類展示。")
        print(f"   📄 已生成: {file_name}")

    print("\n✅ Demo 環境準備就緒！")
    print("👉 請執行以下指令觀察 AI 智慧分類效果：")
    print(f"   python main.py --dir ./{demo_dir} --dry-run")

if __name__ == "__main__":
    create_demo_files()
