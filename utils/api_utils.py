import requests
import asyncio
import json

# Function to generate chat completion using AI/ML API
async def generate_chat_completion(api_key, system_prompt, user_prompt):
    base_url = "https://api.aimlapi.com/v1"
    
    try:
        # Define the payload for the API request
        payload = {
            "model": "gpt-3.5-turbo",  # Use GPT-3.5 Turbo (or your custom model)
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "max_tokens": 1000,  # Increase tokens for detailed analysis
            "temperature": 0.5  # Lower temperature for more focused responses
        }
        
        # Send the request to the API
        response = await asyncio.to_thread(
            requests.post,
            f"{base_url}/chat/completions",
            json=payload,
            headers={
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            }
        )
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as e:
        raise Exception(f'HTTP Error: {e.response.status_code} - {e.response.text}')
    except requests.exceptions.RequestException as e:
        raise Exception(f'API Request Error: {e}')

# Function to analyze the contract using the AI/ML API
def analyze_contract(api_key, contract_text):
    # Define comprehensive system prompt
    system_prompt = """
    You are an AI-powered contract review assistant. Your task is to analyze contracts for the following aspects:
    1. Clause extraction: Identify and extract key clauses.
    2. Risk assessment: Evaluate the risk level of each clause.
    3. Anomaly detection: Detect any unusual or non-standard clauses.
    4. Compliance checking: Ensure the contract complies with relevant regulations (e.g., GDPR).
    5. Provide a detailed analysis report in the following JSON format:
    {
        "risk_analysis": {
            "high_risk_clauses": [],
            "medium_risk_clauses": [],
            "low_risk_clauses": []
        },
        "compliance": {
            "gdpr": "Compliant/Non-compliant",
            "data_protection": "Compliant/Non-compliant",
            "intellectual_property": "Compliant/Non-compliant"
        },
        "key_clauses": [
            {
                "clause_name": "Termination Clause",
                "description": "30 days' notice"
            },
            {
                "clause_name": "Liability Limitation",
                "description": "Limited to contract value"
            },
            {
                "clause_name": "Confidentiality Agreement",
                "description": "Standard clause"
            }
        ]
    }
    """
    
    # Split the contract text into smaller chunks
    chunks = split_text_into_chunks(contract_text)
    analysis_results = []

    for chunk in chunks:
        user_prompt = f"""Analyze the following contract text and provide a detailed report in JSON format:
        {chunk}
        """
        
        # Generate analysis using the AI/ML API
        analysis_result = asyncio.run(generate_chat_completion(api_key, system_prompt, user_prompt))
        if analysis_result:
            analysis_results.append(analysis_result)
    
    # Combine results from all chunks into a single JSON object
    return merge_json_responses(analysis_results)

# Function to merge multiple JSON responses into a single JSON object
def merge_json_responses(json_responses):
    merged_result = {
        "risk_analysis": {
            "high_risk_clauses": [],
            "medium_risk_clauses": [],
            "low_risk_clauses": []
        },
        "compliance": {
            "gdpr": "Compliant",
            "data_protection": "Compliant",
            "intellectual_property": "Compliant"
        },
        "key_clauses": []
    }

    for response in json_responses:
        try:
            data = json.loads(response)
            
            # Merge risk analysis
            if "risk_analysis" in data:
                for risk_level in ["high_risk_clauses", "medium_risk_clauses", "low_risk_clauses"]:
                    if risk_level in data["risk_analysis"]:
                        merged_result["risk_analysis"][risk_level].extend(data["risk_analysis"][risk_level])
            
            # Merge compliance (take the strictest compliance)
            if "compliance" in data:
                for compliance_key in ["gdpr", "data_protection", "intellectual_property"]:
                    if compliance_key in data["compliance"]:
                        if data["compliance"][compliance_key] == "Non-compliant":
                            merged_result["compliance"][compliance_key] = "Non-compliant"
            
            # Merge key clauses
            if "key_clauses" in data:
                merged_result["key_clauses"].extend(data["key_clauses"])
        
        except json.JSONDecodeError:
            raise Exception(f"Failed to parse JSON response: {response}")
    
    return merged_result
