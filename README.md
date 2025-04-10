# 📄 DOCUMENT-FORMAT-CONVERTER

A simple web-based tool to convert between various document and Document formats using Calibre and Streamlit.

---

## 🛠️ Requirements

- Python 3.x
- `streamlit` Python package
- Calibre (for eBook conversion)

---

## 🔧 Installation Instructions

1. **Install Python 3.x**  
   Download and install from [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Install Calibre**:
   - **Ubuntu**:
     ```bash
     sudo apt-get install -y calibre
     ```
   - **macOS**:
     ```bash
     brew install calibre
     ```
   - **Windows (PowerShell as Admin)**:
     ```bash
     choco install calibre
     ```

3. **Install Python packages**:
   ```bash
   pip install streamlit subprocess
   ```
   **OR using requirements.txt:**
   ```bash
   pip install -r requirement.txt
   ```
### 🖥️ streamlit Web Interface

1. **Run the Script**:
   ```bash
   streamlit run app.py
   ```

2. **Open the Web App**: After running the command, Streamlit will provide a local URL (e.g., http://localhost:8501) — click it to open the app.

## 📚 Supported Formats

   **📥 Input File Formats :**
   `.azw`, `.azw3`, `.cbz`, `.cbr`, `.cbc`, `.chm`, `.docx`, `.epub`, `.fb2`, `.html`, `.htmlz`,`.lit`, `.lrf`, `.mobi`, `.odt`, `pdf`, `.prc`, `.pdb`, `.pml`, `.rb`, `.rtf`, `.snb`, `.tcr`,
   `.txt`, `.txtz`

   **📤 Output File Formats :**
   `.azw3`, `.cbc`, `.docx`, `.epub`, `.fb2`, `.htmlz`, `.lit`, `.lrf`, `.mobi`, `.odt`, `.pdf`,`.pdb`, `.pml`, `.rb`, `.rtf`, `.snb`, `.tcr`, `.txt`, `.txtz`, `.zip`
