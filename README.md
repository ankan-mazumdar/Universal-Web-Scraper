# Universal-Web-Scraper


![image](https://github.com/user-attachments/assets/33f2367d-9209-4704-a78a-5bde0db8713e)

## 1. Scraping Setup

URL Input: Enter the URL of the website you wish to scrape.

Field Definition: Define the fields you want to extract from the website (e.g., title, number of points, creator, date of posting, number of comments).

Initiate Scraping: Click on "Scrape" to begin the scraping process.

Data Presentation: The scraper retrieves data and presents it in a table format.

Export Options: You can export the data in various formats such as JSON, Excel, or Markdown.

Cost Estimation: The application shows the number of input and output tokens and calculates the cost of the scraping operation.

## 2. Advanced Scraping Example
   
Alternative Website: Test the scraper on another website, such as a car listing site.

Field Definition: Define new fields for scraping (e.g., image, vehicle name, vehicle info, condition, sale info, bids).

Scrape Data: Initiate scraping, and the data is retrieved, including URLs linking to specific car listings.

Cost Analysis: Review the token usage and cost for this more extensive data set.

## 3. Code Implementation
   
Boilerplate Imports: Import necessary libraries like Pandas, BeautifulSoup, fentic, html2text, and Selenium.

 ### a. Selenium Setup:
  Create Options: Add arguments like disabling GPU, setting the user agent, and ensuring Chrome instances are separate.

  Fetch HTML: Use Selenium to mimic human behavior (e.g., scrolling) and fetch the HTML of the target page.

  ### b. Markdown Creation:
	HTML Cleaning: Remove unnecessary sections like footers and headers.
	
	Conversion to Markdown: Use html2text to convert HTML into a readable Markdown format.
	
  ### c. Dynamic Schema Creation:
	
	Schema Definition: Dynamically create a pydantic model based on user-provided fields.
	
	Container Setup: Define a container to hold multiple rows of the scraped data.
	
  ### d. Token and Price Calculation:
	Token Counting: Trim tokens if necessary and calculate the cost based on the number of tokens used.
	
  ### e. Save and Export Data:
	JSON and Excel Export: Save the scraped data in JSON format and export it as an Excel file.
	
## 4. Application Interface (Streamlit):
Sidebar Setup: Configure sidebar options like model selection and field tags.
	
Main Interface: Present the scraped data and offer export options.

## 5. Handling User Feedback
   
Consistency in Naming: Implement structured output to ensure consistent naming of fields across different scraping operations.

Library Utilization: Discuss the use of libraries like firr and alternatives for simplifying the scraping process while addressing CAPTCHA and other complexities.

Exploration of Alternatives: Consider benefits and drawbacks of using libraries versus manual scraping.
