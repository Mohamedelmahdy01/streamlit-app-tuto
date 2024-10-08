---

# Career Recommendation System

This project provides a web-based application to recommend the most suitable career path based on user responses to a set of questions. It uses a machine learning model to predict the best career choice and offers recommendations through a user-friendly Streamlit interface.

## Features

- **Career Recommendation**: Based on user answers to questions about their interests and preferences.
- **Machine Learning Model**: Uses a RandomForestClassifier to predict the best career.
- **Streamlit Interface**: Interactive web application for users to get career recommendations.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/career-recommendation-system.git
   cd career-recommendation-system
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare Data**

   Ensure you have the dataset file `data.csv` in the same directory as the script.

5. **Run the Application**

   ```bash
   streamlit run app.py
   ```

## Usage

- **Navigate to the Web Application**: Open your browser and go to `http://localhost:8501`.
- **Answer the Questions**: Respond to the questions about your interests and preferences.
- **Get Recommendations**: Click the "احصل على التوصية" button to see your recommended career.

## Files

- **`app.py`**: The main script to run the Streamlit application.
- **`career_prediction_model.pkl`**: Pre-trained RandomForest model for career prediction.
- **`data.csv`**: Dataset used to train the model.
- **`README.md`**: This file.

## Dependencies

- pandas
- scikit-learn
- streamlit
- numpy
- pickle


## Acknowledgements

- Thanks to the contributors and resources used to build this project.

