# Learning Log

Learning Log is a web application designed to help you track your learning journey. Create topics you're studying and log daily entries to document your progress, insights, and resources. Whether you're learning a new language, programming, or any skill, Learning Log keeps your notes organized and accessible.

## Features

- **User Authentication**: Register, log in, and manage your personal learning logs securely.
- **Topic Management**: Create, edit, and delete topics (e.g., "Python", "Spanish", "History").
- **Entry Logging**: Add, edit, and delete entries for each topic. Each entry can include text, code snippets, or links.
- **Responsive Design**: Built with Bootstrap for a seamless experience on desktop and mobile devices.
- **Easy Navigation**: View all your topics and their entries in a clean, intuitive interface.

## Technologies Used

- **Backend**: Python, Django (including built-in authentication and admin interface)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite (development) / PostgreSQL (production)
- **Version Control**: Git

## Installation

Follow these steps to set up Learning Log locally.

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning)

### Steps

1. **Clone the repository** (or download the source code):
   ```bash
   git clone git@github.com:Software-dev804/Learning_logs-page.git
   cd learning-log
   #for HTTPS clone use:
   git clone https://github.com/Software-dev804/Learning_logs-page.git
   ```

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (to access the admin panel):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Open your browser** and go to `http://127.0.0.1:8000` to start using Learning Log.

## Usage

1. **Register** a new account or log in if you already have one.
2. **Create a topic** (e.g., "Python") from the dashboard.
3. **Add entries** to a topic by clicking on the topic and selecting "Add new entry".
4. **Edit or delete** entries and topics as needed.
5. Use the **admin panel** at `http://127.0.0.1:8000/admin` to manage users and data directly (superuser access required).

## Contributing

Contributions are welcome! If you'd like to improve Learning Log, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Open a pull request.

Please ensure your code follows the existing style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the "Learning Log" project from the book *Python Crash Course* by Eric Matthes.
- Built with Django and Bootstrap.

---

**Happy Learning!** 📚
