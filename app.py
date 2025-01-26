import streamlit as st
from utils.api_utils import generate_chat_completion, analyze_contract
from utils.file_utils import extract_text_from_pdf, split_text_into_chunks
from utils.display_utils import display_analysis_result

# Streamlit UI
st.title("ContractIQ")

# Initialize session state for API key
if "api_key" not in st.session_state:
    st.session_state.api_key = None

# Prompt the user to enter their API key
if not st.session_state.api_key:
    st.header("Get Started")
    st.markdown("**Please enter your AI/ML API key to continue.**")
    api_key = st.text_input("Enter your API key:", type="password")
    
    if api_key:
        st.session_state.api_key = api_key
        st.success("API key saved successfully!")
    else:
        st.warning("Please enter a valid API key to proceed.")
        st.stop()

# Display key metrics (can be dynamically updated based on backend data)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Contracts Reviewed", "1,234")  # Replace with dynamic data
col2.metric("High Risk Contracts", "56")    # Replace with dynamic data
col3.metric("Approved Contracts", "987")    # Replace with dynamic data
col4.metric("Active Users", "42")           # Replace with dynamic data

# Upload Contract Section
st.header("Upload New Contract")
st.markdown("**Please upload a contract file (PDF, DOC, TXT) that is less than 100 KB.**")
uploaded_file = st.file_uploader("Drag and drop your contract file or click to browse", type=["pdf", "doc", "txt"])

if uploaded_file is not None:
    # Check file size
    if uploaded_file.size > 100 * 1024:  # 100 KB in bytes
        st.error("File size exceeds 100 KB. Please upload a smaller file.")
    else:
        try:
            # Extract text from the uploaded file
            if uploaded_file.type == "application/pdf":
                contract_text = extract_text_from_pdf(uploaded_file)
            else:
                contract_text = uploaded_file.read().decode("utf-8")
            
            # Analyze the contract
            if st.button("Start AI Review"):
                with st.spinner("Analyzing contract..."):
                    # Use the API key from session state
                    api_key = st.session_state.api_key
                    
                    # Analyze the contract using the AI/ML API
                    analysis_result = analyze_contract(api_key, contract_text)
                    
                    if analysis_result:
                        st.markdown("### Analysis Result")
                        display_analysis_result(analysis_result)  # Display the parsed analysis result
                    else:
                        st.error("Failed to analyze the contract.")
        except Exception as e:
            st.error(f"Error processing the file: {e}")

# Recent Contract Activity (can be dynamically updated based on backend data)
st.header("Recent Contract Activity")
st.write("Latest updates on contract reviews and approvals")

# Example dynamic data (replace with actual data from backend)
recent_activity = [
    {"Contract Name": "Service Agreement - TechCorp", "Status": "Approved", "Risk Level": "Low", "Last Updated": "2023-09-15"},
    {"Contract Name": "NDA - StartupX", "Status": "In Review", "Risk Level": "Medium", "Last Updated": "2023-09-14"},
    {"Contract Name": "Licensing Agreement - BigCo", "Status": "Needs Attention", "Risk Level": "High", "Last Updated": "2023-09-13"},
]

st.table(recent_activity)
