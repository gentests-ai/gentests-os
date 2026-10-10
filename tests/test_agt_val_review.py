import json
import unittest
from pathlib import Path
from scripts.agt_val_review import review

BASE = Path(__file__).parent / "fixtures"

def load(name):
    return json.loads((BASE/name).read_text(encoding="utf-8"))

class ReviewTests(unittest.TestCase):
    def test_parecer_nao_autoriza_envio(self):
        result=review(load("email_valido.json"))
        self.assertFalse(result["pode_enviar"])
        self.assertEqual(result["autorizacao_humana"],"PENDENTE")
        self.assertEqual(result["resultado"],"CORRECAO_NECESSARIA")
    def test_alegacao_sem_evidencia(self):
        result=review(load("email_sem_fontes.json"))
        self.assertTrue(any(a["id"]=="QG-ALEGACAO" for a in result["achados"]))
    def test_segredo_bloqueia(self):
        item=load("email_valido.json")
        item["corpo"]="api_key: ABC123XYZ456"
        result=review(item)
        self.assertEqual(result["resultado"],"BLOQUEADO")
    def test_sem_prova_visual_nao_e_conforme(self):
        item=load("email_valido.json")
        item["assinatura_arquivo_oficial"]="assinatura-v3"
        result=review(item)
        self.assertIn("QG-RENDER",[a["id"] for a in result["achados"]])
    def test_falta_revisao_semantica(self):
        self.assertIn("QG-SEMANTICA",[x["id"] for x in review(load("email_valido.json"))["achados"]])

if __name__=="__main__":
    unittest.main()
