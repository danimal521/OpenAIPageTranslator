import requests
from openai import AzureOpenAI

url = 'https:///'
response = requests.get(url)

html_content = response.text

with open('en.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

client = AzureOpenAI(
  azure_endpoint = "https://.openai.azure.com/", 
  api_key="",  
  api_version="2024-02-15-preview"
)

filEN = open('en.html', 'r', encoding='utf-8')
Lines = filEN.readlines()
count = 0
for line in Lines:
    count += 1

    str = "translate the below text in this html to spanish only return the html: " + line

    response = client.chat.completions.create(
    model="gpt-35-turbo-16k",
    messages = [{"role":"system", "content":"You are a language translator."},
               {"role":"user","content":""+str+""},])

    strOut = response.choices[0].message.content

    with open('sp.html', 'a+') as file:
        file.write(strOut)


  


