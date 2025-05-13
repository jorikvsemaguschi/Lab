from kafka import KafkaConsumer
import json
import psycopg2

consumer = KafkaConsumer(
    'user_actions',
    bootstrap_servers='localhost:9092',
    group_id='db_group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

conn = psycopg2.connect(
    dbname='your_db',
    user='your_user',
    password='your_pass',
    host='localhost'
)
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS user_actions (
        user_id INT,
        action TEXT,
        timestamp TIMESTAMP
    )
''')
conn.commit()

for message in consumer:
    data = message.value
    cur.execute(
        "INSERT INTO user_actions (user_id, action, timestamp) VALUES (%s, %s, %s)",
        (data['user_id'], data['action'], data['timestamp'])
    )
    conn.commit()
    print("Saved to DB:", data)
