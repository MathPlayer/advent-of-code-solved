#!/usr/bin/env bash
#
# Monitor a file with the solution / algorithm for solvoing one part and runs it again.
# Works only on macOS by making use of fswatch.
#
# Supported filetypes:
# - Python
#

execute_python_file() {
  echo ">>> Starting new run ..."
  pushd "$(dirname "$1")" >/dev/null || exit
  python3 "$(basename "$1")" &
  popd >/dev/null || exit
}

# Handle CTRL+C.
handle_sigint() {
  if [[ "$PID" -ne 0 ]]; then
    kill "$PID" &>/dev/null
  fi
  exit 0
}
trap handle_sigint SIGINT

# File path sanity check.
if [[ -z "$1"  || ! -f "$1" ]]; then
  echo "Please provide a valid file to monitor."
  exit 1
fi
FILE_PATH="$1"
echo ">>> Monitor $FILE_PATH..."

execute_python_file "$FILE_PATH"
PID=$!
while true; do
  fswatch -1 "$FILE_PATH" &>/dev/null  # macOS specific.
  if [[ $PID -ne 0 ]]; then
    kill $PID &>/dev/null
  fi
  execute_python_file "$FILE_PATH"
  PID=$!
done
