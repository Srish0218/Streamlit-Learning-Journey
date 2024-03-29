# Streamlit Learning Journey 
This repository captures my learning journey with Streamlit, a powerful Python library for creating web applications with minimal effort. Here, you'll find a step-by-step exploration of Streamlit features through various tutorials provided by Nileg Production. Each tutorial covers different aspects of Streamlit, from basic text elements to advanced web scraping and web application development.

## Table of Contents

- [Introduction](#introduction)
- [Learning Path](#learning-path)
- [Libraries Used](#libraries-used)
- [Projects](#projects)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Streamlit provides a straightforward way to create interactive web applications using Python scripts. As I progress through these tutorials, I aim to build a solid understanding of Streamlit's capabilities and harness its potential to develop dynamic and engaging applications.
## Learning Path

| Day       | Topic                                                                                                                             |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------|
| **Day 1** | - [Streamlit Introduction](Notes/Notes.md)                                                                                        |
|           | - [Basic Elements](Basic-Elements.py)                                                                                             |
|           | - [Widgets](Wigets.py)                                                                                                            | 
|           | - [File Uploader Widget](Uploading-Files.py)                                                                                      |
|           | - [Timer App With Progress Bar](Wigets.py)                                                                                        |
| **Day 2** | - [Sidebar and Graph](Sidebar-Graph.py)                                                                                           |
|           | - [Forms](Streamlit%20Forms.py)                                                                                                   |
|           | - [Project 1. Image Editor]( Project1-Image-Editor.py)                                                                            |
| **Day 3** | - [Project 2. URL Shortener](Project2-URL-Shortener.py)                                                                           |
| **Day 4** | - [Project 3. SEO Analysis Web App](Project3-SEO-Analysis-Web-App.py)                                                             |
|           | - [GeeksforGeeks SEO Analysis Web App *(Updation of Project 3)*](https://github.com/Srish0218/GeeksforGeeks-SEO-Analysis-Web-App) |
|           | - [Project 4. SentimentAnalyzerApp](https://github.com/Srish0218/SentimentAnalyzerApp)                                            |
| **Day 5** | - [Cache](cache.py)                                                                                                               |
|           | - [Call-Back property](Call-backs-Properties.py)                                                                                  |
|           | - [Session States](Session-States.py)                                                                                             |


## Libraries Used

- Streamlit
- Numpy
- Pillow
- matplotLib

## Projects

1. ### Image Editor
***Overview***

This Streamlit project implements a simple image editor. Users can upload an image (in PNG or JPG format), and the app displays information about the image, such as size, mode, and format. Users can also perform image editing operations, including resizing, rotating, and applying filters like blur, detail, emboss, and smooth.

***Technologies Used***

- [Streamlit](https://www.streamlit.io/): A Python library for creating web applications with minimal effort.
- [PIL (Pillow)](https://pillow.readthedocs.io/): A Python Imaging Library that adds image processing capabilities to your Python interpreter.
***How to Run***
    ```bash
    streamlit run Project1-Image-Editor.py
***Live Demo***

[Demo](https://srish-image-editor.streamlit.app/)

***Usage***
- Launch the Streamlit app using the provided instructions.
- The app will open in your web browser. 
- Upload an image by clicking the "Upload Your Image" button. 
- The app will display information about the uploaded image, including size, mode, and format. 
- Perform image editing operations:
   - Adjust width and height for resizing.
   - Enter degrees for rotation.
   - Choose a filter (Blur, Detail, Emboss, Smooth) or select "None" for no filter. 
- Click the "Submit" button to apply the edits and view the updated image.

2. ### URL-Shortener

**Overview**

This is a simple URL shortener application built using Streamlit, PyShorteners, and Pyperclip. It allows users to enter a URL, submit it, and obtain a shortened version of the URL. The application is designed to be user-friendly and efficient.

**Technologies Used**
- **Streamlit**: A Python library for creating web applications with minimal code.
- **PyShorteners**: A Python library for interacting with various URL shortening services.
- **Pyperclip**: A cross-platform clipboard module for copying and pasting text.

**How to Run**
1. **Install Dependencies:**
   ```bash
   pip install streamlit pyshorteners pyperclip
2. **Run the App:**
   ```bash
   streamlit run Project2-URL-Shortener.py

***Live Demo***

[Demo](https://srish-url-shortener.streamlit.app/)

***Usage***
- Open the application in your web browser.
- Enter the URL you want to shorten in the provided input field.
- Click the 'Submit' button.
- The shortened URL will be displayed on the screen. 
- Optionally, click the 'Copy' button to copy the shortened URL to your clipboard.

*Feel free to explore each day's tutorial to see the code and learn about different aspects of Streamlit. Happy coding!*

## Getting Started

If you're interested in following my learning journey or contributing to this project, follow these steps to get started:

1. Clone the repository:

   ```bash
   git clone https://github.com/Srish0218/Streamlit-Learning-Journey.git

## Contributing
*If you'd like to contribute to this learning repository, please check the Contribution Guidelines for more information. Contributions, feedback, and suggestions are highly appreciated!*

## License
*This project is licensed under the MIT License. Feel free to use, modify, and distribute the code for your learning purposes.*