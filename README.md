## Political Figure Classifier

The Political Figure Classifier is a machine learning application designed to classify political figures based on images. The model uses SVM (Support Vector Machine). The application features a responsive front-end built with Vue.js and a back-end powered by Flask, which serves the classification model through a RESTful API.

Short demo on how it works! You can try it yourself [here](https://political-figure-classifier-a.vercel.app/)

![Alt text](resources/Demo.gif)

## 🚀 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Abdu-LateefLF/political-figure-classifier.git
   cd political-figure-classifier
   ```
2. Create a Virtual Environment
   ```bash
   cd server
   python -m venv venv
   source venv\Scripts\activate
   ```
3. Install Server Dependencies
   ```bash
    pip install -r requirements.txt
   ```
4. Run the Flask Backend
   ```bash
   python server.py
   ```
5. Start the Frontend
   ```bash
   cd ../client
   npm install
   npm run dev
   ```
