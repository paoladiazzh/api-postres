import boto3
import json
import time
from django.core.management.base import BaseCommand
from django.conf import settings
from postres_api.models import Postre
from postres_api.serializers import PostreSerializer

class Command(BaseCommand):
    help = 'Escucha la cola de SQS para crear postres'

    def handle(self, *args, **options):
        # Inicializa el cliente de SQS
        sqs = boto3.client('sqs', region_name=settings.AWS_REGION)
        queue_url = settings.SQS_QUEUE_URL
        
        self.stdout.write(self.style.SUCCESS(f'Iniciando listener para la cola SQS: {queue_url}'))

        while True:
            try:
                # Pide mensajes de la cola
                response = sqs.receive_message(
                    QueueUrl=queue_url,
                    MaxNumberOfMessages=1,
                    WaitTimeSeconds=20  # Long Polling
                )

                if 'Messages' in response:
                    for msg in response['Messages']:
                        receipt_handle = msg['ReceiptHandle']
                        
                        try:
                            # Procesa el mensaje
                            body = json.loads(msg['Body'])
                            self.stdout.write(f"Mensaje recibido: {body}")

                            # Usa el serializer para validar y guardar
                            serializer = PostreSerializer(data=body)
                            if serializer.is_valid():
                                serializer.save()
                                self.stdout.write(self.style.SUCCESS(f"Postre '{body['nombre']}' guardado en la base de datos."))
                                
                                # Borra el mensaje de la cola para no procesarlo de nuevo
                                sqs.delete_message(
                                    QueueUrl=queue_url,
                                    ReceiptHandle=receipt_handle
                                )
                                self.stdout.write(f"Mensaje eliminado de la cola.")
                            else:
                                self.stdout.write(self.style.ERROR(f"Error de validación: {serializer.errors}"))
                                # Aquí podrías mover el mensaje a una Dead Letter Queue

                        except Exception as e:
                            self.stdout.write(self.style.ERROR(f"Error procesando mensaje: {e}"))

                else:
                    self.stdout.write("No hay mensajes en la cola. Esperando...")
            
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error de conexión con SQS: {e}"))
                time.sleep(10) # Espera antes de reintentar la conexión