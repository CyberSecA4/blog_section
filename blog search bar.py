#correct code for blog section search  bar with search bar
from googlesearch import search

# Function to search for articles from a specific website based on multiple queries
def search_articles_by_queries(site, queries, num_results=10):
    results = []
    try:
        for query in queries:
            for idx, url in enumerate(search(query + " site:" + site), start=1):
                results.append(url)
                if idx >= num_results:
                    break
    except Exception as e:
        print("Error searching:", e)
    return results

# Function to display search results
def display_results(results):
    for idx, url in enumerate(results, start=1):
        print(f"{idx}. {url}")

# Get user input for the search query
def get_search_query():
    query = input("Enter the search query: ")
    return query

# Example usage
if __name__ == "__main__":
    websites = ["https://medium.com/", "https://www.analyticsvidhya.com/", "https://twitter.com/"]
    queries = [get_search_query()]  # Get the search query from user input
    max_results = 10
    for website in websites:
        search_results = search_articles_by_queries(website, queries, num_results=max_results)
        display_results(search_results)
