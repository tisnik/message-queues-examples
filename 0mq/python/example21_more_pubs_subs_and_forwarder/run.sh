export PYTHONUNBUFFERED=yes

python3 forwarder.py > forwarder.out &
forwarder_pid=$!

python3 publisher.py Publisher1 1 > publisher1.out 2>&1 &
publisher1_pid=$!

python3 publisher.py Publisher2 0.5 > publisher2.out 2>&1 &
publisher2_pid=$!

python3 publisher.py Publisher3 0.2 > publisher3.out 2>&1 &
publisher3_pid=$!

python3 subscriber.py > subscriber1.out &
subscriber1_pid=$!

python3 subscriber.py > subscriber2.out &
subscriber2_pid=$!

python3 subscriber.py > subscriber3.out &
subscriber3_pid=$!

sleep 20

kill $forwarder_pid
kill $publisher1_pid
kill $publisher2_pid
kill $publisher3_pid
kill $subscriber1_pid
kill $subscriber2_pid
kill $subscriber3_pid
