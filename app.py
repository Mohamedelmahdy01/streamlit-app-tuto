import streamlit as st
import numpy as np
import pickle

# Define the career function
def career(pred): 
    careers = [
       'Bachelor of Fine Arts (BFA) - بكالوريوس الفنون الجميلة',  # Related to drawing
       'Bachelor of Music (BMus) - بكالوريوس الموسيقى',  # Related to singing
       'Bachelor of Physical Education (BPEd) - بكالوريوس التربية البدنية',  # Related to sports
       'Bachelor of Game Design - بكالوريوس تصميم الألعاب',  # Related to video games
       'Bachelor of Performing Arts (BPA) - بكالوريوس الفنون المسرحية',  # Related to acting
       'Bachelor of Tourism and Travel Management (BTTM) - بكالوريوس إدارة السياحة والسفر',  # Related to traveling
       'Bachelor of Horticulture - بكالوريوس البستنة',  # Related to gardening
       'Bachelor of Veterinary Science (BVSc) - بكالوريوس العلوم البيطرية',  # Related to animals
       'Bachelor of Photography - بكالوريوس التصوير الفوتوغرافي',  # Related to photography
       'Bachelor of Education (BEd) - بكالوريوس التربية',  # Related to teaching
       'Bachelor of Computer Science (BSc) - بكالوريوس علوم الحاسب',  # Related to coding
       'Bachelor of Electrical Engineering (BEE) - بكالوريوس الهندسة الكهربائية',  # Related to electricity
       'Bachelor of Mechanical Engineering (BME) - بكالوريوس الهندسة الميكانيكية',  # Related to mechanic parts
       'Bachelor of Computer Engineering (BCE) - بكالوريوس هندسة الحاسبات',  # Related to computer parts
       'Bachelor of Science in Research (BSc) - بكالوريوس العلوم في البحث العلمي'  # Related to researching
    ]
    # Ensure the prediction index is within range
    if pred[0] >= len(careers) or pred[0] < 0:
        return ["Unknown Career"]
    return [careers[pred[0]]]

# Load the pre-trained model
with open('./career_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Main title of the website
st.title('اختيار التخصص الأنسب')

# Description
st.write("أجب عن الأسئلة التالية لتحديد التخصص أو الكلية الأنسب لك")

# Questions (You can modify the questions based on your project)
drawing = st.radio('هل تستمتع بالرسم؟', ('نعم', 'لا'))
singing = st.radio('هل تستمتع بالغناء؟', ('نعم', 'لا'))
sports = st.radio('هل تهتم بالرياضة؟', ('نعم', 'لا'))
video_games = st.radio('هل تستمتع بتطوير أو لعب ألعاب الفيديو؟', ('نعم', 'لا'))
acting = st.radio('هل تجد المتعة في التمثيل؟', ('نعم', 'لا'))
travelling = st.radio('هل تحب السفر؟', ('نعم', 'لا'))
gardening = st.radio('هل لديك اهتمام بالبستنة؟', ('نعم', 'لا'))
animals = st.radio('هل تهتم برعاية الحيوانات؟', ('نعم', 'لا'))
photography = st.radio('هل تستمتع بالتصوير الفوتوغرافي؟', ('نعم', 'لا'))
teaching = st.radio('هل تحب التعليم؟', ('نعم', 'لا'))
coding = st.radio('هل تستمتع بالبرمجة؟', ('نعم', 'لا'))
electricity = st.radio('هل تهتم بفهم مكونات الكهرباء؟', ('نعم', 'لا'))
mechanic_parts = st.radio('هل تستمتع بالعمل مع الأجزاء الميكانيكية؟', ('نعم', 'لا'))
computer_parts = st.radio('هل تحب التعامل مع أجزاء الكمبيوتر؟', ('نعم', 'لا'))
researching = st.radio('هل تستمتع بالبحث؟', ('نعم', 'لا'))

# Convert the answers to numeric values (1 for Yes, 0 for No)
answers = [
    1 if drawing == 'نعم' else 0,
    1 if singing == 'نعم' else 0,
    1 if sports == 'نعم' else 0,
    1 if video_games == 'نعم' else 0,
    1 if acting == 'نعم' else 0,
    1 if travelling == 'نعم' else 0,
    1 if gardening == 'نعم' else 0,
    1 if animals == 'نعم' else 0,
    1 if photography == 'نعم' else 0,
    1 if teaching == 'نعم' else 0,
    1 if coding == 'نعم' else 0,
    1 if electricity == 'نعم' else 0,
    1 if mechanic_parts == 'نعم' else 0,
    1 if computer_parts == 'نعم' else 0,
    1 if researching == 'نعم' else 0,
    0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0
]

# When the button is clicked
if st.button('احصل على التوصية'):
    # Convert the answers into a numpy array as the model expects it
    user_input = np.array(answers).reshape(1, -1)
    
    # Use the model to predict
    prediction = model.predict(user_input)
    
    # Get the career name from the prediction
    career_name = career(prediction)
    
    # Display the recommendation to the user
    st.write(f'التخصص الأنسب لك هو: {career_name[0]}')
