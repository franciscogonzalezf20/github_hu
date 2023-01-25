import SatAbstract
from sat_prueba_concepto.spider_sat_prueba.Validador import Validador


class ScrapearGeneral(SatAbstract):
    estatus_aduana: Validador

    def scrapear_pagina(self):
        pass

    def set_complement(self, regex: str):
        pass
