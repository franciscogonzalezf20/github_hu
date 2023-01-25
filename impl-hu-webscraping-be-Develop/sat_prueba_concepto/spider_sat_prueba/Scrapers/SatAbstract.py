from abc import ABC
from abc import abstractmethod
from sat_prueba_concepto.spider_sat_prueba.Validador import Validador
import scrapy


class SatAbstract(ABC, scrapy.Spider):
    name = "sat"
    allowed_domains = ['pecem.mat.sat.gob.mx']
    base_url = 'https://pecem.mat.sat.gob.mx/app/qr/ce/faces/pages/mobile/validadorqr.jsf?D1=16&D2=1&D3='
    numero_validado: Validador
    complement_url = ""
    start_url = [base_url+complement_url]

    @abstractmethod
    def scrapear_pagina(self):
        pass

    @abstractmethod
    def set_complement(self, regex: str):
        pass

    def parse(self, response, **kwargs):
        pass
