![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey.svg)

---

# 🏨 Hotel Listings Web App — Flask Mini Project

A lightweight **full-stack web application** built using **Flask**, designed to manage hotel listings. The app provides a responsive UI for browsing, adding, editing, and deleting hotel records, complete with user authentication and review functionality.

---

## 📋 Table of Contents

* [Features](#-features)
* [Tech Stack](#-tech-stack)
* [Getting Started](#-getting-started)
* [Project Structure](#-project-structure)
* [Routes Overview](#-routes-overview)
* [Future Enchnacements](#future-enhancements)
* [Limitations & Notes](#-limitations--notes)
* [License](#-license)

---

## ✅ Features

* 🏨 **Hotel Listings**
  Browse hotels with location, rating, price, and image.

* ➕ **CRUD Functionality**
  Add, edit, or delete hotel entries directly from the UI.

* 💬 **Comments & Ratings**
  Users can leave reviews and assign ratings (out of 5 stars).

* 🔐 **User Authentication**
  Basic in-memory login/signup system to simulate user management.

* 🌐 **Responsive Frontend**
  Clean UI built with HTML5 and CSS, suitable for desktop and mobile views.

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML5, CSS3, Jinja2 templating
* **Storage:** In-memory Python dictionaries (for learning/demo)
* **Deployment:** Localhost (Flask development server)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/rasika1205/Flask-Mini-Project.git
cd Flask-Mini-Project
```

### 2. Install Dependencies

```bash
pip install flask
```

> You can also create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install flask
```

### 3. Run the App

```bash
python app.py
```

Visit: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📁 Project Structure

```
Flask-Mini-Project/
│
├── app.py                  # Main Flask application
│
├── templates/              # Jinja2 HTML templates
│   ├── index.html          # Hotel listings
│   ├── home.html           # Welcome/homepage
│   ├── show.html           # Hotel detail view
│   ├── add.html            # Add new hotel form
│   ├── edit.html           # Edit existing hotel
│   ├── login.html          # User login form
│   └── signup.html         # User registration form
│
└── static/
    └── images/             # Hotel images referenced in app.py
```

---

## 🔗 Routes Overview

| Route                        | Description                     |
| ---------------------------- | ------------------------------- |
| `/`                          | Homepage                        |
| `/list_hotels`               | List all hotels                 |
| `/show/<hotel_name>`         | View hotel details              |
| `/new_hotel`                 | Add a new hotel                 |
| `/edit_hotel/<hotel_name>`   | Edit existing hotel info        |
| `/delete_hotel/<hotel_name>` | Delete a hotel entry            |
| `/add_comment/<hotel_name>`  | Add comment & rating to a hotel |
| `/signup`                    | User registration               |
| `/login`                     | User login                      |

---

## 🚀 Future Enhancements

Here are some planned improvements and features that can make this project more robust and production-ready:

* **🔐 Persistent Database Integration**
  Replace in-memory storage with a real database such as **SQLite**, **PostgreSQL**, or **MongoDB** for data persistence.

* **👤 User Authentication System**
  Implement full-fledged authentication using **Flask-Login**, password hashing with **bcrypt**, and role-based access control.

* **🖼️ Image Upload Functionality**
  Allow hotel owners or admins to upload images directly through a form instead of placing them in a static folder manually.

* **🌍 Search & Filter Options**
  Add advanced filters (by price, rating, location) and a search bar to improve the browsing experience.

* **📝 Hotel Booking System**
  Enable users to **book rooms**, select **check-in/check-out dates**, and view availability calendars.

* **⭐ Rating System with Averages**
  Enhance the rating system to calculate and display **average ratings** per hotel dynamically.

* **💬 Comment Moderation**
  Allow admins to **approve/delete comments** and flag inappropriate reviews.

* **📱 Responsive Design**
  Improve UI/UX for **mobile responsiveness** using Bootstrap or Tailwind CSS.

* **📧 Contact or Inquiry Form**
  Add a contact form to allow users to reach out to hotel owners/admins.

* **🌐 Multi-language Support**
  Add i18n support to allow users to browse the application in different languages.

* **🧪 Unit & Integration Testing**
  Add test coverage using **pytest** or **unittest** for reliability and CI/CD pipelines.

---

## 🧪 Limitations & Notes

* ⚠️ **Data Persistence**:
  No database is used; all hotel/user data is stored in-memory using Python dictionaries. Restarting the server will **reset all data**.

* 🖼️ **Static Images**:
  Make sure to place image files in the `static/images/` folder. Images must be manually added to this directory before referencing them in hotel entries.

* 🔐 **Authentication**:
  The login/signup system is simulated for demonstration. Passwords are stored in plain text and not meant for production.


---

## 📄 License

This project is provided **for educational and demonstration purposes only.**
No commercial license is granted.

---

*Developed with ❤️ by [Rasika Gautam](https://github.com/rasika1205)*

---

