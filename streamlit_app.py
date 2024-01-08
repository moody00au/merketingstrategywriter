import streamlit as st
import openai

# Load secrets from the `.streamlit/secrets.toml` file
openai.api_key = st.secrets["openai_api_key"]

st.title("Social Media Marketing Strategy Generator")

# Collect company details
company_name = st.text_input("Company Name")
website_url = st.text_input("Website URL (if available)")
social_media_sites = st.text_area("List your social media profiles")

# Target audience and additional details
target_audience = st.text_input("Describe your target audience")
additional_info = st.text_area("Additional Information about your business")

# Competitor Analysis
competitors = st.text_area("List your main competitors (optional)")

# Historical Performance Data
historical_performance = st.text_area("Describe past marketing campaigns and their outcomes (optional)")

# Specific Marketing Goals
marketing_goals = st.text_area("Your marketing goals (e.g., increasing brand awareness, boosting sales)")

# Content Preferences
content_preferences = st.text_area("Preferred types and tone of content (e.g., videos, professional, humorous)")

# Budget Constraints
budget_info = st.text_area("Your marketing budget (optional)")

# Platform-Specific Strategies
platform_strategies = st.text_area("Preferred social media platforms and specific features to leverage (optional)")

# Seasonal/Cultural Considerations
seasonal_cultural_info = st.text_area("Any seasonal or cultural events to consider in your marketing (optional)")

# Feedback Loop
feedback_loop = st.text_area("Are you willing to provide ongoing feedback to refine marketing strategies? (optional)")

# Button to generate the marketing plan
generate_button = st.button("Generate Marketing Plan")

def generate_marketing_plan(data):
    prompt = f"""
    Create a comprehensive social media marketing plan for a company named {data['company_name']} with a website {data['website_url']}.
    Social media profiles: {data['social_media_sites']}.
    Target audience: {data['target_audience']}.
    Competitors: {data['competitors']}.
    Past marketing performance: {data['historical_performance']}.
    Marketing goals: {data['marketing_goals']}.
    Content preferences: {data['content_preferences']}.
    Budget: {data['budget_info']}.
    Platform strategies: {data['platform_strategies']}.
    Seasonal/cultural considerations: {data['seasonal_cultural_info']}.
    Feedback loop willingness: {data['feedback_loop']}.
    Additional info: {data['additional_info']}.
    """

    response = openai.migrate.create(
        model="gpt4",
        prompt=prompt,
        max_tokens=1000
    )
    return response.choices[0].text

if generate_button:
    data = {
        "company_name": company_name,
        "website_url": website_url,
        "social_media_sites": social_media_sites,
        "target_audience": target_audience,
        "additional_info": additional_info,
        "competitors": competitors,
        "historical_performance": historical_performance,
        "marketing_goals": marketing_goals,
        "content_preferences": content_preferences,
        "budget_info": budget_info,
        "platform_strategies": platform_strategies,
        "seasonal_cultural_info": seasonal_cultural_info,
        "feedback_loop": feedback_loop
    }
    plan = generate_marketing_plan(data)
    st.text_area("Your Marketing Plan", plan, height=400)
