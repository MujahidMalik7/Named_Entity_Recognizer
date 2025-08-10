# ner_app.py
import spacy
import streamlit as st
import html

try:
    nlp = spacy.load("en_core_web_trf")
except OSError:
    # fallback for debugging, try download once (optional)
    import subprocess, sys
    subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_trf"])
    nlp = spacy.load("en_core_web_trf")


# Mapping from spaCy labels to CoNLL labels
spacy2conll = {
    "PERSON": "PER",
    "NORP": "MISC",
    "ORG": "ORG",
    "GPE": "GPE",
    "LOC": "LOC",
    "FAC": "FAC",
    "MISC": "MISC",
    "PRODUCT": "PROD",
    "EVENT": "EVENT",
    "DATE": "DATE",
    "MONEY": "MONEY"
}

# Human-friendly descriptions for spaCy entity types
entity_descriptions = {
    "PERSON": "People, including fictional characters",
    "NORP": "Nationalities, religious or political groups",
    "ORG": "Organizations (companies, agencies, institutions)",
    "GPE": "Countries, cities, states",
    "LOC": "Locations (non-political, e.g., mountains, rivers)",
    "FAC": "Facilities (buildings, airports, highways)",
    "MISC": "Miscellaneous entities",
    "PRODUCT": "Products (objects, vehicles, foods, etc.)",
    "EVENT": "Named events (wars, sports events, etc.)",
    "DATE": "Specific dates or periods",
    "MONEY": "Monetary values"
}

# Colors for entity types
colors = {
    "PERSON": "lightgreen",
    "ORG": "lightblue",
    "GPE": "orange",
    "DATE": "pink",
    "MONEY": "yellow",
    "PRODUCT": "violet",
    "LOC": "lightcoral",
    "MISC": "lightgrey",
    "EVENT": "khaki",
    "FAC": "wheat",
    "NORP": "lightseagreen"
}

# Load SpaCy model once with caching and error handling
@st.cache_resource
def load_model():
    try:
        return spacy.load("en_core_web_trf")
    except Exception as e:
        st.error(f"Failed to load spaCy model: {e}")
        return None

nlp = load_model()

# Highlight function for HTML with escaping
def highlight_entities_html(doc):
    html_output = ""
    last_idx = 0
    text = doc.text
    for ent in doc.ents:
        html_output += html.escape(text[last_idx:ent.start_char])
        color = colors.get(ent.label_, "lightgrey")
        ent_text = html.escape(ent.text)
        html_output += f'<span style="background-color:{color}; font-weight:bold;">{ent_text} ({ent.label_})</span>'
        last_idx = ent.end_char
    html_output += html.escape(text[last_idx:])
    return html_output

# Sidebar: Show entity color legend with descriptions
st.sidebar.header("Entity Legend")
for label, conll in spacy2conll.items():
    color = colors.get(label, "lightgrey")
    description = entity_descriptions.get(label, "No description available")
    st.sidebar.markdown(
        f'<div style="margin-bottom:8px;">'
        f'<span style="background-color:{color}; padding:4px; border-radius:4px; color:black;">{label}</span> '
        f'→ **{conll}**<br>'
        f'<small>{description}</small>'
        f'</div>',
        unsafe_allow_html=True
    )

# Main UI
st.title("Named Entity Recognition (NER) Highlighter")
st.write("Enter text and see detected entities highlighted with colors.")

user_input = st.text_area("Enter text here", height=150)

if st.button("Analyze Entities"):
    if not nlp:
        st.error("Model not loaded, please check setup.")
    elif user_input.strip():
        with st.spinner("Analyzing text..."):
            doc = nlp(user_input)
            if doc.ents:
                st.markdown(highlight_entities_html(doc), unsafe_allow_html=True)
            else:
                st.warning("No entities found.")
    else:
        st.error("Please enter some text.")
