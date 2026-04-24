#!/bin/bash

LOG_PATH="/opt/container-monitor/logs/container.log"
DATE=$(date "+%c")
CONTAINER_NAME="f3b77687d308"

STATE=$(docker inspect -f '{{.State.Status}}' "$CONTAINER_NAME" 2>/dev/null)

if [[ "$STATE" != "running" ]]; then
  if [[ -z "$STATE" ]]; then
    echo "Time: $DATE | ERROR: Container '$CONTAINER_NAME' does not exist."
  else
    echo "Time: $DATE | ERROR: Container '$CONTAINER_NAME' is $STATE (not running)."
  fi
  exit 1
fi

docker stats --no-stream --format "Time: $DATE | Container: {{.Name}} | MEMORY: {{.MemUsage}} | CPU: {{.CPUPerc}}" $CONTAINER_NAME