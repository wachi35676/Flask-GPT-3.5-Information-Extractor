To write a comprehensive README.md for your Python application, I'll first need to examine the contents of `app.py` to understand its functionality, dependencies, and how it's meant to be used. I'll start by reviewing the code. Give me a moment to open and read through your file.

Based on the code from `app.py`, here is a draft of the `README.md` for your application:

---

# Flask GPT-3.5 Information Extractor

This Flask application leverages OpenAI's GPT-3.5 model to process and extract information on specific topics from scraped web content. It integrates Google's Custom Search API for web scraping and OpenAI's API for processing the scraped content. The application provides a simple API endpoint that allows users to specify a topic; it then searches the web for content related to that topic, scrapes the content, and uses GPT-3.5 to extract and process relevant information.

## Features

- **Web Scraping:** Uses Google's Custom Search API to find and scrape content related to a specified topic.
- **Information Processing:** Leverages OpenAI's GPT-3.5 model to analyze and extract information from scraped content.
- **Flask API:** Provides a REST API endpoint for requesting processed information on specific topics.

## Installation

To set up and run this application locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/wachi35676/Researcher.git
   ```

2. **Install dependencies:**

   Ensure you have Python 3 installed. Then, install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables:**

   Create a `.env` file in the root directory of the project and add your OpenAI API key, Google Custom Search API key, and Custom Search Engine ID:

   ```plaintext
   OPENAI_API_KEY=<your_openai_api_key>
   GOOGLE_CUSTOM_SEARCH_API_KEY=<your_google_custom_search_api_key>
   GOOGLE_CUSTOM_SEARCH_ENGINE_ID=<your_custom_search_engine_id>
   ```

4. **Run the application:**

   ```bash
   python app.py
   ```

## Usage

Once the application is running, you can request processed information on a specific topic by accessing the following URL in your web browser or using a tool like curl:

```
http://localhost:5000/process/<topic>
```

Replace `<topic>` with your desired topic.
