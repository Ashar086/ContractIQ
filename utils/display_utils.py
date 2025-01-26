import streamlit as st

# Function to parse and display the analysis result
def display_analysis_result(analysis_result):
    try:
        # Display Risk Analysis
        st.subheader("Risk Analysis")
        st.write("**High Risk Clauses:**")
        for clause in analysis_result["risk_analysis"]["high_risk_clauses"]:
            if isinstance(clause, dict):
                st.write(f"- {clause['clause_name']}: {clause['description']}")
            else:
                st.write(f"- {clause}")
        
        st.write("**Medium Risk Clauses:**")
        for clause in analysis_result["risk_analysis"]["medium_risk_clauses"]:
            if isinstance(clause, dict):
                st.write(f"- {clause['clause_name']}: {clause['description']}")
            else:
                st.write(f"- {clause}")
        
        st.write("**Low Risk Clauses:**")
        for clause in analysis_result["risk_analysis"]["low_risk_clauses"]:
            if isinstance(clause, dict):
                st.write(f"- {clause['clause_name']}: {clause['description']}")
            else:
                st.write(f"- {clause}")
        
        # Display Compliance
        st.subheader("Compliance")
        st.write(f"**GDPR:** {analysis_result['compliance']['gdpr']}")
        st.write(f"**Data Protection:** {analysis_result['compliance']['data_protection']}")
        st.write(f"**Intellectual Property:** {analysis_result['compliance']['intellectual_property']}")
        
        # Display Key Clauses
        st.subheader("Key Clauses")
        for clause in analysis_result["key_clauses"]:
            st.write(f"**{clause['clause_name']}:** {clause['description']}")
    
    except KeyError as e:
        st.error(f"Missing expected key in analysis result: {e}")
