# akhbaar padke dikhao
# api key = your api key

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
    
if __name__ == "__main__":
    import requests
    import json
    
    print("Enter category:\n1. business\n2. entertainment\n3. health \n4. science\n5. sports\n6. technology")
    category = input()
    api_key = input("Enter your api_key: ")
    r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={api_key}").text
    # news = r.text
    parsed = json.loads(r)
    for i in range(0,10):
        speak(f"News {i+1}")
        print(parsed["articles"][i]["title"])
        speak(parsed["articles"][i]["title"])
        print("for more",parsed["articles"][i]["url"])
