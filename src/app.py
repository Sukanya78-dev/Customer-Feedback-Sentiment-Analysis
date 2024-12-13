from Tools.scripts.make_ctype import method
from flask import Flask, request, jsonify
import pandas as pd

from src.sentiment_model import analyze_sentiment

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Customer Feedback Sentiment Analysis Service is running"}), 200


@app.route("/analyze-feedback", methods=["GET", "POST"])
def analyze_feedback():
    """
    Reads feedback from a provided CSV file or user input,
    analyzes sentiment using `analyze_sentiment()`.
    """
    try:
        if request.method == "POST":
            uploaded_file = request.files.get("file")
            if uploaded_file:
                feedback_df = pd.read_csv(uploaded_file)
            else:
                return jsonify({"error": "no file uploaded"}), 400
                    #print(feedbacks)
                    #for index, row in feedbacks.iterrows():
                        #feedback_text = row['feedback']
                        #feedback_result = analyze_sentiment(feedback_text)
                        #print("Customer Feedback Sentiment Analysis Result " + feedback_result)
        else:
            file_path = "../data/feedback.csv"
            feedback_df = pd.read_csv(file_path)

        if "feedback" not in feedback_df.columns:
            return jsonify({"error": "The uploaded CSV does not have a 'feedback' column"}), 400

        feedback_df["sentiment"] = feedback_df["feedback"].apply(analyze_sentiment)
        return jsonify(feedback_df.to_dict(orient="records")), 200

    except FileNotFoundError:
        return jsonify({"error": "The feedback.csv file could not be found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("""
    ======================================================
    Flask Sentiment Analysis Web App
    ------------------------------------------------------
    Launch the app by running:
       python src/app.py
    Visit: http://127.0.0.1:5000/ in your browser
    ------------------------------------------------------
    """)
    app.run(debug=True, port=5000)
