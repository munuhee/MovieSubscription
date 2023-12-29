# Movie Subscription Website

[![License](https://img.shields.io/badge/License-Apache-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python Version](https://img.shields.io/badge/Python-3.10-green)](https://www.python.org/downloads/)

This Django-based subscription movie website allows users to subscribe to access premium movies. The site includes user authentication, subscription handling, payment integration, and access control for premium content.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project structure is organized as follows:

- **MovieSubscription**: Django project root directory.
  - **movie**: App handling movie-related functionalities.
  - **user_profile**: App managing user profiles and watchlists.
  - **review**: App handling movie reviews.
  - **subscription**: App managing subscription plans and handling payments.

## Features

- **User Authentication**: Utilizes Django's built-in authentication system for user registration, login, and logout.
- **Movie Listing**: Displays a list of movies, categorized as most popular, TV series, and new releases.
- **Movie Details**: Provides detailed information about each movie, including description, trailers, reviews, etc.
- **Subscription Handling**: Allows users to subscribe to different plans offering access to premium content.
- **Payment Integration**: Integrates PayPal for subscription payments.
- **User Profiles**: Provides user profiles with a watchlist feature to bookmark favorite movies.

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/munuhee/MovieSubscription.git
   cd MovieSubscription
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # For Unix or MacOS
   # Or
   .\env\Scripts\activate  # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file based on `.env.example` and add your environment-specific variables like `PAYPAL_CLIENT_ID`, `PAYPAL_CLIENT_SECRET`, etc.

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

## Usage

1. Run the development server:
   ```bash
   python manage.py runserver
   ```

2. Access the website in your browser: [http://localhost:8000](http://localhost:8000)

3. Use the admin panel to manage movies, subscriptions, users, etc.: [http://localhost:8000/admin](http://localhost:8000/admin)

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.
