import pandas as pd
from smart_logger import write_log, log_error

def clean_excel():
    try:
        df = pd.read_excel("../Sample_dataset.xlsx")
        df.fillna("unknown", inplace=True)

        cleaned_file = "Cleaned_Report.xlsx"
        df.to_excel(cleaned_file, index=False)

        write_log("Cleaned Excel saved successfully")
        print("✅ Excel file cleaned & saved!")
        
    except Exception as e:
        log_error(f"Excel cleaning failed: {str(e)}")
        print("❌ Cleaning failed!")

if __name__ == "__main__":
    clean_excel()
