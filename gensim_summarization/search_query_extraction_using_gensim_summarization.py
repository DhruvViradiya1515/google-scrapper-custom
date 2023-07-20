import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize
from nltk.tokenize import sent_tokenize

# Function to fetch the web page content
def get_webpage_content(url):
    response = requests.get(url)
    return response.text

# Function to extract relevant text from the webpage
def extract_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Extract text from HTML tags based on your requirements
    # Adjust this code according to the structure of the web page you are scraping
    # Remove unnecessary tags or content (e.g., headings, navigation, footers)
    for unwanted_element in soup(['header', 'nav', 'footer', 'aside', 'script', 'style']):
        unwanted_element.extract()

    # Remove elements with specific class names
    unwanted_classes = ['widget', 'advertisement', 'sidebar']
    for unwanted_class in unwanted_classes:
        for element in soup.find_all(class_=unwanted_class):
            element.extract()

    text = soup.get_text()
    return text

# Function to summarize the text
def summarize_text(text, num_sentences):
    # Perform text summarization using Gensim's TextRank algorithm
    summary_sentences = summarize(text, ratio=1.0, split=True)

    # Filter out short and uninformative sentences
    filtered_sentences = []
    for sentence in summary_sentences:
        if len(sentence) > 1 :
            filtered_sentences.append(sentence.strip())

    # Return the specified number of sentences
    filtered_sentences = list(set(filtered_sentences))
    return filtered_sentences[:num_sentences]

# Main function
def summarize_webpage(url, num_sentences=3):
    html = get_webpage_content(url)
    text = extract_text(html)
    summary_sentences = summarize_text(text, num_sentences*5)  # Generate more sentences
    return summary_sentences

# Example usage
url ="https://www.tcs.com/"
num_sentences = 10

summary_sentences = summarize_webpage(url, num_sentences)
print("Summary Sentences:")
for i, sentence in enumerate(summary_sentences):
    print(f"{i+1}. {sentence}")
