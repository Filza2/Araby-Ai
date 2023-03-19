from requests import get,post
import re,os


# Araby Ai
# By @TweakPY - @vv1ck


def banner():
    os.system('cls' if os.name=='nt' else "clear");print('''
 █████╗ ██████╗  █████╗ ██████╗ ██╗   ██╗      █████╗ ██╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝     ██╔══██╗██║
███████║██████╔╝███████║██████╔╝ ╚████╔╝█████╗███████║██║
██╔══██║██╔══██╗██╔══██║██╔══██╗  ╚██╔╝ ╚════╝██╔══██║██║
██║  ██║██║  ██║██║  ██║██████╔╝   ██║        ██║  ██║██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝    ╚═╝        ╚═╝  ╚═╝╚═╝

            By @TweakPY - @vv1ck
''')
    
    
email='TweakPY@vv1ck.com' # Enter an email
password='Test123456789' # Enter a password

token=list()
    
'if the request respone is "" or { } or request status_code = 504 just change any letter in the auth'

def dashboardData():
    "Some general stats from the website"
    banner()
    
    r=get('http://gateway.api.production.araby.ai/dashboardData',headers={
        'Host': 'gateway.api.production.araby.ai',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        'Content-Length': '51',
        'Origin': 'https://araby.ai',
        'Referer': 'https://araby.ai/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Te': 'trailers',
        'Connection': 'close'
    })
    try:
        data=re.findall('{"_id":"(.*?)","count":(.*?)}',r.text)
        print(f'\n- Total users : {r.json()["total_users"]}')
        print(f'- Subscribed users : {r.json()["subscribed_users"]}')
        print(f'- Total images Generated : {r.json()["total_images_generated"]}')
        print(f'- Total Texts Generated : {r.json()["total_texts_generated"]}')
        for date,count in data:
            "Count of users who Joined on This Date"
            print(f'- Date : [ {date} ]\tcount : [ {count} ]')
        print('\n')
    except Exception as error:
        print('\nError : ',error)
    
def register():
    "A verification email will be sent, you must click on the link in it, then we will go to log in"
    banner()
    
    r=post('https://gateway.api.production.araby.ai/register',headers={
        'Host': 'gateway.api.production.araby.ai',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        'Content-Length': '51',
        'Origin': 'https://araby.ai',
        'Referer': 'https://araby.ai/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Te': 'trailers',
        'Connection': 'close'
    },
        data=f'email={email}&password={password}')
    
    if 'User registered successfully! Please verify your email.' in r.text:
        i=r.json()['User']
        print('\n- User registered successfully ! Please verify your email. ')
        print(f'- Name : {i["name"]} ')
        print(f'- ID : {i["_id"]} ')
        print(f'- Created At : {i["createdAt"]} \n')
    elif 'Email already exists' in r.text:
        print('\n- Error, This email is already linked to an account ')
    else:
        print(r.text)
        print('\n');exit()
        
def login():
    """
    The token that comes from the login is required for all the operations that you want to perform on the site. We will put it in the Authorization field in the headers
    Every account has one token !
    """
    banner()
    
    #https://gateway.api.production.araby.ai/autoLogin
    #GET Method, same headers but without data , the auto login only take token , its like a refresh thing 
    r=post('https://gateway.api.production.araby.ai/login',headers={
        'Host': 'gateway.api.production.araby.ai',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        'Content-Length': '51',
        'Origin': 'https://araby.ai',
        'Referer': 'https://araby.ai/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Te': 'trailers',
        'Connection': 'close'
    },
        data=f'email={email}&password={password}')
    if 'Authentication successful' in r.text:
        i=r.json()['User']
        token_p=r.json()["token"]
        print('\n- Authentication successful ! ')
        print(f'- ID : {i["_id"]} ')
        print(f'- Email verified at : {i["email_verified_at"]} ')
        print(f'- Created At : {i["createdAt"]} ')
        print(f'- Token : {token_p} \n')
        token.append(token_p)
    elif 'Failed to login. Please verify your email and try again.' in r.text:print('\n- Failed to login. Please verify your email and try again.');exit()
    else:
        print(r.text)
        print('\n');exit()
        
        
