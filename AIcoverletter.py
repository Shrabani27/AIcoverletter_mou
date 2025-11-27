import google.Generativeai as genai
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("AI Cover Letter Generator")
job_title = st.text_input("Enter Job Title")
resume = st.text_area("Paste your resume summary here")

if st.button("Generate cover letter"):
    prompt = f"""
    write a professional cover letter for the job title "{job_title}".
    use this resume summary:
    {resume}
    """

response = model.generate_content(prompt)
print(response.text)
