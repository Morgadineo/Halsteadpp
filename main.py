import argparse
from halsteadpp.parsedcode import ParsedCode

def main():
    parser = argparse.ArgumentParser(
        description="Halstead++ — Analyze Halstead and Cyclomatic complexity metrics in C source code."
    )

    parser.add_argument(
        "name",
        help="Base name of the preprocessed C file (without extension). Example: article_example"
    )

    parser.add_argument(
        "-d", "--dir",
        default="./Examples/",
        help="Directory containing the preprocessed files (default: ./Examples/)"
    )

    args = parser.parse_args()

    print(f"🔍 Analyzing '{args.name}' in directory '{args.dir}'...")

    # Initialize analyzer
    code = ParsedCode(args.name, args.dir)

    if not code.has_errors:
        code.print_complexities()
        code.print_functions()
    else:
        print("❌ Error: Could not analyze the provided file. Make sure it was preprocessed correctly.")

if __name__ == "__main__":
    main()

