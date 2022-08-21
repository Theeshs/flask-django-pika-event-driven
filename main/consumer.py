from email.mime import image
import pika, json
from main import Product, db

parms = pika.URLParameters("amqps://xnolggsb:me9LzNvUf1Qivez6jwHHF_uTYrclzVey@armadillo.rmq.cloudamqp.com/xnolggsb")

connetion = pika.BlockingConnection(parms)

channel = connetion.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print("Received in main")
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(
            id=data["id"],
            title=data["title"],
            image=data["image"]
        )
        db.session.add(product)
        db.session.commit()

    elif properties.content_type == 'product_updated':
        product = Product.query.get(id=data["id"])
        product.title=data["title"],
        product.image=data["image"]
        db.session.commit()
    
    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()

channel.basic_consume(queue="main", on_message_callback=callback, auto_ack=True)

print("Strated consuming")
channel.start_consuming()

channel.close()