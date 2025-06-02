import google.generativeai as genai

def analyze_depression(user_responses):
    prompt = f"""
    You are a clinical AI assistant assessing mental health with the PHQ-9 questionnaire.
    Analyze these raw user responses, assign PHQ-9 scores (0-3 per question), and determine depression severity.

    Responses:
    1. Little interest or pleasure in doing things? → {user_responses[0]}
    2. Feeling down, depressed, or hopeless? → {user_responses[1]}
    3. Trouble falling/staying asleep or sleeping too much? → {user_responses[2]}
    4. Feeling tired or having little energy? → {user_responses[3]}
    5. Poor appetite or overeating? → {user_responses[4]}
    6. Feeling bad about yourself or like a failure? → {user_responses[5]}
    7. Trouble concentrating? → {user_responses[6]}
    8. Moving/speaking slowly or feeling restless? → {user_responses[7]}
    9. Thoughts of self-harm? → {user_responses[8]}

    Provide:
    - PHQ-9 Score
    - Severity Level
    - Analysis
    - Recommendation
    """

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text
