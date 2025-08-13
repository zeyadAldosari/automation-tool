FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && \
    apt-get install -y \
        curl \
        wget \
        git \
        && rm -rf /var/lib/apt/lists/* \
        && apt-get clean
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p /reports
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
RUN useradd -m -s /bin/bash testuser && \
    chown -R testuser:testuser /app /reports
USER testuser
ENTRYPOINT ["behave"]
CMD ["--junit", "--junit-directory", "/reports/junit", "-f", "pretty", "-o", "/reports/text/results.txt"]
