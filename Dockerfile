# syntax=docker/dockerfile:1
# ---------- stage 1: build the dependencies ----------
FROM python:3.12-slim AS build
RUN python -m venv /venv
COPY requirements.txt .
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

# ---------- stage 2: only what runs ----------
FROM python:3.12-slim
RUN useradd --system --uid 10001 --no-create-home app
WORKDIR /code
COPY --from=build /venv /venv
COPY app ./app
ENV PATH="/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
USER 10001
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
