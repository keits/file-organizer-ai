import os
import argparse
import logging
from core.organizer import FileOrganizer

# 設定日誌格式，讓輸出更具專業感
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def main():
    parser = argparse.ArgumentParser(description="AI 智慧檔案整理器 - 補助展示版")
    parser.add_argument("--dir", type=str, required=True, help="要整理的目標資料夾路徑")
    parser.add_argument("--dry-run", action="store_true", help="僅產出建議，不實際移動檔案")
    parser.add_argument("--model", type=str, default="mock", choices=["mock", "openai"], help="選擇 AI 模型引擎")
    
    args = parser.parse_parse_args() if hasattr(parser, 'parse_parse_args') else parser.parse_args()
    
    target_dir = args.dir
    if not os.path.exists(target_dir):
        logging.error(f"找不到指定的資料夾路徑：{target_dir}")
        print("💡 提示：請確認路徑是否正確，或使用絕對路徑。")
        return

    logging.info(f"啟動檔案掃描引擎，目標：{target_dir}")
    logging.info(f"目前使用 AI 引擎：{args.model.upper()}")
    
    try:
        organizer = FileOrganizer(target_dir)
        
        # 1. 取得檔案清單
        files = organizer.list_files()
        if not files:
            logging.warning("資料夾為空，或沒有需要整理的檔案。")
            return
            
        print(f"\n🔍 掃描完成，共發現 {len(files)} 個檔案。")
        
        # 2. 詢問 AI 分類計畫
        print("🤖 正在調用 AI 語意分析引擎，請稍候...")
        plan = organizer.generate_plan(files)
        
        # 3. 顯示計畫並執行
        organizer.display_plan(plan)
        
        if not args.dry_run:
            print("\n" + "="*40)
            confirm = input("⚠️ 是否授權系統執行實體檔案搬移？(y/N): ")
            if confirm.lower() == 'y':
                logging.info("開始執行檔案搬移作業...")
                organizer.execute_plan(plan)
                logging.info("✨ 檔案整理作業順利完成！")
            else:
                logging.info("已取消執行，檔案維持原狀。")
        else:
            print("\n📝 [安全模式] Dry-run 結束，未更動任何實體檔案。")
            
    except PermissionError:
        logging.error("權限不足：無法讀取或移動該資料夾內的檔案。")
    except Exception as e:
        logging.error(f"執行過程中發生未預期錯誤：{str(e)}")

if __name__ == "__main__":
    main()
