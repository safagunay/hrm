#!/bin/bash

stop_and_rm_if_exists() {
  container_name=$(docker ps -a --format='{{ .Names }}' | grep postgres)
  if [[ $? -eq 0 ]]; then
    docker stop $container_name && docker rm $container_name
  fi
}

run_postgres() {
  docker run -d --name postgres -p 5432:5432 postgresondocker:9.3
}

upgrade_and_migrate() {
  python migrate.py db init
  python migrate.py db migrate
  python migrate.py db upgrade
}

insert_data() {
  python insert_admin_data.py $1
  python insert_fake_data.py $2
}

main() {
  stop_and_rm_if_exists
  sleep 2
  run_postgres; sleep 3 &&  upgrade_and_migrate
  insert_data
}

main


