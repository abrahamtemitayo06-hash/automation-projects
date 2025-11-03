import os
import pandas as pd
import smtplib
from email.message import EmailMessage
from smart_logger import write_log, log_error

def clean_excel_file():
    try:
        # ✅ Path to the original Excel file (one folder up)
        source_file = "../Sample_dataset.xlsx"
        
        # ✅ Load the dataset
        df = pd.read_excel(source_file)
        
        # ✅ Fill empty cells
        df.fillna("unknown", inplace=True)

        # ✅ Save cleaned version inside Day4 folder
        cleaned_file = "Cleaned_Report.xlsx"
        df.to_excel(cleaned_file, index=False)

        write_log("Excel file cleaned successfully")

        return cleaned_file  # ✅ Return filename for email attachment

    except Exception as e:
        log_error(f"Excel cleaning failed: {str(e)}")
        return None


def send_email_with_attachment(file_path):
    try:
        EMAIL_ADDRESS = "temidoyin@example.com"  # replace
        EMAIL_PASSWORD = "yourpassword"          # replace
        
        msg = EmailMessage()
        msg["Subject"] = "Cleaned Excel Report"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS

        msg.set_content("The cleaned Excel report is attached.")

        # ✅ Attach the file
        with open(file_path, "rb") as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype="application",
                               subtype="octet-stream", filename=file_path)

        # ✅ Send email
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        write_log("Email with attachment sent successfully!")

    except Exception as e:
        log_error(f"Email sending failed: {str(e)}")


if __name__ == "__main__":
    cleaned_file = clean_excel_file()

    if cleaned_file:
        send_email_with_attachment(cleaned_file)
    else:
        print("Cleaning failed! Email not sent.")