def generate_text_1(token_p,text,language):
    "Just a repeat for generate_text to help"
    banner()
    r=post('https://gateway.api.production.araby.ai/generate-text',headers={'Host': 'gateway.api.production.araby.ai','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0','Accept': 'application/json, text/plain, */*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/json','Authorization': token_p,'Origin': 'https://dashboard.araby.ai','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Te': 'trailers','Connection': 'close'},json={"useCase":"ProfileBio","tone":"Convincing","language":language,"inputs":[{"about":text}]})
    if 'No more text generation quota left' in r.text:print('\n- Error, No more text generation quota left ');print('- Change any letter in the Token !\n')
    elif r.status_code==504:print('\n- Error, No more text generation quota left ');print('- Change any letter in the Token !\n')
    else:
        data=re.findall('''{"finish_reason":"(.*?)","index":(.*?),"logprobs":(.*?),"performance_prediction":(.*?),"text":"(.*?)","word_count":(.*?)}''',r.text)
        print("𓐚"*50)
        try:
            for finish_reason,index,logprobs,performance_prediction,text,word_count in data:
                text=str(text).replace('\\n','\n')
                print(f'\nindex Number : {index}\nText : {text}\n{"𓐚"*50}')
            print('\n')
        except Exception as error:print('\nError : ',error)
def generate_text():
    """
    You Must run Login def to get the token and run this ,
    If your text or image limit has been reached you can change one letter in the token : Authorization ! , you can set the token to be random but I am telling you the right way to do things ,
    The AI will take some time to response.
    
    if the text is in AR language you must encode it before you send the request
    """
    banner()
    
    token_p=token[0]
    text='Tweakpy'     # put here the text you want the ai to generate " talk about your self or your channel & etc . " !
    language='English' # You can put here eng or ar i don't know about the other languages !
    
    
    r=post('https://gateway.api.production.araby.ai/generate-text',headers={
        'Host': 'gateway.api.production.araby.ai',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json',
        'Authorization': token_p,
        'Origin': 'https://dashboard.araby.ai',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Te': 'trailers',
        'Connection': 'close'
    },
        json={"useCase":"ProfileBio","tone":"Convincing","language":language,"inputs":[{"about":text}]}) # the tone is Convincing you can see a diffrent tone in the website to change 'Convincing'
    if 'No more text generation quota left' in r.text:
        token_p=str(token_p).replace('y','e').replace('J','a')
        generate_text_1(token_p,text,language)
    elif r.status_code==504:
        token_p=str(token_p).replace('y','e').replace('J','a')
        generate_text_1(token_p,text,language)
    else:
        data=re.findall('''{"finish_reason":"(.*?)","index":(.*?),"logprobs":(.*?),"performance_prediction":(.*?),"text":"(.*?)","word_count":(.*?)}''',r.text)
        print("𓐚"*50)
        try:
            for finish_reason,index,logprobs,performance_prediction,text,word_count in data:
                text=str(text).replace('\\n','\n')
                print(f'\nindex Number : {index}\nText : {text}\n{"𓐚"*50}')
            print('\n')
        except Exception as error:
            print('\nError : ',error)
            
            
