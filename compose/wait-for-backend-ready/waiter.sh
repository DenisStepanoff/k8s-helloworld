#!/bin/sh

set -e

CONT_NAME="hw-backend"
PORT="8080"
CMD="$@"

until curl http://"$CONT_NAME":"$PORT"; do
  >&2 echo "$CONT_NAME is DOWN"
  sleep 1
done

>&2 echo "$CONT_NAME is READY"

exec $CMD

