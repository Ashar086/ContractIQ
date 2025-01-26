# ContractIQ
**Hack The Feature Hackathon**

ContractIQ is an AI-powered platform designed to revolutionize the way businesses review contracts. Built with cutting-edge natural language processing (NLP) technology, ContractIQ automates the tedious and error-prone process of contract analysis, enabling users to focus on strategic decision-making.

---

## Features
- **Clause Extraction**: Automatically identifies and extracts critical clauses from contracts.
- **Risk Assessment**: Evaluates clauses for high, medium, and low risks.
- **Anomaly Detection**: Flags unusual or non-standard clauses.
- **Compliance Checking**: Ensures contracts comply with relevant regulations (e.g., GDPR).
- **User-Friendly Interface**: Designed for both legal professionals and non-experts.

---

## How It Works
1. **Upload Contracts**: Users upload contracts in PDF, DOC, or TXT format.
2. **AI Analysis**: ContractIQ’s AI analyzes the contract, identifying key clauses, risks, and compliance issues.
3. **Generate Report**: Users receive a detailed report with actionable insights.

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Streamlit
- OpenAI API key (or equivalent AI/ML API key)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Ashar086/ContractIQ.git
   cd contractiq

   Set up your API key:

Create a .env file in the root directory:

plaintext
Copy
AI_ML_API_KEY="your-api-key-here"
Alternatively, you can enter your API key directly in the app when prompted.

Running the App
Start the Streamlit app:

bash
Copy
streamlit run app.py
Open your browser and navigate to the provided local URL (usually http://localhost:8501).

File Structure
Copy
contractiq/
├── app.py                  # Main Streamlit app
├── utils/                  # Utility functions
│   ├── __init__.py         # Initialize the utils package
│   ├── api_utils.py        # API-related functions
│   ├── file_utils.py       # File handling functions
│   └── display_utils.py    # Display and UI-related functions
├── requirements.txt        # Dependencies
└── .env                    # Environment variables (optional)
Usage
Enter API Key: When you first open the app, you will be prompted to enter your AI/ML API key.

Upload Contract: Upload a contract file (PDF, DOC, or TXT) for analysis.

View Results: The app will analyze the contract and display the results, including risk levels, compliance status, and key clauses.

Contributing
We welcome contributions! If you'd like to contribute to ContractIQ, please follow these steps:

Fork the repository.

Create a new branch for your feature or bugfix:

bash
Copy
git checkout -b feature/your-feature-name
Commit your changes:

bash
Copy
git commit -m "Add your commit message here"
Push your changes to the branch:

bash
Copy
git push origin feature/your-feature-name
Open a pull request and describe your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Built with ❤️ by [Your Name/Team Name].

Special thanks to Hack The Feature Hackathon for the opportunity.

Contact
For questions or feedback, please reach out:

Email: your-email@example.com

GitHub: your-username
