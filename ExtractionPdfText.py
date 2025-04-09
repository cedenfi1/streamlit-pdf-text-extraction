import streamlit as st
import PyPDF2

st.title("PDF Text Extraction App")
st.write("### Step 1: Upload your PDF files")
st.write("Upload as many PDFs as needed.")

# Allow multiple file uploads
uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    st.write(f"You've uploaded {len(uploaded_files)} file(s).")
    
    st.write("### Step 2: Extract Text from PDFs")
    if st.button("Extract and Combine Text"):
        combined_text = ""
        # Iterate over all uploaded PDF files
        for uploaded_file in uploaded_files:
            try:
                # Initialize PDF reader with the uploaded file stream
                pdf_reader = PyPDF2.PdfReader(uploaded_file)
                # Process each page in the PDF
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text = page.extract_text() or ""
                    combined_text += text + "\n"
            except Exception as e:
                st.error(f"Error processing {uploaded_file.name}: {e}")

        if combined_text.strip():
            st.success("Text extraction completed successfully!")
            # Provide a download button for the combined text file
            st.download_button(
                label="Download Combined Text",
                data=combined_text,
                file_name="combined_text.txt",
                mime="text/plain"
            )
        else:
            st.error("No text was extracted. Please check if the PDFs contain extractable text.")
