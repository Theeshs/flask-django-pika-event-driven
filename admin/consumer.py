import pika

parms = pika.URLParameters("amqps://xnolggsb:me9LzNvUf1Qivez6jwHHF_uTYrclzVey@armadillo.rmq.cloudamqp.com/xnolggsb")

connetion = pika.BlockingConnection(parms)

channel = connetion.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print("Received in admin")
    print(body)

channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack=True)

print("Strated consuming")
channel.start_consuming()

channel.close()