# Automated-Comment-Sorter

## Description

**Automated-Comment-Sorter** is a Streamlit application designed to analyze and sort comments based on their sentiment. Leveraging the `distilbert` model from the `transformers` library, this application classifies comments into positive or negative sentiments and displays them with color-coded backgrounds accordingly. The app also features interactive elements like input fields and video embedding to enhance user experience.

## Features

- **Sentiment Analysis**: Utilizes the `distilbert` model for classifying comments into positive or negative sentiments.
- **Comment Sorting**: Allows users to sort comments based on their sentiment.
- **Dynamic Comment Display**: Comments are shown with a color-coded background indicating their sentiment (Green for Positive, Red for Negative).
- **Interactive UI**: Includes fields for user input, comment addition, and video display.

## Requirements

To run this project, you need to install the following Python packages:

- `streamlit`
- `transformers`

## Installation

1. **Clone the Repository**

- git clone https://github.com/siddhantjain603/Automated-Comment-Sorter.git
- cd Automated-Comment-Sorter

### 2. Install Dependencies

- pip install -r requirements.txt

### 3. Run the Application

- streamlit run main.py

## Usage

- **Enter Your Username**: Provide your username in the input field.
- **Add a Comment**: Type in a comment in the text field and click "Add Comment".
- **Sort Comments**: Use the dropdown menu to sort comments by sentiment (Positive or Negative).
- **View Comments**: Added comments are displayed with a color-coded background based on their sentiment.
