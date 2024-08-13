
# Dettingen Music Library

## UX Design

The Dettingen Music Library App is designed to provide a user-friendly experience for musicians and administrators. The app allows users to browse, filter, and manage a comprehensive library of musical scores based on their user status. Key design considerations include:

-  **Intuitive Navigation:** Easy access to the music library, user created setlists, and administrative account management.

-  **Responsive Design:** Ensuring the app is accessible on various devices, including desktops, tablets, and smartphones.

![Responsivity](static/readme/Responsivity.png)

-  **Clear Visual Hierarchy:** Use of consistent colours, typography, and spacing to guide users through the app's functionalities.

### Wireframe Design

![Sign in Page](static/readme/Sign%20in.png)

![Library Page](static/readme/Library%20Page.png)

![Piece View Page](static/readme/Piece%20View.png)

![Setlist Page](static/readme/Setlists.png)
  

## Features

![Mindmap Screenshot](static/readme/Mind%20Map.jpg)

  

### User Authentication

-  **User Login:** Secure login for all users to access the app.

-  **Admin Login:** Additional privileges for admins to manage the library.

  

### Library Management (Admin Only)

-  **Add Items:** Admins can add new music scores to the library.

-  **Edit Items:** Admins can update existing music scores.

-  **Remove Items:** Admins can delete outdated or irrelevant scores.

  

### Setlist Management

-  **Create Setlist:** Users can create personalized setlists.

-  **Edit Setlist:** Users can modify their existing setlists.

-  **Delete Setlist:** Users can remove setlists they no longer need.

  

### Printing

-  **Print Library List:** Users can print a complete list of the music library.

-  **Print Setlist:** Users can print their setlists for use in rehearsals or performances.

-  **Print Individual Score Parts:** Users can print individual PDF parts for specific scores.

  

### Library Filtering

-  **Filter by Genre:** Users can filter the library based on musical genres.

-  **Filter by Band Arrangement:** Users can filter the library based on band arrangements.

  

### Location Information

-  **March Card Location:** Users can view the physical location of march card versions of scores.

  

## Github Repository

  

### Kanban Board

![Kanban Board Screenshot](static/readme/Kanban%20Board.png)

  

### Milestones

![Milestones Screenshot](static/readme/Milestones.png)

  

### Roadmap

![Milestone Roadmap Screenshot](static/readme/Milestone%20Roadmap.png)

  

## Technologies

### Frontend

-  **CSS:** Styling the app to ensure a consistent and attractive user interface.

-  **HTML:** Structuring the app's content and layout.

-  **JavaScript:** Adding interactivity and dynamic elements to the app.

  

### Backend

-  **Django:** A high-level Python web framework for building the app's backend and managing the database.

-  **PostgreSQL:** A powerful, open-source object-relational database system for storing music scores and user data.

  

## Manual Testing Write-Up

### Testing Overview

Manual testing was conducted to ensure the app's features work as expected. The following aspects were tested:

-  **User Authentication:** Verified that users can log in, and that admins have additional privileges.

-  **Library Management:** Confirmed that admins can add, edit, and remove music scores.

-  **Setlist Management:** Ensured users can create, edit, and delete setlists.

-  **Printing Functionality:** Checked that users can print the library list, setlists, and individual score parts.

-  **Filtering:** Tested the filtering by genre and band arrangement to ensure accurate results.

-  **Location Information:** Verified that the location of march card versions is displayed correctly.

  

### Test Cases

1.  **Login/Logout:** Test valid and invalid login credentials, and ensure successful logout.

2.  **Add/Edit/Remove Library Items:** Test adding, editing, and removing music scores as an admin.

3.  **Create/Edit/Delete Setlist:** Test the creation, modification, and deletion of setlists.

4.  **Print Features:** Test printing the library list, setlists, and individual score parts.

5.  **Filter Library:** Test filtering the library by genre and band arrangement.

6.  **View Location:** Test displaying the location of march card versions.

  

### Results

All manual tests were passed successfully. Any issues found were promptly addressed and re-tested.

  

## Deployment Using Heroku

### Prerequisites

- Heroku account

- Git installed locally

  

## Credits

- Bootstrap Documentation

- Django Documentation

- SweetAlert2 Documentation

- ChatGPT