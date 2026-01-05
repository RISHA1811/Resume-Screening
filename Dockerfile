# 1. Base image
FROM python:3.10-slim

# 2. Set working directory
WORKDIR /app

.

# 3. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy project files
COPY . .

# 5. Expose Streamlit port
EXPOSE 8501

# 6. Streamlit run command
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

