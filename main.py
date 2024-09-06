from restricted import GoogleSheetUpdater, WebScraper


def main():
    print("Welcome to financeAI!")

    gsUpdater = GoogleSheetUpdater()
    webScraper = WebScraper()

    while True:
        print("\nOptions:")
        print("1. Financial Advice")
        print("2. Update Data Manually")
        print("3. Update Data with AI")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nNot implemented yet")
        elif choice == '2':
            month = input("\nWhich month do you want to update? (e.g. 11/2023): ")
            if month == 'q':
                continue

            gsUpdater.set_worksheet(month)
            df = webScraper.filter_by_month(month)
            total_transactions_count = len(df)
            end_of_month_balance = round(float(df.iloc[0]['Account Balance'][1:].replace(",", "")), 2)
            categories = {
                '1': ['rent + utilities', 0],
                '2': ['other monthly payments', 0],
                '3': ['groceries', 0],
                '4': ['food / whiskey / cigars', 0],
                '5': ['gas', 0],
                '6': ['fun', 0],
                '7': ['insurance', 0],
                '8': ['vehicle payments', 0],
                '9': ['student loans payments', 0],
                '10': ['misc', 0],
                '11': ['earned', 0]
            }
            index = 0
            print(f"Set worksheet to {month}")

            while index < total_transactions_count:
                print(f"\nTransaction {index}/{total_transactions_count} ({index / total_transactions_count * 100:.2f}%)")
                print(f"{df.iloc[index]}")
                sub_choice = input("\t".join([f"{key}) {value[0]}" for key, value in categories.items()]) + "\tprint) show current values\n")
                if sub_choice == 'q':
                    break
                elif sub_choice == 'print':
                    print(categories)
                    continue
                elif sub_choice in categories:
                    str_value = df.iloc[index]['Transaction Price']
                    if str_value[0] == '$':
                        float_value = float(str_value[1:].replace(",", ""))
                    else:
                        float_value = float(str_value[2:].replace(",", ""))
                    categories[sub_choice][1] = round(categories[sub_choice][1] + float_value, 2)
                    index += 1
                else:
                    print("Invalid choice. Please try again")
                    continue

            if sub_choice != 'q':
                print(f"\nTransaction {index}/{total_transactions_count} ({index / total_transactions_count * 100:.2f}%)")
                print("Attempting to push data to Google Sheets...")

                total_expenses = sum(value[1] for key, value in categories.items() if key != '11')

                values = [[name, round(amount, 2)] for name, amount in categories.values()]
                values.append(["total expenses", round(total_expenses, 2)])
                values.append(["net monthly", round(categories['11'][1] - total_expenses, 2)])

                gsUpdater.update(values, "A3")
                gsUpdater.update([["total number of transactions", total_transactions_count]], "A17")
                gsUpdater.update([["checking", end_of_month_balance]], "A20")
                print("Pushed data to Google Sheets")

        elif choice == '3':
            print("\nNot implemented yet")
        elif choice == 'q':
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice. Please try again")


if __name__ == "__main__":
    main()
