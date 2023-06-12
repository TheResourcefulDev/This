import os
from dotenv import load_dotenv
from github import Github

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("API_KEY")

# Check if the API key is provided
if api_key is None:
    print("API key not found. Please provide your API key in the .env file.")
    exit()


def main():
    # Create a GitHub instance using the API key
    github = Github(api_key)

    # Specify the repository where the file will be uploaded
    repo_owner = "TheResourcefulDev"
    # needs adding input for repo
    repo_name = "This"

    # Get the repository
    repo = github.get_repo(f"{repo_owner}/{repo_name}")

    UPLOAD_FILE = True
    # Specify the details of the new file
    while UPLOAD_FILE == True:
        file_path = input("Enter/Paste file path {q for quit}")
        commit_message = "Add new file"

        if file_path == 'q':
            UPLOAD_FILE = False
            

        try:
            # Read the file content from the file path
            with open(file_path, "r") as f:
                file_content = f.read()

            # Create the new file in the repository
            repo.create_file(file_path, commit_message, file_content)

            print(f"New file '{file_path}' has been uploaded to the repository.")
        except:
            print(" !!! No file uploaded !!! ")
if __name__ == '__main__':
    main()