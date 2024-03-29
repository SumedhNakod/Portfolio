import streamlit as st
from PIL import Image
import pandas as pd
import json
from pathlib import Path

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
#css_file = "/content/main.css"
resume_file = current_dir / "SumedhNakod.pdf"
profile_pic_file = current_dir / "profile-pic1.png"

PAGE_TITLE = "Digital cv | Sumedh Nakod"
PAGE_ICON = ":wave:"
NAME = "Sumedh Nakod"
DESCRIPTION = """
Junior Data Scientist assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "sumedhnakodx@gmail.com"
Phone_number = "+44-7768042825"
SOCIAL_MEDIA = {
"LinkedIn": "https://www.linkedin.com/in/sumedh-nakod-15a838150/",
"GitHub": "https://github.com/SumedhNakod?tab=repositories",
}

PROJECTS = {
"🏆 IT Spend Dashboard -  Analysing IT Spend for a company from 2001 to 2012": {
  'link' : "https://github.com/SumedhNakod/Projects/blob/master/PowerBI%20Projects/IT%20Spend%20Analytics/IT_SPEND_ANALYSIS.pdf",
  'description' : "The IT spend analysis PowerBI dashboard project for the years 2001-2012 utilized interactive visualizations, drill-down functionality, dynamic filters, data consolidation, advanced calculations, conditional formatting, cross-filtering & export functionality. The dashboard provided an overview of the total IT spending for each year, as well as a breakdown of expenditures across different categories, such as hardware, software, infrastructure, services, and personnel."
},
"🏆 Comment Toxicity Detector using Keras and LSTM with Gradio App (NLP)": {
  'link' : "https://github.com/SumedhNakod/Projects/blob/master/Toxicity_Detector.ipynb",
  'description' : "Completed the project using TensorFlow, Keras, and LSTM to develop a comment toxicity classification model. The model accurately categorizes comments into toxicity levels. I performed data preprocessing, including tokenization and sequence padding. The LSTM model was trained on a labeled dataset of comments. I evaluated the model's performance and optimized parameters. I created a Gradio app in Python for real-time toxicity predictions. The project focused on efficiency and user-friendliness."
},
"🏆 Uber Data Analysis using R and ggplot": {
  'link' : "https://github.com/SumedhNakod/Projects/blob/master/Uber.R",
  'description' : "I analyzed Uber data using R and ggplot. Preprocessing involved cleaning and formatting the dataset. I explored patterns and correlations, identifying insights on ride frequency, peak hours, and popular routes. Utilizing ggplot, I created visually appealing plots such as line charts and bar graphs to represent findings. The project prioritized efficient analysis and clear visualizations for easy understanding."
},
"🏆 Twitter Sentiment Analysis for Stock prices (NLP)" : {
  'link' : "dummy",
  'description' : "BERT and Twitter data are utilized for predicting stock market trends. By leveraging NLP, BERT extracts features from tweets, which are preprocessed and fine-tuned on labeled data. The sentiment of new tweets is classified to analyze and predict future stock movements. Twitter sentiment serves as an input for traders and investors to gain insights. However, it is recommended to consider other analysis techniques alongside Twitter sentiment for comprehensive decision-making."
},
"🏆 Image Caption Generator using Neural Networks" : {
  'link' : "https://github.com/SumedhNakod/Projects/blob/master/training_caption_generator.ipynb",
  'description' : "The model utilized LSTM (Long Short-Term Memory) for text generation and CNN (Convolutional Neural Network) for image feature extraction. I preprocessed the images and extracted features using CNN. The LSTM model was trained on these features to generate captions for the images. The project aimed to accurately describe the content of images with textual captions. The LSTM and CNN architectures were implemented efficiently to achieve high-quality image captioning."
},
}

def V_SPACE(lines):
  for _ in range(lines):
    st.write('&nbsp;')


st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)


with open(resume_file,"rb") as pdf_file:
  PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_file)# Set the padding value in pixels
padding_px = 20

# Create HTML code with padding
padding_html = f'<div style="padding-top: {padding_px}px;"></div>'

#Hero section
col1,col2 = st.columns(2,gap = "small")
with col1:
  st.markdown(padding_html, unsafe_allow_html=True)
  st.image(profile_pic, width =300,output_format='PNG')

with col2:
  st.title(NAME)
  st.write(DESCRIPTION)
  st.download_button(
    label = " 📄 Download Resume",
    data = PDFbyte,
    file_name = resume_file.name,
    mime = "application/octet-stream",
  )
  st.write("📧", EMAIL)
  st.write("📞", Phone_number)

#Social Links
#st.write("#")
V_SPACE(1)
cols = st.columns(len(SOCIAL_MEDIA))
for index,(platform,link) in enumerate(SOCIAL_MEDIA.items()):
  cols[index].write(f"[{platform}]({link})")


#Experience and Qualifications
#st.write("#")
V_SPACE(1)
st.subheader("Professional Experience 💻")
st.write("---")
st.markdown('<h5><u>'+'Blackcoffer (Data Science Intern) - Delhi' + '</h5>' , unsafe_allow_html=True)
st.write("Nov 2021 - Apr 2022")
#st.write("#")
st.write(
    """
    Blackcoffer is an enterprise software and analytics consulting firm based in India and European Union (Malta). It is a Data-driven technology and decision science firm focused exclusively on Big Data & Analytics (Intern for 7 months).
    - ✔️Outperformed peers by leading 20% more global client engagements, delivering strategic insights, and crafting customized solutions.
    - ✔️Researched, assessed emerging technologies and algorithms, offering strategic guidance and driving continuous enhancements for an Australian client's project. Seamlessly handling a daily influx of around 1 million records, ensuring secure storage for cryptocurrency data from various sources in a robust data pipeline on Google Cloud Platform (GCP).
    - ✔️Showcased deep business acumen and generated impactful insights through advanced visualization using PowerBI and Tableau for a government-based project in Nigeria. Proposed system enhancements that have since optimized future data flow, contributing to 70% improved efficiency.
    - ✔️Achieved consistent success by meticulously maintaining, debugging, and enhancing the precision of both new and existing machine learning projects, impressing various clients who subsequently extended involvement for subsequent projects.
    - ✔️Successfully led 4 whole projects throughout its life cycle. 
    """
  )

#st.write("#")
V_SPACE(1)
st.markdown('<h5><u>'+'XLNC Technologies (Business Analytics Intern) - Mumbai' + '</h5>' , unsafe_allow_html=True)
st.write("May 2019 - June 2019")
#st.write("#")
st.write(
    """
    XLNC Technologies is an emerging firm providing specialized services pertaining to Robotic Process Automation (Automation Anywhere), Machine Learning, and Artificial intelligence.
    - ✔️Proactively led meetings with key businesses to gather vital insights on business processes and user requirements. Daily responsibilities encompassed creating meta documents, offering valuable insights, and collaborating closely with developers.
    - ✔️Successfully accomplished Robotic Process Automation (RPA) training, securing a prestigious certification in Automation Anywhere.
    """
  )

# Projects
# Skills
# Education
#st.write("#")
V_SPACE(1)
st.subheader("Education 🎓")
st.write("---")
df = {
  "Degree" : ['MSc','Btech'],
  "Course" : ['Data Science and Statistics','Computer Science'],
  "Date" : ['2022-2023','2016-2020'],
  "University" : ['University of Exeter','Mukesh Patel School of Technology Management & Engineering'],
  "Score" : [4.0,2.97],
  "Modules" : ['Working with Data, Statistical Data Modelling, Advanced Statistics,Application of Data Science,DS in Time and Space',
  'Data Structures, Database Management Systems, Artificial Intelligence, Numerical Methods, Predictive Modelling, Design and Analysis of Algorithms, Software Engineering']
  }

df = pd.DataFrame(df)
# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)
st.table(df)

#Skills
info = {'skills':['Data Science','SQL','Postgres','MongoDB','Python','Java','C++','Airflow','PowerBI','Asana', 'Loom', 'Clockify', 'Notion']}
skill_col_size = 5
#st.write("#")
V_SPACE(1)
st.subheader('Skills & Tools ⚒️')
st.write("---")
def skill_tab():
    rows,cols = len(info['skills'])//skill_col_size,skill_col_size
    skills = iter(info['skills'])
    if len(info['skills'])%skill_col_size!=0:
        rows+=1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break
with st.spinner(text="Loading section..."):
    skill_tab()

# --- Projects & Accomplishments ---
#st.write("#")
V_SPACE(1)

st.subheader("Projects & Accomplishments 👷🏻")
st.write("---")

for project_name, project_details in PROJECTS.items():
  st.write(f"[{project_name}]({project_details['link']})")
  with st.expander('Detailed Description'):
    st.write(project_details['description'])






