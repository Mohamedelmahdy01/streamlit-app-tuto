import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import pickle 

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
    result = []
    for i in list(pred):
        result.append(careers[i])
    return result

data = pd.read_csv('data.csv')

X = data.drop(['Courses'], axis=1) 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model1 = RandomForestClassifier()

model1.fit(X_train, y_train)

with open('career_prediction_model.pkl', 'wb') as file:
    pickle.dump(model1, file)

y_pred = model1.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(model1.n_features_in_)
