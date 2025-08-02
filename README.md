# financeAI

**financeAI** is a tool that leverages AI to automate financial tracking, budgeting, and advice. It integrates with banking APIs to fetch transaction data, categorizes transactions, and provides insights into your financial health. The tool also supports exporting data to Google Sheets for easy visualization.

---

## Features ✨

- **Automated Transaction Categorization**: Uses AI to sort transactions into categories (e.g., gas, groceries, drinks).
- **Multi-Account Support**: Fetches transaction history from checking and credit card accounts.
- **Google Sheets Integration**: Exports categorized data to Google Sheets for easy tracking.
- **Budgeting & Financial Advice**: Analyzes your financial data to suggest budgets and provide actionable advice.
- **Secure API Integration**: Safely accesses banking and loan information without exposing sensitive credentials.

---

## Setup 🛠️

### Prerequisites
- [Homebrew](https://brew.sh/) (for macOS)
- [pyenv](https://github.com/pyenv/pyenv) (for Python version management)
- [PDM](https://pdm.fming.dev/) (for dependency management)

### Installation
1. Install system dependencies:
   ```bash
   brew install pyenv pipx
   ```

2. Install Python and set up the project environment:
   ```bash
   pyenv install 3.12.6
   pyenv local 3.12.6
   pipx install pdm
   ```

3. Install project dependencies:
   ```bash
   pdm install
   ```

4. Set up pre-commit hooks (optional but recommended):
   ```bash
   pdm run pre-commit install
   ```

### Google Sheets Configuration
1. Create a new Google Cloud project and enable the following APIs:
   - `sheets.googleapis.com`
   - `drive.googleapis.com`

2. Create a service account and download the JSON key file.

3. Share your Google Sheet with the service account email.

4. For restricted files (e.g., API keys), create symbolic links:
   ```bash
   ln -s ~/path/to/file restricted/file
   ```

---

## Usage 🚀

1. **Fetch Transaction Data**:
   - **Checking Account**:
     1. Log in to your bank account.
     2. Navigate to the checking account's "Transaction History" section.
     3. Click the download button and choose **CSV format**.
     4. Save the file as `debit.csv` in the `restricted/` directory.
   - **Credit Card Account**:
     1. Log in to your credit card account.
     2. Go to the "Search Transactions" tab.
     3. At the bottom of the page, select **CSV** from the "Transaction Format" dropdown.
     4. Save the file as `credit.csv` in the `restricted/` directory.

2. **Run the Tool**:
   ```bash
   pdm run python main.py
   ```
   - The tool will:
     - Fetch and categorize transactions using AI.
     - Export the data to your configured Google Sheet.
     - Provide budgeting insights and financial advice.

3. **Backup**:
   - After running the tool, back up the transaction history CSV files using the provided script:
   ```bash
   cd restricted
   ./copy_history_to_icloud.sh
   ```

---

## Contributing 🤝

Contributions are welcome! If you'd like to improve financeAI, please:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



- changing how python and it's dependencies are managed
   - going to use mise
   - maybe going to use uv or poetry or something else
- considering learning and using uv for everything else
