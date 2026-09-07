def main():
    # Main entry point for the SBOMX command-line application.
    # This function will eventually handle commands such as:
    #     sbomx scan .
    #     sbomx scan ./my-project
    print("SBOMX")


# This condition is true when this file is executed directly.
# It prevents main() from running automatically when cli.py is imported
# by another Python module.
if __name__ == "__main__":
    main()