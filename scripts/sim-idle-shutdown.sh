#!/bin/zsh
# Shuts down booted iOS simulators once Claude has been idle for IDLE_MIN minutes.
# Activity stamp is touched by a PostToolUse hook whenever a tool call uses a simulator.
IDLE_MIN=${IDLE_MIN:-30}
STAMP=~/.claude/state/sim-activity
LOG=~/.claude/state/sim-idle-shutdown.log
export PATH=/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin

booted=$(xcrun simctl list devices booted 2>/dev/null | grep -c "(Booted)")
[[ $booted -eq 0 ]] && exit 0

# Under memory pressure (swap nearly full) wait only 10 minutes.
swap_free=$(sysctl -n vm.swapusage | sed -E 's/.*free = ([0-9.]+)M.*/\1/')
(( ${swap_free%.*} < 2048 )) && IDLE_MIN=10

# Simulator still in use?
if [[ -f $STAMP ]]; then
  age=$(( ($(date +%s) - $(stat -f %m $STAMP)) / 60 ))
  [[ $age -lt $IDLE_MIN ]] && exit 0
fi

# A build, test or flutter run is using a simulator right now.
pgrep -qf "xcodebuild|simctl (install|launch|spawn|io)|flutter_tools.snapshot (run|drive|test)" && exit 0

xcrun simctl shutdown all 2>>$LOG
echo "$(date '+%F %T') shut down $booted simulator(s), idle ${age:-?} min" >> $LOG
