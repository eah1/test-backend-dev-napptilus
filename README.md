# test-backend-dev-napptilus
Backend Developer - Entry level test

cd app/

docker build -t <name_image> .
docker run -p 8000:8000 -d <name_image>
docker container ls -> look <container_id>
docker logs -f <container_id>
Apartir d'aqui consulta localhost:8000

docker stop <container_id>
