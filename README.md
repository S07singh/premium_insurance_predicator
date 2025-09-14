# 🏥 Premium Insurance Predictor

A **FastAPI-based application** to predict **insurance premiums** using a trained ML model.  
This project follows a **modular structure** (config, schema, model) and supports **Docker deployment** for easy scalability.

---

## 📂 Project Structure
```

premium\_insurance\_predictor/
│── config/          # Configuration files
│── model/           # Trained ML model & related code
│── schema/          # Pydantic schemas for validation
│── app.py           # Main FastAPI application
│── frontend.py      # Frontend to interact with the API
│── requirements.txt # Python dependencies
│── Dockerfile       # Containerization setup
│── .gitignore       # Ignored files

````

---

## ⚡ Features
- Predict **insurance premium costs** based on user input  
- **FastAPI REST API** with schema validation  
- Structured and modular project design  
- **Dockerized** for containerized deployment  
- Frontend integration for easy use  

---

## 🛠️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/premium_insurance_predictor.git
cd premium_insurance_predictor
````

### 2️⃣ Create a virtual environment & install dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

pip install -r requirements.txt
```

---

## ▶️ Usage

### Run FastAPI locally

```bash
uvicorn app:app --reload
```

Open API docs:
👉 Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
👉 ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Run the frontend

```bash
python frontend.py
```

---

## 🐳 Run with Docker

### Build Docker image

```bash
docker build -t insurance-predictor .
```

### Run container

```bash
docker run -d -p 8000:8000 insurance-predictor
```

Now open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

---

## 📊 Example API Request

**POST /predict**

```json
{
  "age": 30,
  "sex": "male",
  "bmi": 27.5,
  "children": 2,
  "smoker": "no",
  "region": "southwest"
}
```

**Response**

```json
{
  "predicted_premium": 4210.75
}
```

---

## 📌 Requirements

* Python 3.8+
* FastAPI
* Uvicorn
* Pandas / Scikit-learn
* Docker (optional for containerized deployment)

Install everything with:

```bash
pip install -r requirements.txt
```

---

## 📖 License

This project is open-source and available under the **MIT License**.
