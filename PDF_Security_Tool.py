import os
import PyPDF2

def is_valid_file_path(path):
    """Check if the path looks like a file path (has an extension)."""
    return os.path.splitext(path)[1] != ""

def get_destination_path():
    """Ask user for destination path and validate."""
    while True:
        dest_path = input("Enter the path to save the PDF: ").strip()

        # Check if it's a file path (not just a folder)
        if not is_valid_file_path(dest_path) or not dest_path.lower().endswith(".pdf"):
            print("⚠️ Error: Please provide a valid PDF file path (e.g., C:\\folder\\file.pdf)")
            continue

        if os.path.exists(dest_path):
            print(f"⚠️ File already exists: {dest_path}")
            choice = input("Choose:\n1. Re-enter destination path\n2. Overwrite the file\nEnter choice (1/2): ").strip()
            if choice == "1":
                continue
            elif choice == "2":
                return dest_path
            else:
                print("⚠️ Invalid choice. Try again.")
                continue
        return dest_path


def lock_pdf(input_pdf, password):
    """Lock a PDF with the given password."""
    with open(input_pdf, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        writer = PyPDF2.PdfWriter()
        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password)

        dest_path = get_destination_path()
        with open(dest_path, "wb") as locked_file:
            writer.write(locked_file)

        print(f"✅ PDF locked successfully and saved at: {dest_path}")


def unlock_pdf(input_pdf):
    """Unlock a PDF by asking for password until correct."""
    while True:
        password = input("Enter the password: ").strip()
        with open(input_pdf, "rb") as file:
            reader = PyPDF2.PdfReader(file)

            if reader.is_encrypted:
                if reader.decrypt(password):
                    writer = PyPDF2.PdfWriter()
                    for page in reader.pages:
                        writer.add_page(page)

                    dest_path = get_destination_path()
                    with open(dest_path, "wb") as unlocked_file:
                        writer.write(unlocked_file)

                    print(f"✅ PDF unlocked successfully and saved at: {dest_path}")
                    return
                else:
                    print("❌ Wrong password! Please try again.")
            else:
                print("⚠️ This PDF is already unlocked.")
                return


def main():
    print("This is a PDF Locker/Unlocker Program\n")
    while True:
        choice = input("Do you want to Lock or Unlock a PDF? (lock/unlock/exit): ").strip().lower()

        if choice == "exit":
            print("👋 Exiting program. Goodbye!")
            exit()

        if choice not in ["lock", "unlock"]:
            print("⚠️ Invalid choice. Please enter 'lock' or 'unlock'.")
            continue

        pdf_path = input("Enter the path of the PDF: ").strip()

        # ✅ Ensure it's a valid PDF file
        if not os.path.isfile(pdf_path) or not pdf_path.lower().endswith(".pdf"):
            print("❌ Error: Please provide a valid PDF file path.")
            continue
        else:
            print("✅ File found, proceeding...")

        # ✅ Open once to check encryption status
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            already_locked = reader.is_encrypted

        if choice == "lock":
            if already_locked:
                print("❌ Error: This PDF is already locked.")
                continue

            # 🔑 Keep asking until passwords match
            while True:
                pwd1 = input("Enter a password to lock this PDF: ").strip()
                pwd2 = input("Re-enter the password to confirm: ").strip()

                if pwd1 != pwd2:
                    print("❌ Passwords do not match. Try again.\n")
                elif pwd1 == "":
                    print("⚠️ Password cannot be empty. Try again.\n")
                else:
                    print("🔑 Password confirmed successfully!")
                    lock_pdf(pdf_path, pwd1)
                    break

        elif choice == "unlock":
            if not already_locked:
                print("⚠️ This PDF is already unlocked.")
                continue
            unlock_pdf(pdf_path)

        while True:
            choice = input("\nDo you want to process another PDF? (y/n): ").strip().lower()
            if choice in ['y', 'yes']:
                print("Continuing...\n")
                break   # restart loop
            elif choice in ['n', 'no']:
                print("👋 Exiting program. Goodbye!")
                exit()
            else:
                print("❌ Invalid choice. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()