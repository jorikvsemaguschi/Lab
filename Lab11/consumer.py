from kafka import KafkaProducer, KafkaConsumer
import json

consumer = KafkaConsumer(
    'user_actions',
    bootstrap_servers='localhost:9092',
    group_id='user_action_group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

dlt_producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for message in consumer:
    try:
        data = message.value
        if not isinstance(data['user_id'], int):
            raise ValueError("Invalid user_id")
        print("Processed:", data)
    except Exception as e:
        print("Sending to DLT:", message.value)
        dlt_producer.send('user_actions_dlt', message.value)
