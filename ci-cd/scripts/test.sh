echo "Running tests..."
curl http://localhost:5000/patients || exit 1
curl http://localhost:5001/appointments || exit 1
curl http://localhost:5002/notifications || exit 1
curl http://
localhost:5003/aggregate || exit 1
echo "All tests passed!"

