from django.contrib.auth.models import User
from .models import ChargePoint
import base64

from rest_framework import HTTP_HEADER_ENCODING, status
from rest_framework.test import APITestCase


class EndpointViewTest(APITestCase):

    def setUp(self):
        username = "test_username"
        password = "test_password"

        # Creamos un usuario
        self.user = User.objects.create_user(username=username, password=password)

        # Generamos las creadenciales en Base64
        credentials = f"{username}:{password}"

        base64_credentials = base64.b64encode(
            credentials.encode(HTTP_HEADER_ENCODING)
        ).decode(HTTP_HEADER_ENCODING)

        self.authorization = base64_credentials

        # creamos un objeto ChargePoint
        self.object_chargepoint = ChargePoint.objects.create(name="cargador")

    def test_endpoint_get(self):

        # Hacemos la llamada Get para obtener los cargadores.
        response = self.client.get(
            path="/charge/chargepoint/",
            HTTP_AUTHORIZATION=f"Basic {self.authorization}",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_endpoint_get_by_id(self):

        # Hacemos la llamada Get pansandole como parametro el ID para obtener la informacion del cargador.
        response = self.client.get(
            path=f"/charge/chargepoint/{self.object_chargepoint.id}/",
            HTTP_AUTHORIZATION=f"Basic {self.authorization}",
            follow=True
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_endpoint_post(self):

        # Hacemos la llamada Post para crear un cargador.
        response = self.client.post(
            path="/charge/chargepoint/",
            data={ "name" : "primer cargador" },
            HTTP_AUTHORIZATION=f"Basic {self.authorization}",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Hacemos la llamada Post con un nombre de campo inventado para que nos devuelva un error.
        response = self.client.post(
            path="/charge/chargepoint/",
            data={ "nombre_inventado" : "primer cargador" },
            HTTP_AUTHORIZATION=f"Basic {self.authorization}",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_endpoint_put(self):

        # Hacemos la llamada Put para actualizar el estado.
        response = self.client.put(
            path=f"/charge/chargepoint/{self.object_chargepoint.id}/",
            data={ "status" : "charging" },
            HTTP_AUTHORIZATION=f"Basic {self.authorization}",
            follow=True,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_endpoint_delete(self):

        # Hacemos la llamada Delete para eliminar el objeto.
        response = self.client.delete(
            path=f"/charge/chargepoint/{self.object_chargepoint.id}/",
            HTTP_AUTHORIZATION=f"Basic {self.authorization}",
            follow=True,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)