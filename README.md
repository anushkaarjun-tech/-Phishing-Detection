# -Phishing-Detection
ABOUT THE PROJECT

Email based phishing is a common cyber-attack in which users are manipulated into providing sensitive information, or following malicious links / content.

This project presents a lightweight Hybrid Phishing Email Detection System that combines keyword-based risk analysis, TF-IDF (Term Frequency–Inverse Document Frequency), and Logistic Regression to determine suspicious emails.
The system analyses email text using a hybrid approach that combines keyword-based risk assessment with TF-IDF feature extraction and Logistic Regression to analyse email content and classify messages as phishing or legitimate.


KEY FEATURES

Keyword-Based Risk Analysis: Identifies commonly used phishing-related words and expressions.
TF-IDF Feature Extraction: Converts email text into numerical features for machine learning analysis.
Logistic Regression: Classifies emails as phishing or legitimate.
Risk Classification: Provides risk-based outputs such as High Risk, Suspicious, and Low Risk.
Lightweight Prototype: Designed as a simple and understandable phishing screening approach.


IMPLEMENTATIONS

- Language: Python
- Vectorizer: TF-IDF Vectorizer
- Model: Logistic Regression


METHODLOGY

Email Input: The user provides the email content for analysis.

Keyword-Based Risk Assessment: The system scans the email for predefined phishing-related keywords and calculates a risk score based on their presence.

Text Feature Extraction: TF-IDF converts email text into numerical data.

Machine Learning Classification: Logistic Regression analyses this data and classifies the email as phishing or legitimate.

Final Risk Assessment: The system combines the analysis to present a risk classification as High Risk/ Phishing email, Suspicious, or Low Risk/ Likely legitimate.


OBJECTIVE

The primary objective is to develop a lightweight phishing email screening prototype that combines rule-based keyword analysis with machine learning to help identify fraud emails and improve awareness of email-based cyber threats.


LIMITATIONS

- The prototype uses a small dataset of 10 sample emails.

- The keyword dictionary is limited and may not identify every phishing variation.

- The system focuses on email text rather than complete email metadata, headers, attachments, and sender authentication.

- No evaluation metrics( Accuracy, Precision, Recall, F1-score, or Confusion Matrix) is calculated in the current prototype.


FUTURE SCOPE

- Expand the dataset with more diverse email samples.

- Include URL, sender, header, and attachment analysis.

- Improve and regularly update the phishing keyword dictionary.

- Compare additional machine learning and NLP models.

- Extend the system to analyse suspicious URLs and QR-code content.


DISCLAIMER

This project is developed for educational and cybersecurity awareness purposes. It is a prototype and should not be considered a replacement for professional email security solutions.
