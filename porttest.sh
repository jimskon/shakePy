#!/bin/bash
# Script to test reception on a given port (5001)
# To run:
# socat -u tcp-l:5001,fork system:./porttest.sh
# Then use browser to query port
read MESSAGE
echo "PID: $$"
echo "$MESSAGE"
