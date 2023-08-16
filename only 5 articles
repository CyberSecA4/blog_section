from googlesearch import search

# Function to search for cybersecurity-related articles from a specific website
def search_cybersecurity_articles(site, queries, max_results=10):
    results = []
    try:
        for query in queries:
            for url in search(query + " site:" + site):
                results.append(url)
                if len(results) >= max_results:
                    return results
    except Exception as e:
        print("Error searching:", e)
    return results

# Function to display search results
def display_results(results):
    for idx, url in enumerate(results, start=1):
        print(f"{idx}. {url}")

# Example usage
if __name__ == "__main__":
    websites = ["https://medium.com/", "https://www.analyticsvidhya.com/"]  # Replace with the websites where you want to search for articles
    queries = [
        "cybersecurity ransomware articles",
        "cybersecurity network security articles",
        "cybersecurity best practices articles"
    ]  # Your list of search queries here
    max_total_results = 5  # Total number of articles to display
    search_results = []
    for website in websites:
        search_results += search_cybersecurity_articles(website, queries, max_total_results - len(search_results))
        if len(search_results) >= max_total_results:
            break
    display_results(search_results[:max_total_results])
