# Universal-Web-Scraper using Python, Selenium and Streamlit UI


![image](https://github.com/user-attachments/assets/33f2367d-9209-4704-a78a-5bde0db8713e)


This guide will walk you through setting up the environment, installing the required packages, configuring your API key, and running a web scraping application. By the end of this tutorial, you'll be able to scrape data from websites using Python.

## 1. Setting Up the Environment

Before we dive into web scraping, let's set up a Python environment to work in.

### Step 1: Create a Virtual Environment

To keep your project dependencies organized, it's best to create a virtual environment:

```bash
python3 -m venv scraping-env
```

### Step 2: Activate the Virtual Environment

Next, activate the environment:

- **Windows:**

  ```bash
  .\scraping-env\Scripts\activate
  ```

- **macOS/Linux:**

  ```bash
  source scraping-env/bin/activate
  ```

## 2. Installing Required Packages

With the virtual environment activated, let's install the necessary packages.

### Step 3: Install the Requirements

Run the following command to install all required libraries:

```bash
pip install -r requirements.txt
```

This will install everything you need for the web scraping application.

## 3. Setting Up Your API Key

If you're using an API that requires authentication, you'll need to set up your API key.

### Step 4: Create an `.env` File

Create a `.env` file in the root directory of your project and add your API key like this:

```plaintext
API_KEY=your_api_key_here
```

### Step 5: Load the API Key in Your Code

In your Python script, ensure the API key is loaded using the `dotenv` library:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')
```

## 4. Running the Web Scraping Application

Now that your environment is set up and your API key is configured, you can run the web scraping application.

### Step 6: Run the Application

Execute your Python script to start scraping:

```bash
python scrape.py
```

This will initiate the web scraping process, and you'll see the output based on the websites you've configured to scrape.

## 5. Trying Out Scraping Websites

### Step 7: Experiment with Different Websites

You can customize the scraping targets by modifying the URLs and scraping logic in your `scrape.py` file. Try scraping different websites by changing the `url` variable and the parsing logic to suit your needs.

### Step 8: Analyze and Store the Data

Once the data is scraped, you can analyze it or store it in a format of your choice (e.g., CSV, JSON, or a database). Modify the script to save the scraped data as needed.

