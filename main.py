from Comvis import ParsedCode

if __name__ == "__main__":
    dirs = "./Examples/"
    code = "article_example"

    code = ParsedCode(code, dirs)

    if not code.has_errors:
        code.print_complexities()
        code.print_functions()


