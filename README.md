<div align="center">

# 🚀 LeetCode Sync

Automatically synchronize accepted LeetCode solutions to GitHub.

Download solutions • Generate metadata • Update README • Push to GitHub automatically

Built with ❤️ in Python

</div>

## Badges

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Tests](https://github.com/arnav-on-code/LEETCODE_SYNC/actions/workflows/tests.yml/badge.svg)
![Lint](https://github.com/arnav-on-code/LEETCODE_SYNC/actions/workflows/lint.yml/badge.svg)
![Sync](https://github.com/arnav-on-code/LEETCODE_SYNC/actions/workflows/sync.yml/badge.svg)
![License](https://img.shields.io/github/license/arnav-on-code/LEETCODE_SYNC)


## ✨ Features

- ✅ Automatic LeetCode authentication
- ✅ Fetch recent accepted submissions
- ✅ Download source code
- ✅ Save metadata
- ✅ Git automation
- ✅ README generation
- ✅ Statistics tracking
- ✅ GitHub Actions automation
- ✅ Unit tested


## 🏗️ Architecture

```text
LeetCode
      │
      ▼
 Authentication
      │
      ▼
 API Client
      │
      ▼
 Parser
      │
      ▼
 Downloader
      │
      ▼
 Statistics
      │
      ▼
 README Generator
      │
      ▼
 Git Manager
      │
      ▼
 GitHub
```

## ⚙️ Installation

```bash
git clone https://github.com/arnav-on-code/LEETCODE_SYNC.git

cd LEETCODE_SYNC

python -m venv myenv

pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env`

```text
LEETCODE_SESSION=

CSRF_TOKEN=

LEETCODE_USERNAME=

GITHUB_USER=

GITHUB_EMAIL=
```

## 🚀 Usage

Run manually

```bash
python main.py
```

Run tests

```bash
pytest tests -v
```

Format code

```bash
black .
```

Lint

```bash
flake8 .
```

## 📊 Statistics

Easy

Medium

Hard

Total

Languages

Recent Problems

Latest Accepted

Last Sync


## 📂 Repository Structure

```text
Leetcode_sync
│
├── .github/
├── config/
├── github_sync/
├── leetcode/
├── storage/
├── sync/
├── tests/
├── utils/
├── README.md
├── requirements.txt
└── main.py
```

## 🧪 Testing

Current Status

- ✅ 23 Unit Tests
- ✅ GitHub Actions
- ✅ Lint Checks
- ✅ Automatic Synchronization


## 🤖 GitHub Actions

Three workflows are configured.

• tests.yml

Runs all unit tests.

• lint.yml

Checks formatting and linting.

• sync.yml

Automatically synchronizes LeetCode submissions every 6 hours.

## 🛣️ Roadmap

- [x] Authentication

- [x] Downloader

- [x] Metadata

- [x] Statistics

- [x] README Generator

- [x] GitHub Actions

- [x] Unit Tests

- [x] README Automation

- [ ] Docker Image

- [ ] Multi-language README

- [ ] PyPI Package


## 📜 License

This project is licensed under the MIT License.

## 📖 About

LeetCode Sync automatically downloads accepted LeetCode solutions, stores them with metadata, updates repository statistics, regenerates the project README, and synchronizes everything to GitHub.

The project is designed with a modular architecture and includes automated testing, CI workflows, and Git integration.