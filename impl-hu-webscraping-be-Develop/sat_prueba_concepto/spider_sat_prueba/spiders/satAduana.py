import scrapy
from fastapi import FastAPI
import os
import threading


app = FastAPI(title='PruebaSat',
              description='Esta es una prueba',
              version='1.0.3')

estatus = "----"

class SataduanaSpider(scrapy.Spider):
    name = 'satAduana'
    allowed_domains = ['pecem.mat.sat.gob.mx']
    basic_url = 'https://pecem.mat.sat.gob.mx/app/qr/ce/faces/pages/mobile/validadorqr.jsf?D1=16&D2=1&D3='
    complement_url = 'SATN20230104070092075171'
    print(basic_url+complement_url)
    start_urls = [basic_url+complement_url]


    def parse(self, response):

        """
        builder.get_num_integracion()
        builder.get_num_gafete()
        builder.get_datos_generales()
        builder.get_informacion_pedimento()
        builder.get_candados()

        ----
        builder.get_num_integracion().get_num_gafete().get_datos_generales().get_informacion_pedimento().get_candado().build()
        """
        box = response.xpath('//div')
        title = box.xpath('./ul/li/span[2]/text()').get()
        title_n_i  = box.xpath('./ul/li[1]/text()').getall()
        titleNI  = box.xpath('./ul/li[1]/text()').get()
        encabezados = title_n_i[1]
        #


        numeroIntegracion = box.xpath('./ul/li[2]/table/tbody/tr/td/text()').get()
        titleNGU = box.xpath('./ul[2]/li[1]/text()').get()
        numeroGafeteUnico = box.xpath('./ul[2]/li[2]/table/tbody/tr/td/text()').get()
        tDatosGeneralesConsultados = box.xpath('./ul[3]/li[1]/text()').get()
        datosGeneralesConsultados = box.xpath('./ul[3]/li[2]/table/tbody/tr[2]/td/text()').getall()


        #datosGeneralesConsultadosP2 = box.xpath('./ul[3]/li[2]/table/tbody/tr[2]/td/br/text()').get()
        #datosGeneralesConsultadosP3 = box.xpath('./ul[3]/li[2]/table/tbody/tr[2]/td/br[2]/text()').get()
        #datosGeneralesConsultados = datosGeneralesConsultadosP1 + ' ' + datosGeneralesConsultadosP2 + ' '+ datosGeneralesConsultadosP3


        prueba = box.xpath('./span[2]/text()').getall()
        yield {
            numeroIntegracion: datosGeneralesConsultados,
            #'/ntitle:': title,
            #'prueba': prueba,
            #titleNGU: numeroGafeteUnico,
            #tDatosGeneralesConsultados: datosGeneralesConsultados,
            #'tDatosGeneralesConsultados': datosGeneralesConsultados,
        }


#podemos implementar asi el ciclo solo cambiando
def comando(name:str):
    os.system(f"scrapy crawl {name} -o prueba.csv")

ob = SataduanaSpider()

#while !validadorEstatus.validar()
for i in range(1):

    comando(ob.name)
    time = threading.Timer(2, comando(ob.name))
    time.start()
"""
print(fEsto se ejecuta antes que la función f().
****
****    {estatus}
****
"")

with open('prueba.csv', 'r+') as f:
    readFile = f.read()
    spliteado = readFile.split(sep="***")
    print(spliteado[1])
"""



