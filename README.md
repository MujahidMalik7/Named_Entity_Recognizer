# Named Entity Recognition (NER) Project

## 📌 Project Overview  
This project focuses on **Named Entity Recognition (NER)** — the task of identifying and classifying entities (such as people, organizations, locations, dates, and more) from text.  
It was developed in two main stages:

- Model Evaluation & Comparison on a dataset.  
- Deployment of the best-performing model using Streamlit for an interactive NER highlighter app.
- Command-line interface to run NER analyses directly from the terminal, allowing batch or interactive text processing without UI.

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


## 🛠 Tools & Libraries Used  
- Python  
- spaCy (`en_core_web_sm`, `en_core_web_trf`)  
- Transformers (`dslim/bert-base-NER`)  
- seqeval (evaluation metrics)  
- matplotlib (visualizations)  

---

## 📌 Summary  
- Compared three NER models (`en_core_web_sm`, `en_core_web_trf`, `dslim/bert-base-NER`) on real and synthetic datasets.  
- Selected `en_core_web_trf` as the final model due to its accuracy and balanced performance.  
- Developed a command-line interface (CLI) to allow running the NER program directly from the terminal for flexible usage without a UI.

---

## 🏷️ Tags  
#NLP #NER #spaCy #Transformers #BERT #Streamlit #MachineLearning #DeepLearning #Python #HuggingFace #NaturalLanguageProcessing #AI #DataScience

---

