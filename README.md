
# MindGlow

MindGlow is an interactive web application built with Streamlit and powered by the Google Gemini API to assess mental health using the PHQ-9 questionnaire. It analyzes raw user inputs to deliver depression severity scores, personalized insights, and recommendations in a sleek, dark-themed UI.





## API Reference

MindGlow uses the **Google Gemini API** to analyze user responses and generate PHQ-9 scores, severity levels, and recommendations. Below is the key API integration detail:

- **API**: Google Gemini API (via `google-generativeai` Python package)
- **Model**: `gemini-pro`
- **Usage**: Processes 9 raw text inputs from PHQ-9 questions, applying custom prompts to compute scores (0-3 per question) and deliver structured output (score, severity, analysis, recommendation).
- **Authentication**: Requires a Gemini API key, stored securely in a `.env` file as `GEMINI_API_KEY`.
- **Documentation**: [Google AI Studio Documentation](https://ai.google.dev/docs)

For setup, install the package:
```bash```
``` pip install google-generativeai ```


