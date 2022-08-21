import pika, json

parms = pika.URLParameters(
    "amqps://xnolggsb:me9LzNvUf1Qivez6jwHHF_uTYrclzVey@armadillo.rmq.cloudamqp.com/xnolggsb"
)

connetion = pika.BlockingConnection(parms)

channel = connetion.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key="main", body=json.dumps(body), properties=properties)
    # return