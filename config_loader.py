import json

def get_database_info():
    with open("./config/database.json", "r") as f:
        database_info = json.load(f)
        return database_info

def get_mqtt_info():
    with open("./config/mqtt.json", "r") as f:
        mqtt_info = json.load(f)
        return mqtt_info

# not used yet.
# def get_tcp_qyery_host_info():
#     with open("./config/tcp_host.json", "r") as f:
#         tcp_host_info = json.load(f)
#         return tcp_host_info