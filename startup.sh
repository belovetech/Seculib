#!/bin/bash

# Stop and remove old containers
docker compose down -v

# Build without cache, Force recreate and start containers
docker compose up -V --build --force-recreate --remove-orphans --watch
