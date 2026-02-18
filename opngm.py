import webbrowser
passw=202093884
title=5
tryy=int(input("enter password: "))
if passw==tryy:
    print("Login successful ","Opening...")
    webbrowser.open("spotify.com")
else:
    title=title-1
    print("You have",title,"attempts left")
    if title==0:
        print("Your password has been blocked.")
    wait=input("Press Enter to exit...")





