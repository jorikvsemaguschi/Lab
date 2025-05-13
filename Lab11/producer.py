from kafka import KafkaProducer
import json
import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    try:
        user_id = int(input("User ID: "))
        action = input("Action: ")
        message = {
            "user_id": user_id,
            "action": action,
            "timestamp": datetime.datetime.utcnow().isoformat()
        }
        producer.send('user_actions', message)
        print(f"Sent: {message}")
    except Exception as e:
        print(f"Error: {e}")
