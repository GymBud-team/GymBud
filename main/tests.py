from django.test import TestCase

from .models import Caracteristicas
from .models import Metas
from .models import PesoHistory
from .models import IngestaoAgua
from .models import IngestaoCalorias
from .models import Post
from .models import Comment

class CaracteristicasTestCase(TestCase):

    def setUp(self):
        usuario =  "Francisco",
        idade = 23 ,
        peso_inicial = 90.0,
        peso_atual = 90.0,
        altura = 1.80,
        inicio = True     #auto_now_add = True
        self.caracteristicas = Caracteristicas(usuario, idade, peso_inicial, peso_atual, altura, inicio)
    
    def test_caracteristicas_usuario_no(self):
        self.assertEqual(self.caracteristicas.usuario(' '), False)

    def test_caracteristicas_usuario_si(self):
        self.assertEqual(self.caracteristicas.usuario('Francisco'), True)

    def test_caracteristicas_idade(self):    
        self.assertEqual(self.caracteristicas.idade(23), True)

    def test_caracteristicas_idade_cond(self):
        if self.caracteristicas.idade == 0 or self.caracteristicas.idade > 130:
            return False
        else:
            return True

    def test_caracteristicas_peso_inicial(self):
        self.assertEqual(self.caracteristicas.peso_inicial(), False)

    def test_caracteristicas_peso_inicial_no(self):
        if self.caracteristicas.peso_inicial < 0:
            return False
        else:
            return True

    def test_caracteristicas_peso_inicial_si(self):    
        self.assertEqual(self.caracteristicas.peso_inicial(90.0), True)

    def test_caracteristicas_peso_atual(self):
        self.assertEqual(self.caracteristicas.peso_atual(), False)

    def test_caracteristicas_peso_atual_cond(self):
        if self.caracteristicas.peso_atual < 0:
            return False
        else:
            return True

    def test_caracteristicas_peso_atual_si(self):    
        self.assertEqual(self.caracteristicas.peso_atual(90.0), True)

    def test_caracteristicas_altura_si(self):
        self.assertEqual(self.caracteristicas.altura(1.80), True)

    def test_caracteristicas_altura_cond(self):
        if self.caracteristicas.altura < 0.0:
            return False
        else:
            return True

    def test_caracteristicas_altura_cond2(self):   # já pede em METRO
        self.assertEqual(self.caracteristicas.altura(180), False)

    def test_caracteristicas_altura_no(self):
        self.assertEqual(self.caracteristicas.altura(0), False)

    #def test_caracteristicas_inicio(self):
    #    self 



class MetasTestCase(TestCase):
    def setUp(self):
        usuario = 'Francisco' ,
        peso = 72.0 ,
        calorias = 2000,
        agua = 4.5
        self.metas = Metas(usuario, peso, calorias, agua)

    def test_metas_usuario_no(self):
        self.assertEqual(self.metas.usuario(' '), False)

    def test_metas_usuario_si(self):
        self.assertEqual(self.metas.usuario('Francisco'), True)

    def test_metas_usuario_cond(self):
        if self.metas.usuario != self.caracteristicas.usuario:
            return False
        else:
            return True

    def test_metas_peso(self):
        self.assertEqual(self.metas.peso(), False)

    def test_metas_peso_no(self):
        if self.metas.peso < 0:
            return False
        else:
            return True

    def test_metas_peso_si(self):    
        self.assertEqual(self.metas.peso(72.0), True)

    def test_metas_peso_cond2(self):
        if self.metas.peso == self.caracteristicas.peso_inicial:
            return False
        else:
            return True
    
    def test_metas_calorias(self):
        self.assertEqual(self.metas.calorias(), False)

    def test_metas_calorias_no(self):
        if self.metas.calorias < 0 or self.metas.calorias > 25000:
            return False
        else:
            return True

    def test_metas_calorias_si(self):    
        self.assertEqual(self.metas.peso(2000), True)

    def test_metas_agua(self):
        self.assertEqual(self.metas.agua(4.5), True)

    def test_metas_agua_no(self):
        self.assertEqual(self.metas.agua(), False)        
    

class PesoHistoryTestCase(TestCase):
    def setUp(self):
        usuario = 'Francisco' ,
        peso = 88.0 ,
        created = 2000 # auto_now_add = True
        self.pesohistory = PesoHistory(usuario, peso, created)

    def test_pesohistory_usuario_no(self):
        self.assertEqual(self.pesohistory.usuario(' '), False)

    def test_pesohistory_usuario_si(self):
        self.assertEqual(self.pesohistory.usuario('Francisco'), True)

    def test_pesohistory_usuario_cond(self):
        if self.pesohistory.usuario != self.caracteristicas.usuario:
            return False
        else:
            return True

    def test_pesohistory_peso(self):
        self.assertEqual(self.pesohistory.peso(88.0), True)
        
    def test_pesohistory_peso_cond(self):
        if self.pesohistory.peso >= 0:
            return True
        else:
            return False

    #def test_pesohistory_peso_cont(self):
        #peso - peso antigo = created

    # def test_pesohistory_created(self):
        #created
    

