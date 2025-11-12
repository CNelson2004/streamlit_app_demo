import streamlit as st

def main():
    st.title("Hello, Streamlit!")

    # ~~ is used for strikethrough
    st.markdown("""
    This is a ~~fun~~ demo for **STAT** *386* ***!***
    """)

    #This creates a slider, the bounds are 0 and 10 inclusive with a default number of 7. 
    #It moves only by integers, if you add a fourth number, that will set the 'step' I think
    fav_num = st.slider("Pick your favorite number:",0,10,7,)

    #Creates a button and sets what will happens when it is clicked
    if st.button("Click me!"):
        #Creates a text box below the button when it is clicked
        st.info(f"Your favorite number is: {fav_num}!")



if __name__ == "__main__":
    main()
    #start this in your terminal using: uv run streamlit run app.py