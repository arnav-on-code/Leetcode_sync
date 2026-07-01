# LeetCode Sync

A Python-based automation tool that synchronizes accepted LeetCode solutions to GitHub without relying on third-party browser extensions.

## Objective

This project aims to build a secure and customizable alternative to browser extensions by automating the entire workflow—from fetching accepted LeetCode submissions to committing and pushing them to a GitHub repository.

## Planned Features

* Fetch accepted LeetCode submissions
* Download submitted source code
* Organize solutions by problem number and title
* Automatically generate and update a README
* Commit and push new solutions to GitHub
* Scheduled synchronization using GitHub Actions
* Logging and error handling
* Modular and extensible project architecture
* Unit tests for core components

## Project Structure

```text
leetcode-sync/
│
├── README.md
├── requirements.txt
├── .env.example
├── config.py
├── main.py
│
├── leetcode/
├── github_sync/
├── storage/
├── logs/
├── tests/
└── .github/
    └── workflows/
```

## Tech Stack

* Python
* Git
* GitHub Actions
* Requests
* BeautifulSoup
* GitPython
* python-dotenv
* Pytest

## Project Status

🚧 This project is currently under active development.

The first milestone focuses on setting up the project structure before implementing LeetCode authentication, solution synchronization, Git automation, and scheduled workflows.

## License

This project is intended for educational and personal use.
