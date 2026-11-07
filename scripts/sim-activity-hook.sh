#!/bin/zsh
# PostToolUse hook: marks simulator activity only when a tool call touched a simulator.
input=$(cat)
if print -r -- "$input" | grep -qE 'iOS_Simulator|simctl|xcodebuild|flutter (run|drive|test)|-destination|iphonesimulator'; then
  touch ~/.claude/state/sim-activity
fi
exit 0
