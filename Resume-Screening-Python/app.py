import nltk
import pickle 
import re 
import streamlit as st


nltk.download('punkt')
nltk.download('stopwords')


### Load models
clf=pickle.load(open('clf.pkl','rb'))

tfidf=pickle.load(open('tfidf.pkl','rb'))

### Web app 

def cleanresume(txt):
    cleantxt=re.sub('http\S+\s',' ',txt)
    cleantxt=re.sub('@\S+',' ',cleantxt)
    cleantxt=re.sub('#\S+',' ',cleantxt)
    cleantxt=re.sub('RT|cc',' ',cleantxt)
    cleantxt=re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""),' ',cleantxt)
    cleantxt=re.sub(r'[^\x00-\x7f]',' ',cleantxt)
    cleantxt=re.sub('\s+',' ',cleantxt)
    return cleantxt



def main():
    st.title("Resume Screening Application")
    upload_file = st.file_uploader('Upload Resume',type=['pdf','txt','docx'])
    if upload_file is not None:
        try:
            resume_bytes= upload_file.read()
            resume_text= resume_bytes.decode('utf-8')
        except:
            ## If the utf-8 decoading fail then try latin-1 decoding
            resume_text= resume_bytes.decode('latin-1')
        cleaned_resume=cleanresume(resume_text)
        input_feature=tfidf.transform([cleaned_resume])
        prediction_id=clf.predict(input_feature)[0]

        category_mapping={
            15:'Java Developer',
            23:'Testing',
            8:'DevOps Engineer',
            20:'Python Developer',
            24:'Web Designing',
            12:'HR',
            13:'Hadoop',
            3:'Blockchain',
            10:'ETL Developer',
            18:'Operations Manager',
            6:'Data Science',
            22:'Sales',
            16:'Mechanical Engineer',
            1:'Arts',
            7:'Database',
            11:'Electrical Engineering',
            14:'Health and fitness',
            19:'PMO',
            4:'Business Analyst',
            9:'DotNet Developer',
            2:'Automation Testing',
            17:'Network Security Engineer',
            21:'SAP Developer',
            5:'Civil Engineer',
            0:'Advocate',
            }
        category_name= category_mapping.get(prediction_id,'Unknown')
        st.write(f"Predicted Category According to your Resume is : {category_name} ")





## Python Main

if __name__=="__main__":
    main()