def image_generate_1(token_p,text):
    "Just a repeat for image_generate to help"
    banner()
    r=post('https://gateway.api.production.araby.ai/image-gen',headers={'Host': 'gateway.api.production.araby.ai','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0','Accept': 'application/json, text/plain, */*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/json','Authorization': token_p,'Origin': 'https://dashboard.araby.ai','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Te': 'trailers','Connection': 'close'},json={"prompt":text,"image_size":"256x256","num_images":"1"})
    if 'No more image generation quota left' in r.text:print('\n- Error, No more text generation quota left ');print('- Change any letter in the Token !\n')
    elif r.status_code==504:print('\n- Error, No more text generation quota left ');print('- Change any letter in the Token !\n')
    else:
        data=re.findall('''"https://arabai-images.s3.me-south-1.amazonaws.com/(.*?)"''',r.text)
        print("𓐚"*50)
        try:
            i=0
            for url0 in data:
                i+=1
                url=f'https://arabai-images.s3.me-south-1.amazonaws.com/{url0}'
                print(f'- Image URL : {url} ')
                r2=get(url).content
                with open(f'Arab_Ai_Image_{i}.png','wb') as f:
                    f.write(r2)
            print('\n')
        except Exception as error:
            print('\nError : ',error)
def image_generate():
    """
    You Must run Login def to get the token and run this ,
    If your text or image limit has been reached you can change one letter in the token : Authorization ! , you can set the token to be random but I am telling you the right way to do things ,
    The AI will take some time to response.
    
    if the text is in AR language you must encode it before you send the request
    """
    banner()
    
    token_p=token[0]
    text='Tweakpy' # put here the text you want the ai to generate as image 

    r=post('https://gateway.api.production.araby.ai/image-gen',headers={
        'Host': 'gateway.api.production.araby.ai',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json',
        'Authorization': token_p,
        'Origin': 'https://dashboard.araby.ai',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Te': 'trailers',
        'Connection': 'close'
    },
        json={"prompt":text,"image_size":"256x256","num_images":"1"})
    if 'No more image generation quota left' in r.text:
        token_p=str(token_p).replace('y','e').replace('J','a')
        image_generate_1(token_p,text)  
    elif r.status_code==504:
        token_p=str(token_p).replace('y','e').replace('J','a')
        image_generate_1(token_p,text)
    else:
        data=re.findall('''"https://arabai-images.s3.me-south-1.amazonaws.com/(.*?)"''',r.text)
        print("𓐚"*50)
        try:
            i=0
            for url0 in data:
                i+=1
                url=f'https://arabai-images.s3.me-south-1.amazonaws.com/{url0}'
                print(f'- Image URL : {url} ')
                r2=get(url).content
                with open(f'Arab_Ai_Image_{i}.png','wb') as f:
                    f.write(r2)
            print('\n')
        except Exception as error:
            print('\nError : ',error)
    

def generate_code_1(token_p,text,codeLanguage):
    """Just a repeat for generate_code to help"""
    banner()
    r=post('https://gateway.api.production.araby.ai/generate-code',headers={'Host': 'gateway.api.production.araby.ai','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0','Accept': 'application/json, text/plain, */*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/json','Authorization': token_p,'Origin': 'https://dashboard.araby.ai','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Te': 'trailers','Connection': 'close'},json={"prompt":text,"codeLanguage":codeLanguage})
    if 'No more code generation quota left' in r.text:print('\n- Error, No more code generation quota left ');print('- Change any letter in the Token !\n') 
    elif r.status_code==504:print('\n- Error, No more code generation quota left ');print('- Change any letter in the Token !\n') 
    else:
        print("𓐚"*50)
        data=re.findall('''"text":"(.*?)"''',r.text)
        try:
            for code in data: 
                code=str(code).replace('\\n','\n').replace('\\',' ')
                print(code)
        except Exception as error:
            print('\nError : ',error)

