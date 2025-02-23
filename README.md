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
```bash
git clone https://github.com/yourusername/ETF-Recommender.git
cd ETF-Recommender
```

2. **Setup virtual environment**
```python -m venv etf-env
source etf-env/bin/activate  # Linux/Mac
# etf-env\Scripts\activate  # Windows
```

3. **Install requirements**
```pip install -r requirements.txt
```

4. **Download initial data**
```python etf_data.py
```

## Usage 💻

1. **Start the app**
```python app.py
```

2. **Open your browser to**
```http://localhost:7860
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
etf-recommendation-engine/
├── .env                    # Environment variables
├── .gitignore
├── README.md
├── requirements.txt
├── setup.py
│
├── config/
│   ├── logging.conf        # Logging configuration
│   └── settings.py         # Global settings (DB connections, API keys)
│
├── data/
│   ├── raw/                # Raw scraped data (JSON/HTML/CSV)
│   ├── processed/          # Cleaned/transformed data
│   └── external/           # Static reference data (e.g., sector classifications)
│
├── docs/                   # Documentation
│
├── etl/
│   ├── scrapers/           # Individual website scrapers
│   │   ├── ishares.py
│   │   ├── vanguard.py
│   │   └── yfinance_api.py
│   │
│   ├── transformers/       # Data cleaning scripts
│   │   ├── clean_etf_metadata.py
│   │   └── normalize_holdings.py
│   │
│   └── loaders/            # Database loading scripts
│       ├── postgres_loader.py
│       └── mongo_loader.py
│
├── src/                    # Core application logic
│   ├── models/             # Database models
│   │   ├── etf_metadata.py
│   │   └── holdings.py
│   │
│   ├── services/           # Business logic
│   │   ├── etf_search.py
│   │   └── recommender.py
│   │
│   └── utils/              # Helper functions
│       ├── logger.py
│       ├── http_client.py  # Custom requests wrapper
│       └── data_validation.py
│
├── tests/                  # Unit and integration tests
│   ├── unit/
│   └── integration/
│
├── notebooks/              # Jupyter notebooks for exploration
│   ├── ETF Data Analysis.ipynb
│   └── Scraping Tests.ipynb
│
├── frontend/               # Web app (React/Vue)
│   ├── public/
│   ├── src/
│   │   ├── components/     # ETF cards, search bar
│   │   └── views/          # Main pages
│
└── backend/                # FastAPI backend
    ├── main.py
    ├── routes/
    │   ├── etf_routes.py
    │   └── chat_routes.py
    └── ai/                 # NLP components
        ├── embeddings.py
        └── semantic_search.py
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
