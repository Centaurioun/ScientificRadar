import re
import requests


def fetch_wikipedia_url(term, access_token):
    """Fetch the Wikipedia URL for a given term using the Wikipedia API with authorization."""
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {"action": "query", "format": "json", "list": "search", "srsearch": term}
    headers = {
        "Authorization": f"Bearer {access_token}",
        "User-Agent": "YourAppName (your.email@example.com)",
    }
    response = requests.get(base_url, params=params, headers=headers)
    search_results = response.json().get("query", {}).get("search", [])
    if search_results:
        return f"https://en.wikipedia.org/wiki/{search_results[0]['title'].replace(' ', '_')}"
    return None


def replace_terms_with_links(text, terms, access_token):
    """Replace terms in the text with Wikipedia links that open in a new tab."""
    for term in terms:
        url = fetch_wikipedia_url(term, access_token) or f"URL not found for {term}"
        text = re.sub(
            rf"\b{term}\b",
            f'<a href="{url}" target="_blank">{term}</a>',
            text,
            flags=re.IGNORECASE,
        )
    return text


def main(access_token):
    # Load terms from a file
    with open(
        "/Users/aldorias/Library/CloudStorage/OneDrive-Centaurioun/ScientificRadar/articles/Vitamin-D/scientific_terms.txt",
        "r",
        encoding="utf-8",
    ) as file:
        terms = [line.strip() for line in file]
    # Read the article from a file
    with open(
        "/Users/aldorias/Library/CloudStorage/OneDrive-Centaurioun/ScientificRadar/articles/Vitamin-D/article.txt",
        "r",
        encoding="utf-8",
    ) as file:
        content = file.read()
    # Replace terms in the content with their Wikipedia links
    updated_content = replace_terms_with_links(content, terms, access_token)
    # Write the updated content back to the file
    with open(
        "/Users/aldorias/Library/CloudStorage/OneDrive-Centaurioun/ScientificRadar/articles/Vitamin-D/article.txt",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(updated_content)


if __name__ == "__main__":
    your_access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI3MjE4Yzg4M2JjOThlNmNkZGRjNjZjM2E4MWQ1ZTQ0MyIsImp0aSI6IjUxY2JmZjcxMzE0MmY2NmUxYjA4OWRkOGRhYjk3YmMxYzgxMmZjOWJhNGIyNjY1NzQ1ZTY1OTMxMTZjYmY4OWFhNzVjNWQ2NzczZTkzOTdjIiwiaWF0IjoxNzEzNjQ0MjQ1LjIyMDY3NSwibmJmIjoxNzEzNjQ0MjQ1LjIyMDY3OCwiZXhwIjozMzI3MDU1MzA0NS4yMTkwMjUsInN1YiI6Ijc1NDc1NjE0IiwiaXNzIjoiaHR0cHM6Ly9tZXRhLndpa2ltZWRpYS5vcmciLCJyYXRlbGltaXQiOnsicmVxdWVzdHNfcGVyX3VuaXQiOjUwMDAsInVuaXQiOiJIT1VSIn0sInNjb3BlcyI6WyJiYXNpYyJdfQ.Q4whzpfp_gD2kUQmoAUSoCT4R9gxpk8hJQxMxNUU_lFZnUISXfm4wIK2SXyvd12pBvX5E8_rwYKE0_DZDzRYn2UrIIoHtdRKvhd3mEPH2C-CGKjqrHMlCXj-E2JdXvU9MWbTOI9qbuTiS6DVBtJR-jvqRu6eA936YonE4bp4tYZWsDwxkdIvfUfaM5KdhcTwaf4wPk6bHvVKw6RVar-N2jN2vPpTRa35wjQ9f4fvajMAdFbT_tGgOULkmcqDQv2yV27QzDEIgx9_BqVbXhX3wTgxl9tL6pzVYQzrdraTPvA8VmLWX6k7Pksw3RhQirwk526n7MFhWsEMvcHtE4awCHpezEr7w6qG8knSq0eIx0BM8csXn5dPvIINON1-Tp3ILh8kRqzOoW9-VhhhnX61e7oE3ZM7nvwRXXyLIKzTBZJfvXmW5Qcw8j6y5RrkUeYjQ4rNSsE7n-FjH5TB3gFV9hvi1uVkAPv19pi0PatT_9z1zwrwCxnrwmwTy5USrpUyFqJ5ocCVXGkvfdR1c_h_5qGgWNJDTGVD43ZJ-sM6STvCyJqGP06Q6ynyYJF75AB8QM9NjbyVsJ2xT1kY9hcbXNb8Ue_qB522CameZe75YD7-480Gd7sMwFmadXhGayxIv8PS0TW8-6PLAsOrNfemmAFWYOc9X-0NLstd9IQPN3k"  # Replace with your actual access token
    main(your_access_token)
