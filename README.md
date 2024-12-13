# Customer-Feedback-Sentiment-Analysis

This Python-based tool analyzes customer feedback and categorizes it into Positive, Neutral, or Negative sentiments. The project leverages natural language processing (NLP) techniques to perform sentiment analysis on user reviews, feedback, or comments, helping businesses understand their customers' opinions. It supports different approaches to sentiment analysis, such as VADER and TextBlob, for quick integration and high accuracy.

## Features:
- Classify customer feedback into three categories: Positive, Neutral, and Negative.
- Visualize sentiment distribution using bar charts and pie charts.
- Optionally, deploy as a simple Flask web app for real-time sentiment analysis.

## How It Works
1. **Input Data**: The tool accepts customer feedback as text (reviews, comments, etc.).
2. **Preprocessing**: The feedback text is cleaned and preprocessed by:
   - Lowercasing
   - Tokenization
   - Removing stop words
   - Lemmatization
3. **Sentiment Analysis**: The feedback is analyzed using sentiment analysis libraries (VADER or TextBlob) to classify it into:
    - Positive
    - Neutral
    - Negative
4. **Visualization**: The sentiment distribution is visualized through bar or pie charts, giving a clear overview of feedback trends.
5. **Optional Web App**: A Flask web app is available to input feedback and get real-time sentiment analysis results.

## Requirements
To run this project, you’ll need:
- Python 3.7 or higher
- **Libraries**:
  - vaderSentiment
  - TextBlob
  - Flask (for the web app)
  - Matplotlib and Seaborn (for visualization)
  - Pandas
  - scikit-learn (optional for machine learning models)

## Setup Instructions
1. Clone the Repository and Navigate to the Project Directory
2. Set Up a Virtual Environment (Optional)
3. Install Dependencies
- All required dependencies are listed in the requirements.txt file. Install them using:
```bash
   pip install -r requirements.txt
   ```
4. Run the Script for Sentiment Analysis
   To perform sentiment analysis on feedback data:
```bash
   python src/sentiment_model.py
   ```
5. Launch the Web App (Optional)
   If you'd like to interact with the tool through a web interface:
```bash
   python src/app.py
   ```
Visit http://127.0.0.1:5000/ in your browser for real-time feedback analysis.(e.g. http://127.0.0.1:5000/analyze-feedback)
6. View Results
 - **Command-line output**: Displays categorized feedback as positive, neutral, or negative.
 - **Visualization**: Sentiment distribution charts are saved in the output directory or displayed in the app.