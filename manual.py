from restricted import GoogleSheetUpdater

def main():
    print("yo")

    gsUpdater = GoogleSheetUpdater()

    print("we init")

    gsUpdater.update('B62', 'Hello, world!')

    print("done")

if __name__ == "__main__":
    main()
