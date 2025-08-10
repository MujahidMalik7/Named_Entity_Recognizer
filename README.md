# Named Entity Recognition (NER) Project

## 📌 Project Overview  
This project focuses on **Named Entity Recognition (NER)** — the task of identifying and classifying entities (such as people, organizations, locations, dates, and more) from text.  
It was developed in two main stages:

- Model Evaluation & Comparison on a dataset.  
- Deployment of the best-performing model using Streamlit for an interactive NER highlighter app.

---

## 🧪 Stage 1: Model Evaluation  

In the first phase, I implemented and evaluated multiple NER models to determine the most suitable one for deployment. The models tested were:

| Model               | Type                          | Key Features                               |
|---------------------|-------------------------------|--------------------------------------------|
| `en_core_web_sm`    | spaCy small model             | Lightweight, fast, but less accurate.      |
| `en_core_web_trf`   | spaCy Transformer-based model | Uses Transformers for improved accuracy.   |
| `dslim/bert-base-NER` | Hugging Face Transformer model | Fine-tuned BERT model for NER tasks.      |

### Evaluation Methodology  
- Used a **CoNLL-like dataset** for testing.  
- Converted spaCy entity labels to CoNLL format for alignment.  
- Evaluated models on **Precision, Recall, and F1-score** using `seqeval`.  
- Conducted tests on both a real dataset and a custom synthetic dataset (50 diverse sentences with various entity types).  
- Visualized performance comparisons with **matplotlib** bar charts.

### Key Results  
From the evaluation:  
- `en_core_web_trf` achieved the **best balance** between accuracy and robustness.  
- `dslim/bert-base-NER` performed well on some entities but struggled with others in my dataset.  
- `en_core_web_sm` was the fastest but had lower accuracy compared to the Transformer-based models.

Based on these results, **`en_core_web_trf`** was selected for deployment.

---

## 💻 Stage 2: Streamlit Deployment  

After selecting **`en_core_web_trf`**, I developed an **interactive NER highlighter** using Streamlit.  
Key features of the web app:

- **Text Input Area**: Users can enter any text to analyze.  
- **Color-Coded Entity Highlighting**: Each entity type is displayed with a distinct background color.  
- **Sidebar Entity Legend**:  
  - Shows each spaCy entity label.  
  - Maps it to its CoNLL equivalent.  
  - Provides a **human-friendly description** of the entity type (e.g., `NORP` → "Nationalities, religious or political groups").  
  - Displays the corresponding highlight color.  
- **Entity Categories Supported**: PERSON, ORG, GPE, LOC, FAC, MISC, PRODUCT, EVENT, DATE, MONEY.

---

## 📊 Example Output  

**Sidebar Legend**  

| Entity Label | CoNLL Tag | Description                                  | Highlight Color |
|--------------|-----------|----------------------------------------------|-----------------|
| PERSON       | PER       | People, including fictional characters       | lightgreen      |
| ORG          | ORG       | Organizations, companies, agencies           | lightblue       |
| GPE          | GPE       | Countries, cities, states                     | orange          |
| LOC          | LOC       | Non-GPE locations, mountain ranges, bodies of water | yellow          |
| FAC          | FAC       | Buildings, airports, highways, bridges       | pink            |
| MISC         | MISC      | Miscellaneous entities                        | purple          |
| PRODUCT      | PROD      | Objects, vehicles, foods                      | teal            |
| EVENT        | EVNT      | Named events like wars, sports events         | brown           |
| DATE         | DATE      | Absolute or relative dates or periods         | lightgray       |
| MONEY        | MONEY     | Monetary values, including unit               | gold            |

**Highlighted Text Example:**  
Barack Obama (PERSON) was elected President of the United States (GPE) in 2008 (DATE).

---

## 🛠 Tools & Libraries Used  
- Python  
- spaCy (`en_core_web_sm`, `en_core_web_trf`)  
- Transformers (`dslim/bert-base-NER`)  
- seqeval (evaluation metrics)  
- matplotlib (visualizations)  
- Streamlit (web deployment)  

---

## 📌 Summary  
- Compared three NER models (`en_core_web_sm`, `en_core_web_trf`, `dslim/bert-base-NER`) on real and synthetic datasets.  
- Selected `en_core_web_trf` as the final model due to its accuracy and balanced performance.  
- Built a Streamlit web app that allows interactive entity recognition with color-coded highlights and an easy-to-understand legend.

---

## 🏷️ Tags  
#NLP #NER #spaCy #Transformers #BERT #Streamlit #MachineLearning #DeepLearning #Python #HuggingFace #NaturalLanguageProcessing #AI #DataScience

---

