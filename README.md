# Personal Finance Management CLI Application

This is a CLI-based personal finance management application built with Python and SQLite. The application allows users to manage their financial transactions, categories, and user accounts.

## Features

- Register a new user
- List all users
- Add a new transaction
- List all transactions for a user
- Delete a transaction
- Add a new category
- List all categories
- Delete a category

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/shukridida/python-p3-v2-final-project-template.git
    cd finance-cli-app
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Initialize the database:

    ```sh
    python create_db.py
    ```

## Usage

Run the main CLI program:

```sh
python lib/cli.py
