## Uli_Scraping

### To run this code

1. Clone this repository
2. Make sure pip is up to date:
   ```bash
   python -m pip install --upgrade pip
   ```
3. Install `uv` package manager:
   ```bash
   pip install uv
   ```
4. Create and activate a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Unix/MacOS
   # OR
   .venv\Scripts\activate     # On Windows
   ```
5. Install requirements:
   ```bash
   uv pip install -r requirements.txt
   ```
6. Run the scraper:
   ```bash
   python scripts/scrape.py
   ```