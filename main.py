from restricted import GoogleSheetUpdater, WebScraper

def main():
    print("yo")

    # webScraper = WebScraper()

    # df = webScraper.parse_html()

    gsUpdater = GoogleSheetUpdater()

    gsUpdater.set_worksheet("11/2023")

    print("we init")

    gsUpdater.update('B35', 'Hello, world!')

    print("done")

if __name__ == "__main__":
    main()
