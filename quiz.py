#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 17:05:06 2024

@author: me
"""

import streamlit as st
import json
# import matplotlib.pyplot as plt

# questions_load = [
#     {
#         "question": "What is your body type ?",
#         "choices": [
#             {"answer": "Too Tall / Too Short", "kalpa_points": 3, "vatta_points": 1, "pitta_points": 2},
#             {"answer": "Medium", "kalpa_points": 1, "vatta_points": 3, "pitta_points": 2},
#             {"answer": "Short", "kalpa_points": 2, "vatta_points": 1, "pitta_points": 3}
#         ]
#     },
#     {
#         "question": "What is your body-weight type ? ",
#         "choices": [
#             {"answer": "Lean", "kalpa_points": 2, "vatta_points": 3, "pitta_points": 1},
#             {"answer": "Average", "kalpa_points": 3, "vatta_points": 2, "pitta_points": 1},
#             {"answer": "Heavy", "kalpa_points": 1, "vatta_points": 2, "pitta_points": 3}
#         ]
#     },
#     {
#         "question": "What is your Skin-type ? ",
#         "choices": [
#             {"answer": "Rough, easily skin gets dark", "kalpa_points": 2, "vatta_points": 3, "pitta_points": 1},
#             {"answer": "Smooth, Achne/Pimple", "kalpa_points": 3, "vatta_points": 2, "pitta_points": 1},
#             {"answer": "Bright, Smooth, Attractive", "kalpa_points": 1, "vatta_points": 2, "pitta_points": 3}
#         ]
#     },
#     {
#         "question": "What type of eye you have ? ",
#         "choices": [
#             {"answer": "Sunken, small eyelashes", "kalpa_points": 2, "vatta_points": 3, "pitta_points": 1},
#             {"answer": "Sharp, penetrating eyes ", "kalpa_points": 3, "vatta_points": 2, "pitta_points": 1},
#             {"answer": "Big, thick eyelashes", "kalpa_points": 1, "vatta_points": 2, "pitta_points": 3}
#         ]
#     },
#     {
#         "question": "What type of hair you have ? ",
#         "choices": [
#             {"answer": "Dry, Small, Curly", "kalpa_points": 2, "vatta_points": 3, "pitta_points": 1},
#             {"answer": "Thin, Silky, Oily", "kalpa_points": 3, "vatta_points": 2, "pitta_points": 1},
#             {"answer": "Thick, soft, dark, wavy", "kalpa_points": 1, "vatta_points": 2, "pitta_points": 3}
#         ]
#     },
#     {
#         "question": "What type of forehead you have ? ",
#         "choices": [
#             {"answer": "Small, Irregular", "kalpa_points": 2, "vatta_points": 3, "pitta_points": 1},
#             {"answer": "Medium", "kalpa_points": 3, "vatta_points": 2, "pitta_points": 1},
#             {"answer": "Large, Attractive", "kalpa_points": 1, "vatta_points": 2, "pitta_points": 3}
#         ]
#     },
#     {
#         "question": "How is your digestion going on? ",
#         "choices": [
#             {"answer": "Irregular", "kalpa_points": 2, "vatta_points": 3, "pitta_points": 1},
#             {"answer": "Very Well", "kalpa_points": 3, "vatta_points": 2, "pitta_points": 1},
#             {"answer": "Weak", "kalpa_points": 1, "vatta_points": 2, "pitta_points": 3}
#         ]
#     },
#     {
#         "question": "How often you get thirty ? ",
#         "choices": [
#             {"answer": "Sometimes", "kalpa_points": 2, "vatta_points": 3, "pitta_points": 1},
#             {"answer": "Very Often", "kalpa_points": 3, "vatta_points": 2, "pitta_points": 1},
#             {"answer": "Very Rarely", "kalpa_points": 1, "vatta_points": 2, "pitta_points": 3}
#         ]
#     },
#     {
#         "question": "What is your preferred food taste?",
#         "choices": [
#             {"answer": "Sweet, Sour, Salty", "kalpa_points": 2, "vatta_points": 3, "pitta_points": 1},
#             {"answer": "Sweet, bitter, slightly bitter", "kalpa_points": 3, "vatta_points": 2, "pitta_points": 1},
#             {"answer": "Bitter, Slight bitter, Strong Taste", "kalpa_points": 1, "vatta_points": 2, "pitta_points": 3}
#         ]
#     },
#     {
#         "question": "How much is your control on hunger? ",
#         "choices": [
#             {"answer": "Irregular", "kalpa_points": 2, "vatta_points": 3, "pitta_points": 1},
#             {"answer": "Poor", "kalpa_points": 3, "vatta_points": 2, "pitta_points": 1},
#             {"answer": "Very Good", "kalpa_points": 1, "vatta_points": 2, "pitta_points": 3}
#         ]
#     },
#     {
#         "question": "How much is your food consumption? ",
#         "choices": [
#             {"answer": "Irregular", "kalpa_points": 2, "vatta_points": 3, "pitta_points": 1},
#             {"answer": "Heavy", "kalpa_points": 3, "vatta_points": 2, "pitta_points": 1},
#             {"answer": "Normal", "kalpa_points": 1, "vatta_points": 2, "pitta_points": 3}
#         ]
#     },
#     {
#         "question": "What are your bowel movements ? ",
#         "choices": [
#             {"answer": "Irregular, Diarrhea, Constipation", "kalpa_points": 2, "vatta_points": 3, "pitta_points": 1},
#             {"answer": "Diarrhea", "kalpa_points": 3, "vatta_points": 2, "pitta_points": 1},
#             {"answer": "Constipation", "kalpa_points": 1, "vatta_points": 2, "pitta_points": 3}
#         ]
#     }
# ]


# Function to load questions from a JSON file
def load_questions(file_path):
    with open(file_path, 'r') as f:
        questions = json.load(f)
        # questions = questions_load
    return questions

# Initialize session state variables
def initialize_session_state(questions):
    session_state = st.session_state
    session_state.question_index = 0
    session_state.kalpa = 0
    session_state.vatta = 0
    session_state.pitta = 0
    session_state.questions = questions

def reset_quiz():
    questions = load_questions('questions.json')
    initialize_session_state(questions)

def Quiz():
    st.title('Know your Prakriti ?')

    st.markdown("""---""")
    
    # Load questions from JSON file
    questions = load_questions('questions.json')
    
    if 'question_index' not in st.session_state:
        initialize_session_state(questions)

    if not st.session_state.questions:
        st.session_state.questions = questions

    current_question = st.session_state.questions[st.session_state.question_index]
   
    st.markdown(f"### Question {st.session_state.question_index + 1}: {current_question['question']}")
    

    form = st.form(key=f"quiz_form_{st.session_state.question_index}")
    # Quest = f"Question {st.session_state.question_index + 1} : {current_question['question']}" 


    user_choice = form.radio("Choose any one answer", [choice['answer'] for choice in current_question['choices']])
    if st.session_state.question_index >= 12 - 1:
        text = "Submit"
    else:
        text = "Next"
    
    submitted = form.form_submit_button(text)
    
    if submitted:
        if user_choice is not None:
            selected_option = next(choice for choice in current_question['choices'] if choice['answer'] == user_choice)
            st.session_state.kalpa += selected_option['kalpa_points']
            st.session_state.vatta += selected_option['vatta_points']
            st.session_state.pitta += selected_option['pitta_points']

            SerialNo = st.session_state.question_index
            # st.text(f"{st.session_state.kalpa} : {st.session_state.vatta} : {st.session_state.pitta}")
            # Exception Adding
            # if selected_option['vatta_points'] and SerialNo == '7':
            #     st.session_state.kalpa += 0.5
            # if selected_option['kalpa_points'] and SerialNo == '7':
            #     st.session_state.vatta += 0.5
            # if selected_option['pitta_points'] and SerialNo == '10':
            #     st.session_state.kalpa += 0.5
            #     st.session_state.vatta += 0.5
            # if selected_option['vatta_points'] and SerialNo == '10':
            #     st.session_state.pitta += 0.5
            # if selected_option['pitta_points'] and SerialNo == '11':
            #     st.session_state.vatta += 0.5
            # if selected_option['kalpa_points'] and SerialNo == '11':
            #     st.session_state.vatta += 0.5
            
            
            if st.session_state.question_index < 12 - 1:
                st.session_state.question_index += 1
                st.experimental_rerun()
            else:
                total_points = st.session_state.kalpa + st.session_state.vatta + st.session_state.pitta
                kalpa_percent = (st.session_state.kalpa / total_points) * 100
                vatta_percent = (st.session_state.vatta / total_points) * 100
                pitta_percent = (st.session_state.pitta / total_points) * 100
                # form.form_submit_button("Rerun")
                st.write("Results:")
                st.write(f"Kalpa: {kalpa_percent:.2f}%")
                st.write(f"Vatta: {vatta_percent:.2f}%")
                st.write(f"Pitta: {pitta_percent:.2f}%")

                st.markdown("""
                ### Vata
                Vata is composed of air and space elements and is responsible for all movement in the body and mind. When balanced, Vata promotes creativity, flexibility, and mental clarity.

                ### Pitta
                Pitta is made up of fire and water elements and governs metabolism, digestion, and energy production. Balanced Pitta fosters strong intellect, sharp focus, and a healthy appetite.

                ### Kapha
                Kapha consists of earth and water elements and provides structure, stability, and lubrication to the body. When balanced, Kapha brings strength, endurance, and a calm, steady nature.
                """)

        else:
            st.warning("Please select an answer before submitting.")

    if st.button("Reset Quiz"):
        reset_quiz()
        st.experimental_rerun()


# if __name__ == '__main__':
#     main()
