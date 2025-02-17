from paho.mqtt import client as mqtt_client

broker = '147.142.19.112'
port = 1883
topic = "altes/Feschbach_Water_Interlock/"
client_id = "Feschbach_Water_Interlock"

def connect_mqtt():
    def on_connect(client,userdata,flags,rc):
        if rc == 0:
            print("Connected to MQTT Broker")
        else:
            print("Failed to connect, return code %d\n",rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set("smartlab", "TtSwjSstVDGB")
    client.on_connect = on_connect
    client.connect(broker,port)
    return client

def publish(client):

    while True:


        result = client.publish(topic, Input)
        status = result[0]
        if status == 0:
            print(f"Send `{Input}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic `{topic}`")

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()
