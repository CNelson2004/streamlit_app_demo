import streamlit as st
import matplotlib.pyplot as plt

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

    #doing pyplot
    # Sample data
    categories = ['A', 'B', 'C', 'D']
    values = [10, 24, 36, 18]

    # Create the plot
    fig, ax = plt.subplots()
    ax.bar(categories, values, color='skyblue')
    ax.set_xlabel('Category')
    ax.set_ylabel('Value')
    ax.set_title('Simple Bar Plot Example')

    # Display it in Streamlit
    st.pyplot(fig)


if __name__ == "__main__":
    main()
    #start this in your terminal using: uv run streamlit run app.py