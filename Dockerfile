FROM pathwaycom/pathway:latest

ENV PATHWAY_LICENSE_KEY = "demo-license-key-with-telemetry"
ENV PATHWAY_SERVICE_INSTANCE_ID = "pathway-gcp-demo"

ENV PORT 8080

COPY app.py .

CMD ["python", "app.py"]
