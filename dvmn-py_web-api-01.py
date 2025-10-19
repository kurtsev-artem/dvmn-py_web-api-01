
import requests
   

def main():
    url_template = 'https://wttr.in/{}?nmMTqu&lang=ru'
    url = url_template.format('Лондон')
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)

    url = url_template.format('svo')
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)

    url = url_template.format('Череповец')
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)    

 
if __name__ == '__main__':
    main()    
