import pytest
import main

   """
   If you need you can edit this tests to facilitate your work...
   """


def test_sendRequest():
   """
   Test the sendRequest function
   """
   try:
      r = main.requests.get(main.URL_GET + 'AAAAAA')
      assert type(r) == main.requests.Response
   except main.requests.RequestException as e:
        assert False, f"Request exception occurred: {e}"  

def test_readWordList():
   """
   Test the readWordList function
   """
   wordlist = main.readWordList('wordlist_test.txt')
   assert type(wordlist) == list




