FROM python:3.13-slim
WORKDIR /app
COPY pyproject.toml ./
COPY src ./src
RUN pip install --no-cache-dir .
ARG APP_VERSION=dev
ENV APP_VERSION=${APP_VERSION} PORT=8080
EXPOSE 8080
USER nobody
CMD ["python", "-m", "shopcart.server"]
