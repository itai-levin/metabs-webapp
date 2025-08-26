import streamlit as st

st.image('data/npspecdblogo.png')

# Use HTML to format "How to Cite" as underlined and bold.
st.markdown("<b><u>How to Cite</u></b>", unsafe_allow_html=True)

# Display the rest of the citation text
citation_text = ('Chemla, Y.\*, Levin, I.\*, Fan, Y., Johnson, A. A., Coley, C. W., & Voigt, C. A. (2025). Hyperspectral reporters for long-distance and wide-area detection of gene expression in living bacteria. Nature Biotechnology, 1-11. [link](https://rdcu.be/ej8sj)'
)

st.markdown(citation_text)
