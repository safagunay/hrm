#!/bin/bash

stop_and_rm_if_exists() {
  container_name=$(docker ps -a --format='{{ .Names }}' | grep postgres)
  if [[ $? -eq 0 ]]; then
    docker stop $container_name && docker rm $container_name
  fi
}

run_postgres() {
  docker run -d --name postgres -e POSTGRES_PASSWORD=zopsedu  -e POSTGRES_USER=zopsedu -e POSTGRES_DB=zopsedu -p 5432:5432 postgres
}

upgrade_and_migrate() {
  python ../models.py db upgrade
}

insert_data() {
  python fake_data.py all 10
  python manage.py insert_data

}

main() {
  stop_and_rm_if_exists
  sleep 2
  run_postgres; sleep 3 &&  upgrade_and_migrate;
}

main


