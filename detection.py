# ============================================================
#            AI PHISHING EMAIL DETECTOR
# ============================================================

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


print("==================================================")
print("      PHISHING EMAIL DETECTOR                  ")
print("==================================================")
print("Welcome! This tool checks if an email is suspicious.")
print("It scans the text for common phishing keywords.")
print("==================================================\n")



# ============================================================
# PART 1: TRAINING DATA
# ============================================================

emails = [
    # Phishing emails
    "URGENT! Verify your bank account immediately because it has been suspended.",
    "Your password has expired. Login now to restore access to your account.",
    "Congratulations! You have won a cash prize. Click here to claim your reward.",
    "URGENT! Click here to verify your bank details and claim your reward.",
    "Your account is suspended. Update now and verify your password to avoid losing access.",

    # Legitimate Emails
    "Hello, can we meet tomorrow at 10 AM to discuss the project?",
    "Please find the assignment attached. Submit it by Monday.",
    "Your class starts at 9 AM tomorrow. Please arrive on time.",
    "Thank you for your email. I will review the document and reply soon.",
    "The meeting has been moved to Monday. Please check the updated schedule."
]

# 1 = Phishing
# 0 = Legitimate
labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]


# ============================================================
# PART 2: TRAINING THE AI/ML MODEL
# ============================================================

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(emails)

model = LogisticRegression()

model.fit(X, labels)


# ============================================================
# PART 3: KEYWORD SYSTEM 
# ============================================================

keywords = [
    "urgent",
    "verify",
    "password",
    "click here",
    "login",
    "suspended",
    "update now",
    "bank",
    "reward",
    "prize"
]


# ============================================================
# PART 4: INPUT EMAIL FROM USER
# ============================================================

while True:

    email_text = input("\nEnter email message: ")

    email_lower = email_text.lower()


    # ========================================================
    # PART 5: ORIGINAL KEYWORD ANALYSIS
    # ========================================================

    detected_words = []

    for word in keywords:

        if word in email_lower:
            detected_words.append(word)

    risk_score = len(detected_words)


    # ========================================================
    # PART 6: AI/ML PREDICTION
    # ========================================================

    new_email = vectorizer.transform([email_text])

    prediction = model.predict(new_email)[0]

    probability = model.predict_proba(new_email)[0]

    confidence = max(probability) * 100



    # ========================================================
    # PART 7: DISPLAY KEYWORD RESULTS
    # ========================================================

    print("\n----------------------------------------")
    print("        EMAIL SECURITY ANALYSIS")
    print("----------------------------------------")

    print("\nDetected warning signs:")

    if len(detected_words) == 0:

        print("* None")

    else:

        for word in detected_words:
            print("*", word)


    print("\nKeyword Risk Score:", risk_score)




    # ========================================================
    # PART 8: AI RESULT
    # ========================================================

    print("\nAI/ML Prediction:")

    if prediction == 1:

        print("⚠️ PHISHING EMAIL")

    else:

        print("✅ LEGITIMATE EMAIL")


    print(f"AI Confidence: {confidence:.2f}%")


    # ========================================================
    # PART 9: FINAL COMBINED RESULT
    # ========================================================

    print("\n----------------------------------------")
    print("             FINAL RESULT")
    print("----------------------------------------")

    if prediction == 1 or risk_score >= 3:

        print("⚠️ HIGH RISK / PHISHING EMAIL")

    elif risk_score >= 1:

        print("🟠 SUSPICIOUS EMAIL")

    else:

        print("🟢 LOW RISK / LIKELY LEGITIMATE")


    # ========================================================
    # PART 10: TEST ANOTHER EMAIL
    # ========================================================

    choice = input("\nDo you want to check another email? (y/n): ").lower()

    if choice == "n":

        print("\nThank you for using the AI Phishing Email Detector!")

        break

    elif choice != "y":

        print("Invalid input. Please enter y or n.")