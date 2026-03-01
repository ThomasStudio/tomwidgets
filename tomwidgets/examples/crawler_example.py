import tkinter as tk
from ..tools.Crawler import Crawler


def main():
    # Create the Crawler instance
    crawler = Crawler(title="Web Crawler Demo")
    crawler.pack(fill=tk.BOTH, expand=True)

    # Add some instructions
    print("🚀 Crawler Example Started")
    print("=" * 50)
    print("Instructions:")
    print("1. Enter a URL in the URL bar (e.g., https://example.com)")
    print("2. Click 'Download' or press Enter to fetch the HTML")
    print("3. Enter a regex pattern in the search bar")
    print("4. Click 'Search' or press Enter to find matches")
    print("5. Use TextTwo features to compare and manipulate text")
    print("=" * 50)

    crawler.show()


if __name__ == "__main__":
    main()