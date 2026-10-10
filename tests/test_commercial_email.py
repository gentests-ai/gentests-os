import json
import unittest
from pathlib import Path
from scripts.validate_commercial_email import validate

BASE = Path(__file__).parent / "fixtures"

class EmailGateTests(unittest.TestCase):
    def test_rascunho_ficticio_sem_bloqueios_tecnicos(self):
        sample = json.loads((BASE / "email_valido.json").read_text(encoding="utf-8"))
        self.assertEqual(validate(sample), [])

    def test_email_sem_fontes_ou_destinatario_bloqueado(self):
        sample = json.loads((BASE / "email_sem_fontes.json").read_text(encoding="utf-8"))
        issues = validate(sample)
        self.assertTrue(any("fontes" in x for x in issues))
        self.assertTrue(any("origem_destinatario" in x for x in issues))
        self.assertTrue(any("Alegação" in x for x in issues))

    def test_envio_no_piloto_bloqueado(self):
        sample = json.loads((BASE / "email_valido.json").read_text(encoding="utf-8"))
        sample["enviado"] = True
        self.assertTrue(validate(sample))

if __name__ == "__main__":
    unittest.main()
