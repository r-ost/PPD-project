# PPD-project

### Setup

1. Install uv:
   ```bash
   # Windows (PowerShell)
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Sync dependencies:**
   ```bash
   uv sync
   ```
   This will:
   - Create a virtual environment (`.venv`)
   - Install all dependencies from `pyproject.toml`
   - Use exact versions from `uv.lock`

3. **Use the virtual environment to run notebooks and scripts:**
   ```bash
   uv run jupyter lab
   ```

### Useful commands

- Add a new dependency:
  ```bash
  uv add <package-name>
  ```


### Data download

Download the Yelp dataset from [this link](https://business.yelp.com/external-assets/files/Yelp-JSON.zip) and place the ZIP file in the `data/raw/` directory. Then run `notebooks/01_eda.ipynb` to decompress the data.