class IngestaoAguaTestCase(TestCase):
    
    def setUp(self):
        usuario = 'Francisco' ,
        agua = 0.5,
        created = 4.0
        self.ingestao_agua = IngestaoAgua(usuario, agua, created)

    def test_ingestaoAgua_usuario_no(self):
        self.assertEqual(self.ingestaoAgua.usuario(' '), False)

    def test_ingestaoAgua_usuario_si(self):
        self.assertEqual(self.ingestaoAgua.usuario('Francisco'), True)

    def test_ingestaoAgua_usuario_cond(self):
        if self.ingestaoAgua.usuario != self.caracteristicas.usuario:
            return False
        else:
            return True

    def test_ingestaoAgua_agua(self):
        self.assertEqual(self.ingestaoAgua.agua(0.5), True)

    def test_ingestaoAgua_agua_no(self):
        self.assertEqual(self.ingestaoAgua.agua(), False) 

    def test_ingestaoAgua_created(self):
        self.assertEqual(self.ingestaoAgua.created(4.0), True)

    def test_ingestaoAgua_created(self):
        a1 = self.meta.agua - self.ingestaoAgua.agua
        if a1 != self.ingestaoAgua.created :
            return False
        else:
            return True


class IngestaoCaloriasTestCase(TestCase):
    
    def setUp(self):
        usuario = 'Francisco' ,
        calorias = 500,
        created = True    #1500
        self.ingestaoCalorias = IngestaoCalorias(usuario, calorias, created)

    def test_ingestaoCalorias_usuario_no(self):
        self.assertEqual(self.ingestaoCalorias.usuario(' '), False)

    def test_ingestaoCalorias_usuario_si(self):
        self.assertEqual(self.ingestaoCalorias.usuario('Francisco'), True)

    def test_ingestaoCalorias_usuario_cond(self):
        if self.ingestaoCalorias.usuario != self.caracteristicas.usuario:
            return False
        else:
            return True

    def test_ingestaoCalorias_calorias(self):
        self.assertEqual(self.ingestaoCalorias.calorias(500), True)

    def test_ingestaoCalorias_calorias_no(self):
        self.assertEqual(self.ingestaoCalorias.calorias(), False) 

    def test_ngestaoCalorias_created(self):
        k1 = self.meta.calorias - self.ingestaoAgua.calorias
        if k1 != self.ingestaocalorias.created :
            return False
        else:
            return True

class PostTestCase(TestCase):
    
    def setUp(self):
        usuario = 'Francisco'
        #image  -> Proxima entrega por conta da foto e complexidade
        caption = 'Partiu malhar'
        created = True
        self.post = Post(usuario, caption, created)

    def test_post_usuario_no(self):
        self.assertEqual(self.post.usuario(' '), False)

    def test_póst_usuario_si(self):
        self.assertEqual(self.post.usuario('Francisco'), True)

    def test_post_usuario_cond(self):
        if self.post.usuario != self.caracteristicas.usuario:
            return False
        else:
            return True

    def test_post_caption(self):
        self.assertEqual(self.post.caption('Partiu malhar'), True)

    def test_post_caption_no(self):
        self.assertEqual(self.post.caption(' '), False)

    #def test_post_created(self): 
    #    self        DateTimeField(default=datetime.now)


class CommentTestCase(TestCase):
    def setUp(self):
        usuario = 'Francisco'
        #post  -> Proxima entrega por conta da foto e complexidade
        comentario = "Lindos!" # max tamanho = 300
        created = True
        self.comment = Comment(usuario, comentario, created)
    

    def test_comment_usuario_no(self):
        self.assertEqual(self.comment.usuario(' '), False)

    def test_coomment_usuario_si(self):
        self.assertEqual(self.comment.usuario('Francisco'), True)

    def test_comment_usuario_cond(self):
        if self.comment.usuario != self.caracteristicas.usuario:
            return False
        else:
            return True

 
    def test_comment_comentario(self):
        self.assertEqual(self.comment.comentario('Lindos!'), True)

    def test_comment_comentario_no(self):
        self.assertEqual(self.comment.comentario(' '), False)

    def test_comment_comentario_cond(self):
        cont = len(self.comment.comentario)
        if cont  > 300 and cont:
            return False
        else:
            return True
    
    #def test_comment_created(self):
    #   self

        
#if __name__ == '__main__':
 #   TestCase.main()