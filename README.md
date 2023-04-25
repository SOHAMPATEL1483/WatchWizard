# WatchWizard

This is a web application for recommending movies to users based on their preferences. The application is built using SvelteKit for the front-end and Django Rest Framework (DRF) for the back-end.

##### Website: [watchwizard.vercel.app](https://watchwizard.vercel.app/)
**Created by [Soham Patel](https://github.com/SOHAMPATEL1483) and [Sneh Patel](https://github.com/snehpatel1017)**

## Tools

- **Sveltekit**
  - Tailwind
  - Flowbite
- **Django**
  - rest framework
  - simplejwt package
  - numpy and pandas
- **Docker**

# Features
#### Sveltekit
Using different features of sveltekit like SSR,hooks,form actions,props for better user experience.

#### DRF
Used Django Rest framwork to design Rest API to implement Authentication , database **CRUD** Operations and provide interface for machine learning models to recommend movies

#### User Authentication
The application allows users to create accounts, log in and log out using Json Web Tokens. This feature ensures that each user's preferences and recommendations are kept private and secure.

#### Personalized Recommendations
The application uses a content and collaborative recommendation algorithm to provide personalized movie recommendations based on the user's preferences. Users can rate movies they have watched, and the application uses this information to suggest similar movies that the user may enjoy.

#### Movie Details
The application provides detailed information about each movie, including the title, summary, genre, release year, and cast. Users can browse recommended movies and view these details to decide whether they want to watch the movie.

#### User Account Management
On user page user can see information about movies that user have rated.

#### Responsive Design
The application is designed to work on desktop and mobile devices, with a responsive user interface that adapts to the screen size. This feature ensures that users can access the application from any device and have a consistent experience.

# Installation

**Clone the Repo**

```bash
git clone https://github.com/SOHAMPATEL1483/WatchWizard.git
```

**Frontend (Sveltekit)**

```bash

#go to working directory for sveltekit
cd frontend-sveltekit
#install packages
npm install
#start development server
npm run dev
#go to localhost:5173
```

**Backend(DRF)**

```bash
#go to working directory for DRF
cd Backend-DjangoRestFramework
#Create a virtual environment:
python -m venv env
#Activate the virtual environment:
Windows: env\Scripts\activate
Linux/Mac: source env/bin/activate
#Install the dependencies:
pip install -r requirements.txt
#Migrate the database:
python manage.py migrate
#Start the server:
python manage.py runserver
#this will start drf on port 8000
```

_For app to work properly both DRF and Sveltekit should be in working condition_
_Dataset used to train recommendation models can be found in /datasets folder_

### Contributing
If you would like to contribute to this project, please fork the repository and create a pull request.

### Gallery

** Landing Page **:

<img src="https://user-images.githubusercontent.com/86504280/234232499-bc0b0bca-8eeb-47f3-9cdd-d51a4d6845d7.jpeg">

**Home Page (Without Login)**:

<img src="https://user-images.githubusercontent.com/86504280/234233472-2fe81f29-a54e-4082-a02b-2f9ff7c2e3a8.jpeg">

**Home Page (With Login)**:

<img src="https://user-images.githubusercontent.com/86504280/234233592-1884eefd-bdcf-4fd3-aff3-16d4f0fd9d98.jpeg">

**Movie Page**:

<img src="https://user-images.githubusercontent.com/86504280/234233873-23dd0d6d-7889-4580-b603-e69d2b3fe5c0.jpeg">

**Sign In:**

<img src="https://user-images.githubusercontent.com/86504280/234234103-61ebe1e9-f6c4-4ddd-8042-55465aafcd5d.jpeg">

**Search Movie**:

<img src="https://user-images.githubusercontent.com/86504280/234234246-b8c6ab9d-53bf-4179-8d96-fff678e9fe7a.jpeg">

**User Page**:

<img src="https://user-images.githubusercontent.com/86504280/234232961-37b2c8cb-5995-4666-8278-20e08ede272e.jpeg">
