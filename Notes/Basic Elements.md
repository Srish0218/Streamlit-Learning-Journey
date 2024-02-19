# Notes

## Streamlit Web App Code
- Import Streamlit and Pandas libraries.
- Use `st.title()`, `st.subheader()`, `st.header()`, `st.text()`, and `st.markdown()` to display various text elements.
- Customize text formatting using Markdown syntax.
- Utilize `st.latex()` for LaTeX equations.
- Display JSON data using `st.json()`.
- Present code snippets with syntax highlighting using `st.code()`.

## Visual Elements
- Embed an image with `st.image()` and provide a caption.
- Add audio and video files using `st.audio()` and `st.video()`.
- Display tables with Pandas DataFrame using `st.table()` and `st.dataframe()`.

## User Interaction
- Create a checkbox with `st.checkbox()` and handle its state change.
- Use `st.radio()` to present radio button options.
- Implement buttons with `st.button()` and handle button clicks.
- Utilize `st.selectbox()` and `st.multiselect()` for dropdown selection.

## Styling
- Apply custom CSS styling to hide specific elements.
- Use Streamlit's built-in color syntax for text styling.

# Questions

1. **How can custom CSS styling be applied to hide specific elements in a Streamlit app?**
- *Custom CSS styling can be applied using the st.markdown() function with the unsafe_allow_html=True parameter. HTML-style CSS can be embedded within the markdown string to achieve styling effects.*

2. **What is the purpose of `st.latex()` in the provided code, and how does it enhance the app?**
- *st.latex() is used to render LaTeX equations within the Streamlit app. It enhances the app by allowing the inclusion of mathematical notations and expressions in a visually appealing way.*

3. **Explain the difference between `st.table()` and `st.dataframe()` when displaying Pandas DataFrames.**
- *Both functions are used to display Pandas DataFrames, but st.table() provides a simple static table, while st.dataframe() allows for more interactive exploration of the DataFrame, such as sorting and filtering.*

4. **How can user interaction be implemented with checkboxes, and what is the role of the `on_change` parameter?**
- *User interaction with checkboxes is achieved using st.checkbox(). The on_change parameter allows specifying a callback function that will be triggered when the checkbox state changes.*

5. **Demonstrate how to embed an image with a caption using `st.image()`.**
- *The code snippet st.image('download.jpg', caption="Pycharm-Logo", width=100) demonstrates embedding an image named 'download.jpg' with a caption and setting the width to 100 pixels.*

6. **Describe the significance of using `st.button()` with the `on_click` parameter in the context of the provided code.**
- *st.button() is used to create a button, and the on_click parameter specifies a callback function that will be executed when the button is clicked. In the provided code, the btn_click function is called when the button is clicked.*

7. **What is the purpose of the `st.session_state` object, and how is it used in the provided code?**
- *The st.session_state object is used to store and access session-specific state variables. In the provided code, it is referenced as st.session_state.checker to check the state of a checkbox*

8. **How is radio button functionality achieved in Streamlit using `st.radio()`?**
- *st.radio() is used to create a radio button. It takes options as input, and the user can select a single option. In the provided code, the selected radio button value is stored in the variable radio_btn*

9. **Explain the role of `st.selectbox()` and `st.multiselect()` in providing user choices.**
- *st.selectbox() creates a dropdown with single-choice selection, while st.multiselect() creates a dropdown with multiple-choice selection. Both functions provide a list of options, and the selected values are returned.*

10. **How can Markdown syntax be utilized to enhance text formatting in Streamlit apps?**
- *Markdown syntax can be used in Streamlit apps with functions like st.text() and st.markdown(). It allows formatting text, creating headers, adding lists, embedding links, and more.*
