from transformers import pipeline
import streamlit as st

if 'all_comments' not in st.session_state:
    st.session_state['all_comments'] = []

classifier = pipeline("text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

st.markdown('<p class="title">Comment Analyser</p>', unsafe_allow_html=True)
st.video("https://www.youtube.com/watch?v=zRUliXuwJCQ&list=PLZoTAELRMXVMhVyr3Ri9IQ-t5QPBtxzJO") # Enter any video url of your choice
username = st.text_input("Enter your username", value="Alex123")
comment = st.text_input("Enter your comment", value="Amazing Video")

# Add select box for sorting
sort_option = st.selectbox("Sort Comments by Sentiment:", [ "None","Positive", "Negative"])

def display_comments(comments):

    for idx, comment in enumerate(comments):
        # Determine background color based on sentiment
        if comment['classification'] == 'POSITIVE':
            background_color = '#23DE15'  # Green
        elif comment['classification'] == 'NEGATIVE':
            background_color = '#FF4B4B'  # Red
        else:
            background_color = '#FFFFFF'  # Default white
 
        # HTML template for comment display
        comment_html = f"""
        <div style="margin: 10px; padding: 10px; border-radius: 10px; box-shadow: 0px 2px 5px 0px rgba(0, 0, 0, 0.1); background-color: {background_color};">
            <div style="font-weight: bold; margin-bottom: 5px;">{comment['username']}</div>
            <div style="font-size: 16px; line-height: 1.5;">{comment['comment']}</div>
        </div>
        """
        # Display comment using st.write with unsafe_allow_html=True
        st.write(comment_html, unsafe_allow_html=True)

def classify_comment(classifier, comment):

    result = classifier(comment)[0]['label']
    return result

st.markdown(
    """
    <style>
        /* Style for title */
        .title {
            text-align: center !important;
            padding-bottom: 20px;
            color: white;
            font-size: 60px;
            font-weight: bold;
        }

        /* Style for video */
        .video-wrapper {
            text-align: center;
            padding: 20px 0;
        }

        /* Style for input and select box */
        .input-wrapper {
            margin-bottom: 20px;
        }

        /* Style for comments */
        .comment-wrapper {
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


if st.button("Add Comment"):
    comment_dic = {'username': username,'comment': comment, 'classification': classify_comment(classifier, comment)}
    st.session_state['all_comments'].append(comment_dic)

# Filter comments based on selected option
filtered_comments = st.session_state['all_comments']
if sort_option == "Positive":
    filtered_comments = [c for c in filtered_comments if c['classification'] == 'POSITIVE']
elif sort_option == "Negative":
    filtered_comments = [c for c in filtered_comments if c['classification'] == 'NEGATIVE']
 
display_comments(filtered_comments)
