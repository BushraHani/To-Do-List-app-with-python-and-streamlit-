import streamlit as st

#TO DO LIST APP WITH PYTHON STREAMLIT!

st.title("To Do List")
task = st.text_input("Enter Your Task","")

#button
if st.button("Add Task"):
    if task:
        st.session_state["task_list"].append(task)
        
if "task_list" not in st.session_state:
    st.session_state["task_list"] = []  
    
for i, t in enumerate(st.session_state["task_list"]):
    st.write(f"{i + 1}. {t}")
    
     
for i, t in enumerate(st.session_state["task_list"]): 
    if st.checkbox(f"{i + 1}.t"):
        st.session_state["task_list"].remove(t)       

