import email
import datetime
import wikipedia
import webbrowser
import calendar
import pywhatkit as kit
import pyttsx3 as tts
import os
import subprocess
import ctypes
import random
import pyjokes
import requests
from requests import get
import IP2Location
import openai
from bs4 import BeautifulSoup
import notification
import eel

  

api_key = "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"
lang = 'en'
openai.api_key = api_key
def wishMe():
      hour = int(datetime.datetime.now().hour)
      if hour>=0 and hour<12:
          speak("Good Morning!")
      
      elif hour>=12 and hour<18:
          speak("Good Afternoon!")

      else:
        speak("Good Evening!")
      speak("hellow Mr. Nilanjan,i am star , how can i help you sir ")
def create_note_file(note, file_path):
    with open(file_path, "a") as f:
        f.write(note + "\n")




if __name__ == '__main__':
        wishMe()
        while True:
        #if 2:
            query = takecommand().lower()
            #logic for
            if 'wikipedia' in query:
                speak('searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to Wikipedia")
                print(results)
                speak(results)
  # Open AI
            elif "star" in query:
                new_string = query.replace("star", "")
                print(new_string)
                completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": new_string}])
                text = completion.choices[0].message.content
                speak(text)



            elif "help" in query:
                speak("I can help you with the following tasks:")
                speak("1. Make a note")
                speak("2. Save another note")
                speak("3. Say 'suck' if you are frustrated")
                speak("4. Say 'star' to get a random response")
                speak("5. Say 'help' to get a list of tasks")
                speak("6. Say 'exit' to end the program")
            elif "suck" in query:
                speak("I'm sorry you are frustrated")
                speak("I'll do my best to help you")
            
            
            # elif"note" in query:
            #     print("Opening note")
            #     speak("What would you like to make a note about")
            #     note_audio=r.listen(source)
            #     query =r.recognize_google(note_audio, language='en-in')
            #     print("Note saved")
            #     speak("Note saved successfully.")
            #     file_path = os.path.expanduser("~/Desktop/note.txt")
            #     create_note_file(query, file_path)

            elif "screenshot" in query:
                print("Getting the screenshot")
                screenshot_dir = os.path.expanduser("~/Desktop")
                file_name = "screenshot"
                extension = ".png"
                file_path = os.path.join(screenshot_dir, file_name + extension)
            
            
            # elif 'search' in query:
            #  speak('What do you want to search for?')
            #  search = takecommand()
            #  url = ('https://google.com/search?q=' + search)
            #  webbrowser.get('chrome').open_new_tab(url)
            #  speak('Here is What I found for' + search)

            elif 'open calendar'in query:
             now = datetime.datetime.now()
             print(calendar.month(int(now.strftime("%Y")), int(now.strftime("%m"))))
             #print(calendar.calendar(int(now.strftime("%Y"))))
            
            
            # elif "date" in query:
            #   date = datetime.datetime
            #   final_date = date.date()
            #   print(f"\nSir, today's date is {final_date}")
            #   speak("Sir, today's date is {final_date}")
            
            
            #elif 'time' in query:


            elif 'who am I' in query or 'what is my name' in query:
                print("\n yeor name Mr.Nilanjan Nayak , he is a grate man.")
                speak("yeor name Mr.Nilanjan Nayak , he is a grate man.")
            elif 'are you single' in query:
                print('\nI don\'t have personal life. But I can tell you about other people.')
                speak("I don't have personal life. But I can tell you about other people.")
            elif 'how old are you?' in query:
             age = "1 month old."
             print(age)
             speak(age)
            elif 'wake up' in query:
                music_dr = 'C:\\Users\\nilan\\Music\\kgf'
                songs = os.listdir(music_dr)
                print(songs)
                os.startfile(os.path.join(music_dr,songs[0]))
             
            elif 'open youtube' in query:
             webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open facebook' in query:
                webbrowser.open("facebook.com")
            elif 'open whatsapp' in query:
                webbrowser.open("whatsapp.com")
            elif "open instagram" in query:
                print("\nOpened Instagram")
                speak("Opened Instagram")
                webbrowser.open("https://instagram.com")
            elif "open twitter" in query:
                 print("\nOpened Twitter")
                 speak("Opened Twitter")
                 webbrowser.open("https://twitter.com")
            elif "open reddit" in query:
                 print("\nOpened Reddit")
                 speak("Opened Reddit")
                 webbrowser.open("https://reddit.com")
            elif "open pinterest" in query:
                    print("\nOpened Pinterest")
                    speak("Opened Pinterest")
                    webbrowser.open("https://pinterest.com")
            elif "open github" in query:
                    print("\nOpened GitHub")
                    speak("Opened GitHub")
                    webbrowser.open("https://github.com")
            elif "open netlify" in query:
                    print("\nOpened Netlify")
                    speak("Opened Netlify")
                    webbrowser.open("https://netlify.com")
            elif "open vs code" in query or "open code" in query:
            # Paste the VS Code's path which is in your system
                path = ("C:\\Users\\nilan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code")
                os.startfile(filepath=path)
                print("\nOpened Visual Studio Code")
                speak("Opened Visual Studio Code")
            elif "exit" in query:
             print("\nYou can call me again at any time, Bye Sir")
             speak("You can call me again at any time, Bye Sir")
             exit()
            elif "shutdown system" in query:
                subprocess.call(["shutdown", "/h"])
            elif 'shutdown system' in query:
             print("Shutting down the system")
             os.system("sudo shutdown -h now")
    
            elif'play video' in query:
                In  = input("search for youtube videos: ")
                input = speak("search for youtube videos: ")
                webbrowser.open("https://www.youtube.com/results?search_query=" +In)
                v =  tts.init()
                v.say(In)
                v.runAnwait()
            
            
            elif 'calculator' in query:
                print('\nRunning Calculator Mode\n')
                speak('Running Calculator Mode')
                from calculator import *
            elif 'youtube downloader' in query:
             exec(open('youtube_downloader.py').read())
            elif 'CPU' in query:
              os.cpu_count()
            elif 'joke' in query:
             joke = pyjokes.get_joke(category='all', type='single')
             print(joke)
             speak(joke)
            elif 'phone track' in query:
                print("\nopen phone tracker\n")            
                speak("phone tracker mode on")
                from phonetrack import *
            
   
   
    # IPL Score
            elif "cricket score" in query:
                    url="https://www.cricbuzz.com/"
                    page=requests.get(url)
                    soup=BeautifulSoup(page.text,"html.parser")
                    team1=soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2=soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score=soup.find_all(class_="cb-ovr-flo")[8].get_text()
                    team2_score=soup.find_all(class_="cb-ovr-flo")[10].get_text()
                    a=print(f"{team1} : {team1_score}")
                    b=print(f"{team2} : {team2_score}")
                    notification.notify(
                        title="Cricket Score",
                        message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        # timeout=10
                        )
    
    
    
     # Play Song
            elif "tired" in query:
                    speak("Playing your favourite song")
                    a = (1, 2, 3)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open("https://youtu.be/4mLAIoqLYuQ")
                    elif b == 2:
                        webbrowser.open("https://youtu.be/h1PMLoiiliA")
                    elif b == 3:
                        webbrowser.open("https://youtu.be/7I_sq3umvQc")
           
           
           
           
            # elif'weather' in query:
              
            def truncate(number, digits) -> float:
                    stepper = 10.0 ** digits
                    return math.trunc(stepper * number) / stepper

            def get_weather(city_name, api_key):
                    base_url = "https://api.openweathermap.org/data/3.0/onecall?"
                    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                    response = requests.get(complete_url)
                    data = response.json()
                    if data["cod"] != "404":
                        main = data["main"]
                        current_temperature = main["temp"]
                        current_pressure = main["pressure"]
                        current_humidiy = main["humidity"]
                        weather = data["weather"]
                        weather_description = weather[0]["description"]
                        celsius = current_temperature - 273.15
                        fahrenheit = celsius * 9 / 5 + 32
                        print("Temperature in Celsius = " + str(truncate(celsius, 2)) + " degree celsius")
                        print("Temperature in Farenheit = " + str(truncate(fahrenheit, 2)) + " degree farenheit")
                        print("Atmospheric pressure = " + str(current_pressure) + " mb")
                        print("Humidity = " + str(current_humidiy) + " %")
                        print("Description = " + str(weather_description))
                        print("")
                    else:
                        print("City Not Found. Please try again.")

            def get_input():
                    print("Weather in Birshibpur")
                    city_name = 'Birshibpur'
                    api_key = "a2d0b5283f2eaeb9b6c7794b97daaa5d"
                    get_weather(city_name, api_key)
                    get_input()
                            


            


                
                # images = os.listdir("C:\\Users\\joels\\Desktop\\Wallpapers")
                # imagePath = f"C:\\Users\\joels\\Desktop\\Wallpapers\\{random.choice(images)}"
                # def changeBG(imagePath):
                #     SPI_SETDESKWALLPAPER = 20
                #     ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imagePath , 0)
                #     return;
                # changeBG(imagePath)
                # print ("\nChanged Wallpaper Successfully!")
                # speak("Changed Wallpaper Successfully!")
                # except Exception as e:
                # print(str(e))

            # elif 'weather' in query:
            #     api_key = "64d95f718a0c4bebbe37660d95b213"
            #     ip = get('https://api.ipify.org').text
                
            #     database = IP2Location.IP2Location(os.path.join("data", "IPV4-COUNTRY.BIN"))
            #     rec = database.get_all(ip)

            #     print(rec.country_short)
            #     print(rec.country_long)
            #     print(rec.region)
            #     print(rec.city)
            #     print(rec.isp)  
            #     print(rec.latitude)
            #     print(rec.longitude)            
            #     print(rec.domain)
            #     print(rec.zipcode)
            #     print(rec.timezone)
            #     print(rec.netspeed)
            #     print(rec.idd_code)
            #     print(rec.area_code)
            #     print(rec.weather_code)
            #     print(rec.weather_name)
            #     print(rec.mcc)
            #     print(rec.mnc)
            #     print(rec.mobile_brand)
            #     print(rec.elevation)
            #     print(rec.usage_type)


               
               
               
                




