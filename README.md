Run all python scripts while inside `./Selenium-Features` directory.

To move the downloaded images inside the docker container:

1. `docker ps` and note the container id
2. `docker cp ./photo_import/. CONTAINER_ID:/var/www/html/img/products`