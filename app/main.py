from app.cli.console import run_console
from app.ingest.pipeline import ingest_file


def main():
    while True:
        print("\nChoose option:")
        print("1. Ingest text file")
        print("2. Search console")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            path = input("Enter file path: ").strip()
            ingest_file(path)

        elif choice == "2":
            run_console()

        elif choice == "3":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
