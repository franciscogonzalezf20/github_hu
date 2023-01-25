import scrapy
from fastapi import FastAPI


app = FastAPI(title='PruebaSat',
              description='Esta es una prueba',
              version='1.0.3')


estatus = "´´"

class SataduanaSpider(scrapy.Spider):
    name = 'satSegunda'
    allowed_domains = ['pecem.mat.sat.gob.mx']
    basic_url = 'https://pecem.mat.sat.gob.mx/app/qr/ce/faces/pages/mobile/validadorqr.jsf?D1=16&D2=1&D3='
    complement_url = '92075180'
    print(basic_url+complement_url)
    start_urls = [basic_url+complement_url]
    print(estatus)

    def parse(self, response):
        box = response.xpath('//div')


        titleNI = box.xpath('./ul/li[1]/text()').get()
        numeroIntegracion = box.xpath('./ul/li[2]/table/tbody/tr/td/text()').get()
        datosGeneralesConsultados = box.xpath('./ul[3]/li[2]/table/tbody/tr[2]/td/text()').getall()
        print(datosGeneralesConsultados)
        estatus = datosGeneralesConsultados


        yield {
            titleNI:numeroIntegracion,
            'datos Generales':datosGeneralesConsultados,
        }

