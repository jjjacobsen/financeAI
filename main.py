# flake8: noqa: E501
import os
from restricted.google import GoogleSheetUpdater
from restricted.parse import DataParser


def main():
    print("Welcome to financeAI!")

    gsUpdater = GoogleSheetUpdater()
    dataParser = DataParser()

    while True:
        print("\nOptions:")
        print("1. Financial Advice")
        print("2. Update Data Manually")
        print("3. Update Data with AI")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nNot implemented yet")
        elif choice == "2":
            month = input("\nWhich month do you want to update? (e.g. 11/2023): ")
            if month == "q":
                continue

            gsUpdater.set_worksheet(month)
            df = dataParser.filter_by_month(month)
            total_transactions_count = len(df)
            categories = {
                "1": ["rent + utilities", 0],
                "2": ["other monthly payments", 0],
                "3": ["groceries", 0],
                "4": ["food / whiskey / cigars", 0],
                "5": ["fuel / parking / transportation", 0],
                "6": ["fun", 0],
                "7": ["insurance", 0],
                "8": ["vehicle payments", 0],
                "9": ["student loans payments", 0],
                "10": ["misc", 0],
                "11": ["earned", 0],
            }
            earned_key = "11"
            index = 0
            skip_counter = 0
            print(f"Set worksheet to {month}")

            while index < total_transactions_count:
                print(
                    f"\nTransaction {index}/{total_transactions_count} ({index / total_transactions_count * 100:.2f}%)"
                )
                print(f"{df.iloc[index]}")
                sub_choice = input(
                    "\t".join(
                        [f"{key}) {value[0]}" for key, value in categories.items()]
                    )
                    + "\tp) print current values"
                    + "\ts) skip this transaction"
                    + "\tq) quit\n"
                )
                if sub_choice == "q":
                    break
                elif sub_choice == "p":
                    print(categories)
                    continue
                elif sub_choice == "s":
                    index += 1
                    skip_counter += 1
                    continue
                elif sub_choice in categories:
                    amount = float(abs(df.iloc[index]["Amount"]))
                    categories[sub_choice][1] = round(
                        categories[sub_choice][1] + amount, 2
                    )
                    df.loc[df.index[index], "Category"] = categories[sub_choice][0]
                    index += 1
                else:
                    print("Invalid choice. Please try again")
                    continue

            if sub_choice != "q":
                csv_file = "restricted/history.csv"
                df.to_csv(
                    csv_file, mode="a", header=not os.path.exists(csv_file), index=False
                )
                print(f"Wrote data to {csv_file}")

                print(
                    f"\nTransaction {index}/{total_transactions_count} ({index / total_transactions_count * 100:.2f}%)"
                )
                print("Attempting to push data to Google Sheets...")

                total_expenses = sum(
                    value[1] for key, value in categories.items() if key != earned_key
                )

                values = [
                    [name, round(amount, 2)] for name, amount in categories.values()
                ]
                values.append(["total expenses", round(total_expenses, 2)])
                values.append(
                    [
                        "net monthly",
                        round(categories[earned_key][1] - total_expenses, 2),
                    ]
                )

                gsUpdater.update(values, "A2")
                gsUpdater.update(
                    [
                        [
                            "total number of transactions",
                            total_transactions_count - skip_counter,
                        ]
                    ],
                    "A16",
                )
                print("Pushed data to Google Sheets")

        elif choice == "3":
            print("\nNot implemented yet")
        elif choice == "q":
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice. Please try again")


if __name__ == "__main__":
    main()
