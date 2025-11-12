import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    st.title("Hello, Streamlit!")

    # ~~ is used for strikethrough
    st.markdown("""
    This is a ~~fun~~ demo for **STAT** *386* ***!***
    """)

    st.write("Here, I am checking out how to make a slider and button")
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
    st.write("Here’s a small sample barplot from matplotlib:")
    st.pyplot(fig)


    # Create a simple DataFrame
    data = {
        'Category': ['A', 'B', 'C', 'D'],
        'Value': [10, 24, 36, 18],
        'Growth (%)': [5.2, 3.8, 4.5, 2.9]
    }
    df = pd.DataFrame(data)

    # Display the DataFrame
    st.write("Here’s a small sample dataset:")
    st.dataframe(df)

    # Create some example data
    x = np.arange(0, 10, 1)
    y = x ** 2  # y = x²
    data = pd.DataFrame({'x': x, 'y': y})

    # Display the line chart
    st.write("Here’s a small sample line chart, using only streamlit:")
    st.line_chart(data.set_index('x'))


if __name__ == "__main__":
    main()
    #start this in your terminal using: uv run streamlit run app.py