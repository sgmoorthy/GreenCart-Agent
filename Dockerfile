FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY greencart_backend greencart_backend/
COPY greencart_ui greencart_ui/
CMD uvicorn greencart_backend.main:app --host 0.0.0.0 --port 8000 &
CMD streamlit run greencart_ui/app.py --server.port=8501
