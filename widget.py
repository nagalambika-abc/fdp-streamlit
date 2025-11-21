import streamlit as st

#Text Input
name=st.text_input('Enter student name')
st.write('Student name is ',name)
 
#Text Area
comments=st.text_area('Share your comments')
st.write('Comments: ',comments)
 
#Number Input
age=st.number_input('Enter voter age',min_value=18,max_value=100)
st.write('Voter Age is ',age)
 
#Date Input
dob=st.date_input('Enter your date of birth')
st.write('Date of Birth is ',dob)
 
#Time Input
appointment=st.time_input('Set appointment time')
st.write('Appointment time is ',appointment)

#button
if st.button('Add'):
    total=10+50+60
    st.write('Total Marks: ', total)

    #chedkbox
    checked=st.checkbox('Show Details')
    if checked:
        st.write('Result: Passed') 

#radio button   
gender=st.radio('Select Gender',['Male', 'Female', 'Other'])
st.write('Selected Gender',gender)

#select box
City=st.selectbox('Select City',['New York', 'Los Angeles', 'Chicago', 'Houston'])
st.write('Selected City: ',City)

#multi select box
hobbies=st.multiselect('Select Hobbies',['Reading', 'Traveling', 'Gaming', 'Cooking'])
st.write('Selected Hobbies: ',hobbies)
