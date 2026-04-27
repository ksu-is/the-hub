# The Hub

The Hub is an all-in-one platform designed for college students to manage assignments, finances, fitness, and internships in one place. It aims to streamline student life by providing a centralized dashboard for various academic and personal trackers.

## Features

- **Assignment Tracker**: Keep track of your coursework, filter by class, and monitor your progress. (Completed)
- **Internship Tracker**: Manage internship applications and their status. (Completed)
- **Finance Tracker**: Manage your budget and expenses. (Completed)
- **Fitness Tracker**: (In progress)

## Tech Stack

- **Language**: Python 3
- **Framework**: Flask (Web Framework)
- **Frontend**: HTML, CSS (Jinja2 templates)

## Requirements

- Python 3.x
- Flask

## Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/the-hub.git
cd the-hub
```

### 2. Install dependencies
Install the necessary dependencies using `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Run the application
Navigate to the source directory and run `main.py`:
```bash
python The-Hub/main.py
```
The application will be available at `http://127.0.0.1:5007/`.

## Scripts
*TODO: Add automated scripts for setup, testing, or deployment (e.g., a Makefile or shell scripts).*

## Environment Variables
No environment variables are currently required to run the project.
*TODO: Implement configuration management using environment variables for sensitive data or environment-specific settings.*

## Tests
*TODO: Implement unit and integration tests to ensure application stability.*

## Project Structure

```text
.
├── LICENSE                 # MIT License
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── roadmap                 # Development roadmap and sprint plans
└── The-Hub/                # Source code directory
    ├── main.py             # Entry point of the Flask application
    ├── static/             # Static assets (CSS, Images)
    │   ├── assignments.css
    │   ├── index.css
    │   └── logo.png
    └── templates/          # HTML templates
        ├── assignments.html
        ├── finances.html
        ├── index.html
        └── internships.html
```

## Team Members
- Kimora Robinson

## License
Distributed under the MIT License. See `LICENSE` for more information.