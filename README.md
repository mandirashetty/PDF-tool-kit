
# 📄 PDF Merger & Splitter Tool

A versatile web application built with Streamlit and PyPDF2, offering a suite of functionalities to manage your PDF documents, including merging, splitting, rotating, encrypting, and reading PDF information and text.

## ✨ Features

This tool provides the following key functionalities:

* **🔗 Merge PDFs:** Combine multiple PDF files into a single document.
* **✂️ Split PDF:** Divide a single PDF into individual pages, allowing you to download each page separately.
* **🔄 Rotate PDF:** Rotate all pages of a PDF document by 90, 180, or 270 degrees.
* **🔐 Encrypt PDF:** Password-protect your PDF files for enhanced security.
* **📖 PDF Reader (Info + Text + Metadata):** Upload a PDF to:
    * View its total page count.
    * Extract and display its metadata (Author, Title, Creation Date).
    * Extract and display text content from all pages or just the first page.

## 🚀 Technologies Used

* **Streamlit:** For building the interactive web-based user interface.
* **PyPDF2:** A Python library used for all PDF manipulation tasks (reading, writing, merging, splitting, rotating, encrypting, and extracting text/metadata).
* **Python:** The core programming language for the application logic.

## ⚙️ Setup and Installation

Follow these steps to set up and run the PDF Merger & Splitter Tool locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```
    *(Replace `your-username` and `your-repo-name` with your actual GitHub details)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    * On Windows:
        ```bash
        .\venv\Scripts\activate
        ```

4.  **Install the required libraries:**
    ```bash
    pip install streamlit PyPDF2
    ```

5.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    (Assuming your main script is named `app.py`)

    This command will open the application in your web browser, typically at `http://localhost:8501`.

## 💡 How to Use

1.  **Select an Option:** Use the dropdown menu at the top to choose the desired PDF operation (Merge PDFs, Split PDF, Rotate PDF, Encrypt PDF, or PDF Reader).
2.  **Upload File(s):** Depending on the selected option, use the "Upload file" or "Upload files" button to select your PDF document(s).
3.  **Perform Action:** Click the corresponding button (e.g., "Merge", "Split", "Rotate", "Encrypt PDF", "Read PDF") to initiate the operation.
4.  **Download/View Output:**
    * For merge, rotate, and encrypt operations, a download button will appear to save the processed PDF.
    * For splitting, individual download buttons will appear for each split page.
    * For PDF Reader, the extracted information, metadata, and text will be displayed directly on the page.

## 🤝 Contributing

Feel free to fork the repository, make improvements, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
