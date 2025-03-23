# ETF Semantic Search Tool 🔍

Find exchange-traded funds (ETFs) that match your investment interests using plain English!

![Demo Preview](https://via.placeholder.com/800x400.png?text=Demo+GIF+Coming+Soon)

## Features ✨
- Search ETFs using natural language (e.g., "Leveraged Bear strategy on oil and gas sector" or "High dividend yield REITs ETFs")
- Get AI-powered ETF recommendations
- Simple web interface
- Automatic monthly data updates

## Installation 🛠️

1. **Clone the repository**
```
bash
git clone https://github.com/yourusername/ETF-Recommender.git
cd ETF-Recommender
```

2. **Setup virtual environment**
```
python -m venv etf-env
source etf-env/bin/activate  # Linux/Mac
# etf-env\Scripts\activate  # Windows
```

3. **Install requirements**
```
pip install -r requirements.txt
```

4. **Download initial data**
```
python etf_data.py
```

## Usage 💻

1. **Start the app**
```
python app.py
```

2. **Open your browser to**
```
http://localhost:7860
```

3. **Try these example searches:**

"Technology innovation ETFs"

"Leveraged bear ETF in oil and gas sector"

"Greater than 4% dividend yielding REITs"


## How It Works 🔧

1. Data Collection: Gets ETF information from financial websites

2. AI Processing: Uses language models to understand your search

3. Matching: Finds ETFs with similar descriptions to your query

4. Results: Shows top matches with key details

## Project Structure 📂

```
etf-recommender/
├── data/
│   ├── llm_generated/
│   │   ├── etf_raw/          # Raw LLM outputs (JSON)
│   │   └── etf_processed/    # Cleaned/validated data
│   └── external/             # Reference data (e.g., sector classifications)
│
├── llm/
│   ├── prompts/              # System prompts for different ETF types
│   │   ├── equity_prompt.txt
│   │   └── fixed_income_prompt.txt
│   ├── schemas/              # JSON schemas for validation
│   └── etl.py                # LLM data generation pipeline
│
├── database/
│   ├── models/               # SQLAlchemy models
│   ├── vector_db/            # FAISS/Pinecone embeddings
│   └── etl.py                # DB loading scripts
│
├── app/
│   ├── frontend/             # Streamlit/Gradio UI
│   └── api/                  # FastAPI endpoints
│
├── config/
│   ├── settings.py           # API keys, DB connections
│   └── constants.py          # ETF categories, validation rules
│
└── scripts/
    ├── validation/           # Data quality checks
    └── deployment/           # Cloud deployment configs
```

## Contributing

We welcome improvements! Please:

1. Fork the repository

2. Create your feature branch (git checkout -b cool-new-feature)

3. Commit changes (git commit -m 'Add awesome feature')

4. Push to branch (git push origin cool-new-feature)

5. Open a Pull Request

## License 📄

This project is licensed under the MIT License

Note: This tool provides educational information only. Always consult a financial advisor before investing.
Created with ❤️ by Rahul Ghosh
