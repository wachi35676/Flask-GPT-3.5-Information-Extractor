from flask import Flask, jsonify
from dotenv import load_dotenv
from openai import OpenAI
import os
import requests
from bs4 import BeautifulSoup

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI()

app = Flask(__name__)

API_KEY = os.getenv('GOOGLE_CUSTOM_SEARCH_API_KEY')
SEARCH_ENGINE_ID = os.getenv('GOOGLE_CUSTOM_SEARCH_ENGINE_ID')


def gpt_3_5_process(raw_text, topic):
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "Your task is to read the following text and provide information on a specific topic."},
            {"role": "user", "content": raw_text},
            {"role": "user", "content": f"Extract information about {topic}."}
        ],
    )
    return response.choices[0].message.content


def search_and_scrape(topic):
    search_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={topic}"
    response = requests.get(search_url)
    results = response.json().get('items', [])
    scraped_data = []
    for result in results:
        try:
            url = result['link']
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            text = ' '.join([p.text for p in soup.find_all('p')])
            if not text.strip():
                continue
            scraped_data.append({'url': url, 'content': text, 'topic': topic})
        except Exception as e:
            print(e)
    return scraped_data


@app.route('/process/<topic>', methods=['GET'])
def scrape_and_process(topic):
    try:
        scraped_data = search_and_scrape(topic)
        processed_results = []
        for data in scraped_data:
            processed_text = gpt_3_5_process(data['content'], topic)
            if processed_text.lower() == 'irrelevant':
                continue
            processed_results.append({'url': data['url'], 'processed_content': processed_text, 'topic': topic})
        return jsonify(processed_results), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