def generate_code():
    """
    You Must run Login def to get the token and run this ,
    If your text or image limit has been reached you can change one letter in the token : Authorization ! , you can set the token to be random but I am telling you the right way to do things ,
    The AI will take some time to response.
    
    if the text is in AR language you must encode it before you send the request
    """
    banner()
    
    token_p=token[0]
    text='Tweakpy' # put here the text you want the ai to generate as code 
    codeLanguage='Python' # put here programming Language
    
    r=post('https://gateway.api.production.araby.ai/generate-code',headers={
        'Host': 'gateway.api.production.araby.ai',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json',
        'Authorization': token_p,
        'Origin': 'https://dashboard.araby.ai',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Te': 'trailers',
        'Connection': 'close'
    },
        json={"prompt":text,"codeLanguage":codeLanguage})
    if 'No more code generation quota left' in r.text:
        token_p=str(token_p).replace('y','e').replace('J','a')
        generate_code_1(token_p,text,codeLanguage)  
    elif r.status_code==504:
        token_p=str(token_p).replace('y','e').replace('J','a')
        generate_code_1(token_p,text,codeLanguage)  
    else:
        print("𓐚"*50)
        data=re.findall('''"text":"(.*?)"''',r.text)
        try:
            for code in data: 
                code=str(code).replace('\\n','\n').replace('\\',' ')
                print(code)
        except Exception as error:
            print('\nError : ',error)

def ArabyGPT_1(token_p,text):
    """Just a repeat for ArabyGPT to help"""
    banner()
    
    r=post('https://gateway.api.production.araby.ai/get-response',headers={'Host': 'gateway.api.production.araby.ai','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0','Accept': 'application/json, text/plain, */*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/json','Authorization': token_p,'Origin': 'https://dashboard.araby.ai','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Te': 'trailers','Connection': 'close'},json={"message":text,"history":[],"enable_google_data":""})
    if 'No more text generation quota left' in r.text:print('\n- Error, No more code generation quota left ');print('- Change any letter in the Token !\n') 
    elif r.status_code==504:print('\n- Error, No more text generation quota left ');print('- Change any letter in the Token !\n') 
    else:
        print("𓐚"*50)
        data=re.findall('''"text":"(.*?)"''',r.text)
        try:
            for text in data: 
                text=str(text).replace('\\n','\n').replace('\\',' ')
                print(text)
        except Exception as error:
            print('\nError : ',error)
            
            
def ArabyGPT():
    """
    You Must run Login def to get the token and run this ,
    If your text or image limit has been reached you can change one letter in the token : Authorization ! , you can set the token to be random but I am telling you the right way to do things ,
    The AI will take some time to response.
    
    if the text is in AR language you must encode it before you send the request
    """
    banner()
    
    token_p=token[0]
    text='Tweakpy' # put here the text you want the ai to generate as code 
    
    r=post('https://gateway.api.production.araby.ai/get-response',headers={
        'Host': 'gateway.api.production.araby.ai',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json',
        'Authorization': token_p,
        'Origin': 'https://dashboard.araby.ai',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Te': 'trailers',
        'Connection': 'close'
    },
        json={"message":text,"history":[],"enable_google_data":""})
    if 'No more text generation quota left' in r.text:
        token_p=str(token_p).replace('y','e').replace('J','a')
        ArabyGPT_1(token_p,text)  
    elif r.status_code==504:
        token_p=str(token_p).replace('y','e').replace('J','a')
        ArabyGPT_1(token_p,text)  
    else:
        print("𓐚"*50)
        data=re.findall('''"text":"(.*?)"''',r.text)
        try:
            for text in data: 
                text=str(text).replace('\\n','\n').replace('\\',' ')
                print(text)
        except Exception as error:
            print('\nError : ',error)

def ticket_crate():
    """
    POST /ticket/create HTTP/1.1
    Host: gateway.api.production.araby.ai
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0
    Accept: */*
    Accept-Language: ar,en-US;q=0.7,en;q=0.3
    Accept-Encoding: gzip, deflate
    Referer: https://dashboard.araby.ai/
    Authorization: auth
    Content-Type: application/json
    Content-Length: 70
    Origin: https://dashboard.araby.ai
    Sec-Fetch-Dest: empty
    Sec-Fetch-Mode: cors
    Sec-Fetch-Site: same-site
    Te: trailers
    Connection: closesssss
    
    {"name":"Null","email":"TweakPY@vv1ck.com","message":"Hi There"}
    """
    return 0
    
    
"""
1 - register()
2 - confirm Your email
3 - login()
4 - any thing you want
"""
#register()
#login()
