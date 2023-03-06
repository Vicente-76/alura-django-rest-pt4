from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from escola.models import Curso


class CursosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create()
        self.curso_2 = Curso.objects.create()

    # def test_falha_proposital(self):
    #     self.fail('Teste falhou de proposito')

    def test_requisicao_get_para_listar_cursos(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_um_curso(self):
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'Curso de teste 3 ',
            'nivel': 'A',
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_curso(self):
        """ Teste para verificação de bloqueio da requisição delete """
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_atualizar_curso(self):
        data = {
            'codigo_curso': 'CTT2',
            'descricao': 'Curso de teste 2 atualizado',
            'nivel': 'I',
        }
        response = self.client.put('/cursos/2/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)