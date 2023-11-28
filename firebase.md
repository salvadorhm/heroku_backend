curl -X 'PATCH' 'https://fir-iot-498a3-default-rtdb.firebaseio.com/sensores.json/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"motor": "23"}'

curl -X 'GET' 'https://fir-iot-498a3-default-rtdb.firebaseio.com/sensores.json' -H 'accept: application/json' -H 'Content-Type: application/json'