import streamlit as st
from PyPDF2 import PdfReader, PdfWriter

st.set_page_config(page_title="PDF Merger & Splitter Tool", layout="centered")

st.title("📄 PDF Merger & Splitter Tool")
st.markdown("Built with ❤️ using PyPDF2 + Streamlit")

# Function selection
option = st.selectbox("Select an option", [
    "Merge PDFs",
    "Split PDF", 
    "Rotate PDF",
    "Encrypt PDF",
    "PDF Reader (Info + Text + Metadata)"
])

# ----- Merge PDFs -----
if option == "Merge PDFs":
    st.header("🔗 Merge PDFs")
    merge_files = st.file_uploader("Upload PDFs to merge", type="pdf", accept_multiple_files=True)
    if st.button("Merge"):
        if merge_files and len(merge_files) >= 2:
            try:
                writer = PdfWriter()
                for uploaded_file in merge_files:
                    reader = PdfReader(uploaded_file)
                    for page in reader.pages:
                        writer.add_page(page)
                with open("merged_output.pdf", "wb") as f:
                    writer.write(f)
                st.success("✅ Merged successfully!")
                with open("merged_output.pdf", "rb") as f:
                    st.download_button("Download Merged PDF", f, file_name="merged.pdf")
            except Exception as e:
                st.error(f"❌ Error while merging: {e}")
        else:
            st.warning("Please upload at least two PDF files.")

# ----- Split PDF -----
elif option == "Split PDF":
    st.header("✂️ Split PDF")
    split_file = st.file_uploader("Upload a PDF to split", type="pdf")
    if st.button("Split"):
        if split_file:
            try:
                reader = PdfReader(split_file)
                for i, page in enumerate(reader.pages):
                    writer = PdfWriter()
                    writer.add_page(page)
                    output_name = f"split_page_{i+1}.pdf"
                    with open(output_name, "wb") as f:
                        writer.write(f)
                    with open(output_name, "rb") as f:
                        st.download_button(f"Download Page {i+1}", f, file_name=output_name)
                st.success("✅ Split completed!")
            except Exception as e:
                st.error(f"❌ Error while splitting: {e}")
        else:
            st.warning("Upload a file to split.")

# ----- Rotate PDF -----
elif option == "Rotate PDF":
    st.header("🔄 Rotate PDF")
    rotate_file = st.file_uploader("Upload a PDF to rotate", type="pdf")
    rotate_angle = st.selectbox("Choose Rotation Angle", [90, 180, 270])
    if st.button("Rotate"):
        if rotate_file:
            try:
                reader = PdfReader(rotate_file)
                writer = PdfWriter()
                for page in reader.pages:
                    page.rotate(rotate_angle)
                    writer.add_page(page)
                with open("rotated_output.pdf", "wb") as f:
                    writer.write(f)
                with open("rotated_output.pdf", "rb") as f:
                    st.download_button("Download Rotated PDF", f, file_name="rotated.pdf")
                st.success("✅ Rotated successfully!")
            except Exception as e:
                st.error(f"❌ Error while rotating: {e}")
        else:
            st.warning("Upload a PDF file.")

# ----- Encrypt PDF -----
elif option == "Encrypt PDF":
    st.header("🔐 Password Protect PDF")
    protect_file = st.file_uploader("Upload a PDF to protect", type="pdf")
    password = st.text_input("Enter password to encrypt", type="password")
    if st.button("Encrypt PDF"):
        if protect_file and password:
            try:
                reader = PdfReader(protect_file)
                writer = PdfWriter()
                for page in reader.pages:
                    writer.add_page(page)
                writer.encrypt(password)
                with open("protected.pdf", "wb") as f:
                    writer.write(f)
                with open("protected.pdf", "rb") as f:
                    st.download_button("Download Encrypted PDF", f, file_name="encrypted.pdf")
                st.success("✅ Encrypted successfully!")
            except Exception as e:
                st.error(f"❌ Error while encrypting: {e}")
        else:
            st.warning("Please upload a file and set a password.")

# ----- Combined Info + Text + Metadata -----
elif option == "PDF Reader (Info + Text + Metadata)":
    st.header("📖 PDF Reader (Info + Text + Metadata)")
    reader_file = st.file_uploader("Upload a PDF to view info & extract text", type="pdf")

    show_metadata = st.checkbox("Show Metadata")
    first_page_only = st.checkbox("Extract text from only the first page")

    if st.button("Read PDF"):
        if reader_file:
            try:
                reader = PdfReader(reader_file)
                total_pages = len(reader.pages)
                st.write("**Total Pages:**", total_pages)

                # Metadata
                if show_metadata:
                    meta = reader.metadata
                    st.subheader("📌 Metadata")
                    st.write("**Author:**", meta.author or "N/A")
                    st.write("**Title:**", meta.title or "N/A")
                    st.write("**Creation Date:**", meta.creation_date or "N/A")

                # Text Extraction
                st.subheader("📄 Extracted Text")
                if first_page_only:
                    text = reader.pages[0].extract_text()
                    st.subheader("Page 1")
                    st.text(text if text else "⚠️ No text found on this page.")
                else:
                    for i, page in enumerate(reader.pages):
                        text = page.extract_text()
                        st.subheader(f"Page {i+1}")
                        st.text(text if text else "⚠️ No text found on this page.")

                st.success("✅ Reading completed!")

            except Exception as e:
                st.error(f"❌ Error while reading PDF: {e}")
        else:
            st.warning("Upload a PDF file.")