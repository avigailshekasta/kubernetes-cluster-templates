# שלב 1: ביסוס התמונה על Python
FROM python:3.9-slim

# שלב 2: הגדרת תיקיית עבודה בתוך המכולה
WORKDIR /app

# שלב 3: העתקת קבצים לתוך המכולה
COPY app/ /app/

# שלב 5: חשיפת פורט 8080
EXPOSE 8080

# שלב 4: התקנת התלויות
RUN pip install --no-cache-dir -r /app/requirements.txt

# שלב 5: הפעלת האפליקציה
CMD ["python", "service_a_app.py"]
