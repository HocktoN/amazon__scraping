import requests
from bs4 import BeautifulSoup 
import pandas as pd


"""

WEB SCRAPING


    """

def getData():
    URL = 'https://www.amazon.com.tr/s?k=apple&rh=n%3A12466496031%2Cn%3A26232650031&dc&ds=v1%3A24QIKEr1whZX7fY03aG1Rzroi24YQzoigI1WMNytis0&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=9UPC9JZMBEZY&qid=1658327018&rnid=13818411031&sprefix=appl%2Caps%2C122&ref=sr_nr_n_4'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'}
    sayfa = requests.get(URL, headers = headers)
    icerik = BeautifulSoup(sayfa.content,"lxml")
    ürün_adi =icerik.find_all("span", attrs = {"class":"a-size-base-plus a-color-base a-text-normal"})
    fiyat = icerik.find_all("span", attrs = {"class":"a-price-whole"})
    fiyat2 = icerik.find_all("span", attrs = {"class":"a-price-fraction"})
    
    urun_adi = []
    urun_fiyati=[]
    urun_kusurati = []
    tam_fiyat = []
    
    for i in ürün_adi:

        urun_adi.append(i.text)
    
    urun_adi.remove("Audio-Technica ATH-AR3ISWH taşınabilir on-Ear kulaklık Apple iOS için beyaz")
    for i in fiyat:
        urun_fiyati.append(i.text)
    for i in fiyat2:
        urun_kusurati.append(i.text)
        
    for i in range(len(urun_adi)):
        
        tam_fiyat.append(str(urun_fiyati[i]) + str(urun_kusurati[i]) + " TL")
        
    
    dicti = {'UrunAdi':urun_adi,'Fiyati':tam_fiyat}
    
    daf = pd.DataFrame(dicti)
    
    daf.to_csv("amazon.csv", index = False)
    
    # json_object = json.dumps(dicti, indent = 4) 
    
    # with open("sample.json", "w") as outfile:
    #     outfile.write(json_object)
    
    return daf
        
    
getData()