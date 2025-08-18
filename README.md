## PDF Security Tool

Command-line utility to lock (encrypt) and unlock (decrypt) PDF files using passwords. Built with `PyPDF2`.

### Features
- **Lock PDFs**: Encrypt a PDF with a password you choose (with confirmation)
- **Unlock PDFs**: Decrypt a password-protected PDF after verifying the correct password
- **Safe destination handling**: Prompts for a destination file path and warns before overwriting
- **Input validation**: Checks that provided paths are valid `.pdf` files

### Requirements
- Python 3.8+
- PyPDF2

Install the dependency:

```bash
pip install PyPDF2
```

### Usage
Run the tool from the project directory:

```bash
python PDF_Security_Tool.py
```

Follow the prompts:
- Choose `lock` or `unlock`
- Enter the source PDF path
  - Example (Windows): `C:\Users\you\Documents\file.pdf`
- For locking, enter and confirm the password
- Provide a destination path for the output PDF (must end with `.pdf`)

#### Examples
- Lock a PDF:
  1) Choose `lock`
  2) Enter: `H:\GitHub_Repositories\PDF_Security_Tool\Sample_Files\Unlock\Sample_Unlock.pdf`
  3) Enter and confirm a password
  4) Provide a destination path, e.g. `C:\Users\you\Desktop\locked.pdf`

- Unlock a PDF:
  1) Choose `unlock`
  2) Enter: `H:\GitHub_Repositories\PDF_Security_Tool\Sample_Files\Lock\Sample_lock.pdf`
  3) Enter the correct password
  4) Provide a destination path, e.g. `C:\Users\you\Desktop\unlocked.pdf`

### Project Structure
```
PDF_Security_Tool/
├─ PDF_Security_Tool.py
└─ Sample_Files/
   ├─ Lock/
   │  └─ Sample_lock.pdf
   └─ Unlock/
      └─ Sample_Unlock.pdf
```

### Notes
- If you see "File already exists" when choosing a destination, you can opt to overwrite or re-enter a new path
- For unlocking, if the password is incorrect, the tool will prompt you to try again

### Disclaimer
Use responsibly and only on documents you are authorized to access.


