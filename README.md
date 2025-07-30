# ScholarGPT

**AI-powered scientific assistant for reading, summarizing, and querying research papers.**

---

## Features

- Upload and ingest PDF research papers  
- Generate high-quality embeddings using custom models (e.g., SciBERT)  
- Store and search documents efficiently with Chroma vector database  
- Conversational question-answering with OpenAI GPT models  
- Memory management via ConversationSummaryMemory for context awareness  
- Integrated tools like Calculator and Google Search for enhanced answers  
- Easy-to-use Streamlit web interface for uploading documents  
- Support for fine-tuning to customize model behavior  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ChristinaMakri/ScholarGPT.git
cd ScholarSynth
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a .env file in the root folder and add your OpenAI API key:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

5. (Optional) Set up Google Search API keys if you want to use the Google Search tool.


## Usage

1. Run the Streamlit app to upload PDFs:
```bash
streamlit run app.py
```
Upload your PDF research papers through the web UI.

2. Run the main conversational AI script:
```bash
python main.py
```
Ask questions about the uploaded papers interactively in the terminal.
