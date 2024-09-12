import streamlit as st
import numpy as np
import pickle

# Define the career function
def career(pred): 
    careers = [
       'BBA- Bachelor of Business Administration',
       'BEM- Bachelor of Event Management',
       'Integrated Law Course- BA + LL.B',
       'BJMC- Bachelor of Journalism and Mass Communication',
       'BFD- Bachelor of Fashion Designing',
       'BBS- Bachelor of Business Studies',
       'BTTM- Bachelor of Travel and Tourism Management',
       'BVA- Bachelor of Visual Arts', 'BA in History',
       'B.Arch- Bachelor of Architecture',
       'BCA- Bachelor of Computer Applications',
       'B.Sc.- Information Technology', 'B.Sc- Nursing',
       'BPharma- Bachelor of Pharmacy', 'BDS- Bachelor of Dental Surgery',
       'Animation, Graphics and Multimedia', 'B.Sc- Applied Geology',
       'B.Sc.- Physics', 'B.Sc. Chemistry', 'B.Sc. Mathematics',
       'B.Tech.-Civil Engineering',
       'B.Tech.-Computer Science and Engineering',
       'B.Tech.-Electronics and Communication Engineering',
       'B.Tech.-Electrical and Electronics Engineering',
       'B.Tech.-Mechanical Engineering', 'B.Com- Bachelor of Commerce',
       'BA in Economics', 'CA- Chartered Accountancy',
       'CS- Company Secretary', 'Diploma in Dramatic Arts', 'MBBS',
       'Civil Services', 'BA in English', 'BA in Hindi', 'B.Ed.'
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
    0, 0, 0, 0 
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
