# JPM and Sons

I wanted to make a web application that is thoughtful in terms of user experience and can also bring users in. This project is still a work in progress in terms of the marketing and SEO optimization aspect of it. I have enjoyed learning all the technologies behind it, even though at times it has been frustrating. I first started this in March 2024, and it was my introduction to web development. It’s also what led me to enroll in Springboard’s bootcamp because I found it interesting and something that I can turn into a career. I later revisited this project once I gained more knowledge in Flask and expect to revisit it again once I have more front-end skills or new tools to implement. I want to add more functionality to it as I continue learning, more so on the front end,

---

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Database Schema](#database-schema)

---

## Project Overview

This project is a website for **JPM and Sons**, a home improvement business offering various services such as masonry, concrete, and powerwashing. The goal is to provide a modern and responsive platform where users can:
- View services
- Request quotes
- Learn about past projects
- Engage with the business through form submissions and direct communication.

The primary goals are to drive traffic to the website, engage users, and provide a seamless and user-friendly experience.

### Target Audience:
- Homeowners or businesses looking for home improvement services.
- Potential clients interested in requesting quotes or learning more about available services.

---

## Tech Stack

### Front-End:
- **HTML & CSS**: For structuring and styling the UI.
- **Bootstrap**: For responsive design and faster UI development.
- **JavaScript**: For dynamic content and interactivity.

### Back-End:
- **Python with Flask**: For handling server-side logic and API development.
- **SQLAlchemy**: ORM for interacting with the database.
- **PostgreSQL**: Relational database for storing app data.
- **Flask-Mail**: For sending emails (e.g., notifications, password resets).
- **Flask-Login**: For user authentication and session management.
- **Pillow**: For serving images in webp format and resizing.

### Database Schema
[Click here](https://drawsql.app/teams/tony-26/diagrams/jpm-and-sons)

### Additional Tools:
- **Google Analytics**: For tracking and analyzing user behavior.
- **WTForms**: For creating and validating forms.

---

## Features

### **Admin Authentication**:
- Admin users can log in, manage form entries, and perform CRUD operations on users and projects.

### **Services Showcase**:
- A dedicated section to display home improvement services, providing detailed descriptions and pricing information.

### **Request a Quote**:
- Users can submit a form with their contact information and service request, allowing for easy quote generation and communication.

### **Project Gallery**:
- A gallery showcasing past projects completed by JPM and Sons to highlight the quality and range of services offered.

---

### Prerequisites:
- **Python 3**
- **PostgreSQL**
- **Virtual environment**

## Installation and Setup

### Clone the repository:
https://github.com/tonyrodriguez24/jpm-public

- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt