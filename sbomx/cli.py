import argparse #handles terminal arguments
from .scanner import scan_project # runs the SBOM scanner


def main():
    # create the command line argument parser
    parser = argparse.ArgumentParser(description="Generate a Software Bill of Materials.")

    # Add the project path argument
    parser.add_argument("project", help="Path to the project to scan.")

    # Add the output file argument.
    parser.add_argument("-o", "--output", default="sbom.json", help="Output JSON file.")

    # Read the arguments from the terminal.
    args = parser.parse_args()

    try:
        # Scan the project
        sbom = scan_project(args.project)
    
        # Save the generated SBOM
        sbom.to_json(args.output)
    
        # tell the user where the SBOM was saved
        print(f"SBOM generated: {args.output}")
    
    except(FileNotFoundError, NotADirectoryError) as error:
        # show clean error instead of a traceback
        parser.error(str(error))

if __name__ == "__main__":
    main()
