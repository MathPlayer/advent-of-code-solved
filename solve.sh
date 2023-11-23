#!/usr/bin/env bash
#
# Simple script making use of https://github.com/scarvalhojr/aoc-cli to solve the problems from terminal.
#
# TODO: create template files for part 1 and part 2.

USAGE="Enables interactive solving for one day of AoC:
1. create a ./<year>/<day>/ directory.
2. Run for part X (first 1, then 2):
   a. Download the puzzle description and input.
   b. Wait for an answer to try out.
   c. Submit the answer.
   d. If not correct, go back to 2.2. If correct, either go to part 2 or end the run.

Usage: ./solve.sh [-y <YEAR>] [-d <DAY>] [-s]

Options:
  -y <YEAR> - Specifies the year to solve. Defaults to the current year.
  -d <DAY>  - Specifies the day to solve. Defaults to the current day.
  -s        - Skips parts one for the given year/day.
 "

parse_cli() {
  # Parse year and day from CLI arguments.
  YEAR="$(date '+%Y')"
  DAY="$(date '+%d')"
  SKIP_PART_1="false"
  while getopts ":y:d:sh" opt; do
    case $opt in
      y)
        YEAR="$OPTARG"
        ;;
      d)
        DAY=$(printf '%02d' "$OPTARG")
        ;;
      s)
        SKIP_PART_1="true"
        ;;
      h)
        echo "$USAGE"
        exit 0
        ;;
      \?)
        echo "Invalid option: -$OPTARG" >&2
        exit 1
        ;;
      :)
        echo "Option -$OPTARG requires an argument." >&2
        exit 1
        ;;
    esac
  done
  if [ -z "$YEAR" ] || [ -z "$DAY" ]; then
    echo >&2 "$USAGE"
    exit 1
  fi
}

# Runs the loop for submitting the answers.
# Uses variables ROOT_DIR, YEAR and DAY.
solve() {
  part=$1
  part_dir="$ROOT_DIR/$YEAR/$DAY/part-$part"
  echo ">>> Running on $part_dir"

  mkdir -p "${part_dir}"
  pushd "$part_dir" || (echo >&2 "Cannot cd into $part_dir" && exit 1)

  aoc download -y "${YEAR}" --day "${DAY}" --overwrite
  glow "$part_dir/puzzle.md"
  while true; do
    date -R
    read -r -p ">>> Enter your answer: " answer
    date -R
    echo ">>> Submitting answer"
    output=$(aoc submit -y "$YEAR" -d "$DAY" "$part" "$answer" | tee "/dev/tty")
    if [[ "$output" == *"$CORRECT_TEXT"* ]]; then
      echo ">>> Success: The answer is correct."
    else
      echo ">>> Error or Incorrect Answer."
    fi
  done
  popd || (echo >&2 "Cannot cd from $part_dir" && exit 1)
}


ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
CORRECT_TEXT="That's the right answer"
parse_cli "$@"
if [[ ! $SKIP_PART_1 ]]; then
  solve 1
fi
solve 2
