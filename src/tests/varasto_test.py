import unittest
from varasto import Varasto

# Unit testeja varten.

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    # Omaa koodia:
    def test_konstruktori_luo_eityhjan_varaston(self):
        self.varastob = Varasto(-10)
        self.assertEqual(self.varastob.tilavuus, 0)

    # Omaa koodia:
    def test_konstruktori_luo_alkusaldo_ppienempi_kuin_nolla(self):
        self.varastob = Varasto(10, -10)
        self.assertEqual(self.varastob.saldo, 0)

    # Omaa koodia:
    def test_lisataan_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertEqual(self.varasto.saldo, 0)

    # Omaa koodia:
    def test_lisataan_liikaa_varastoon(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus +1)
        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    # Omaa koodia:
    def test_otetaan_negatiivinen_maara(self):
        self.assertEqual(self.varasto.ota_varastosta(-3), 0)

    # Omaa koodia:
    def test_otetaan_enemman_kuin_saldo(self):
        self.assertEqual(self.varasto.ota_varastosta(self.varasto.saldo +1), self.varasto.saldo)

    # Omaa koodia:
    def test_stringi(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
