import json

if __name__ == '__main__':
    import estimates_scraper
    print(json.dumps(estimates_scraper.scrape_committees(), indent=2))