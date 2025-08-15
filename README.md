# Named Entity Recognition (NER) Project

## 📌 Project Overview  
This project focuses on **Named Entity Recognition (NER)** — the task of identifying and classifying entities (such as people, organizations, locations, dates, and more) from text.  
It was developed in three main stages:

- Model Evaluation & Comparison on a dataset.  
- Deployment of the best-performing model using **Streamlit** for an interactive NER highlighter app.  
- Command-line interface to run NER analyses directly from the terminal, allowing batch or interactive text processing without UI.

---

## 🧪 Stage 1: Model Evaluation  

In the first phase, I implemented and evaluated multiple NER models to determine the most suitable one for deployment. The models tested were:

| Model                  | Type                          | Key Features                               |
|------------------------|-------------------------------|--------------------------------------------|
| `en_core_web_sm`       | spaCy small model             | Lightweight, fast, but less accurate.      |
| `en_core_web_trf`      | spaCy Transformer-based model | Uses Transformers for improved accuracy.   |
| `dslim/bert-base-NER`  | Hugging Face Transformer model| Fine-tuned BERT model for NER tasks.       |

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

Based on these results, **`en_core_web_trf`** was originally selected for deployment.  
However, for the **Streamlit application**, I implemented a lightweight version using `en_core_web_sm` to ensure faster load times and smooth performance on free cloud hosting.

---

## 💻 Stage 2: Streamlit NER App  

An interactive web application was built using **Streamlit** that:  
- Highlights detected entities with different colors.  
- Displays a legend mapping entity labels to CoNLL tags and human-readable descriptions.  
- Works with `en_core_web_sm`.
- Can be accessed online at:  
🔗 **[NER Streamlit App](https://named-entity-recognizer-mujahid07.streamlit.app/)**

---

## 💻 Stage 3: CLI Tool  
A **command-line interface (CLI)** was also developed to:  
- Run NER on text inputs directly from the terminal.  
- Support both batch processing (multiple texts) and interactive mode.  
- Provide the same output formatting and entity labeling as the Streamlit app.

---

## 🛠 Tools & Libraries Used  
- Python  
- spaCy (`en_core_web_sm`, `en_core_web_trf`)  
- Transformers (`dslim/bert-base-NER`)  
- seqeval (evaluation metrics)  
- matplotlib (visualizations)  
- Streamlit (web app deployment)

---

## 📌 Summary  
- Compared three NER models (`en_core_web_sm`, `en_core_web_trf`, `dslim/bert-base-NER`) on real and synthetic datasets.  
- Selected `en_core_web_trf` for highest accuracy, and `en_core_web_sm` for the lightweight Streamlit app deployment.  
- Built an interactive **Streamlit app** for visualizing NER results.  
- Developed a **CLI tool** for flexible usage without a UI.  
- App is live here:  
  🔗 **[https://named-entity-recognizer-mujahid07.streamlit.app/](https://named-entity-recognizer-mujahid07.streamlit.app/)**

---

## 🏷️ Tags  
#NLP #NER #spaCy #Transformers #BERT #Streamlit #MachineLearning #DeepLearning #Python #HuggingFace #NaturalLanguageProcessing #AI #DataScience
