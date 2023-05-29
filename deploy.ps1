docker-compose up -d --build
docker exec campain_viewer-web-1 pytest --cov=app tests/