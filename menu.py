import smtplib, ssl
from email.message import EmailMessage
import requests
from twilio.rest import Client
import tweepy
from instagrapi import Client
import pywhatkit

# ---------------- EMAIL ----------------
def send_email():
    sender = "your_email@gmail.com"
    password = "your_app_password"
    receiver = "receiver@example.com"

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = "Hello from Python"
    msg.set_content("This is a test email from menu-driven project ✅")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)
    print("✅ Email sent successfully!")

# ---------------- SMS ----------------
def send_sms():
    account_sid = "your_twilio_sid"
    auth_token = "your_twilio_auth_token"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hello from Python menu project 🚀",
        from_="+1234567890",   # Your Twilio number
        to="+919876543210"
    )
    print("✅ SMS sent successfully! SID:", message.sid)

# ---------------- PHONE CALL ----------------
def make_call():
    account_sid = "your_twilio_sid"
    auth_token = "your_twilio_auth_token"
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        twiml='<Response><Say>Hello! This is an automated Python call.</Say></Response>',
        from_="+1234567890",
        to="+919876543210"
    )
    print("✅ Call initiated! SID:", call.sid)

# ---------------- LINKEDIN ----------------
def post_linkedin():
    ACCESS_TOKEN = "your_linkedin_access_token"
    AUTHOR_URN = "urn:li:person:your_profile_id"

    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }
    post_data = {
        "author": AUTHOR_URN,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": "Hello LinkedIn! 🚀 Posted using Python"},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }
    r = requests.post(url, headers=headers, json=post_data)
    print("✅ LinkedIn response:", r.json())

# ---------------- TWITTER (X) ----------------
def post_twitter():
    API_KEY = "your_api_key"
    API_SECRET = "your_api_secret"
    ACCESS_TOKEN = "your_access_token"
    ACCESS_SECRET = "your_access_secret"

    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    api.update_status("Hello Twitter (X)! 🚀 Automated post from Python.")
    print("✅ Tweet posted successfully!")

# ---------------- FACEBOOK ----------------
def post_facebook():
    PAGE_ID = "your_page_id"
    ACCESS_TOKEN = "your_page_access_token"

    url = f"https://graph.facebook.com/{PAGE_ID}/feed"
    payload = {"message": "Hello Facebook! 🚀 Posted using Python."}

    r = requests.post(url, data=payload, params={"access_token": ACCESS_TOKEN})
    print("✅ Facebook response:", r.json())

# ---------------- INSTAGRAM ----------------
def post_instagram():
    # Create a Client object
  client = Client()
  
  # Take user input for Instagram credentials and photo details
  username = input("Enter your Instagram username: ")
  password = input("Enter your Instagram password: ")
  photo_path = input("Enter the path to the photo you want to upload: ")
  caption = input("Enter the caption for your photo: ")
  
  # Log in to your Instagram account
  try:
      client.login(username, password)
      print("Logged in successfully.")
  except Exception as e:
      print(f"Failed to log in: {e}")
      exit()  # Exit if login fails
  
  # Upload the photo and get its media ID
  try:
      media_id = client.photo_upload(photo_path, caption=caption).pk
      print(f"Photo uploaded successfully with media ID: {media_id}")
  except Exception as e:
      print(f"Failed to upload photo: {e}")
def send_whatsapp():
    number = input("Enter recipient number (with country code, e.g. +919876543210): ")
    message = input("Enter message: ")
    hour = int(input("Enter hour (24-hour format): "))
    minute = int(input("Enter minute: "))

    try:
        pywhatkit.sendwhatmsg(number, message, hour, minute)
        print("✅ WhatsApp message scheduled!")
    except Exception as e:
        print("❌ Error:", e)
# ---------------- MAIN MENU ----------------
def menu():
    while True:
        print("\n===== Python Automation Menu =====")
        print("1. Send Email")
        print("2. Send SMS")
        print("3. Make Phone Call")
        print("4. Post on LinkedIn")
        print("5. Post on Twitter (X)")
        print("6. Post on Facebook")
        print("7. Post on Instagram")
        print("8. Send WhatsApp Message")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            send_email()
        elif choice == "2":
            send_sms()
        elif choice == "3":
            make_call()
        elif choice == "4":
            post_linkedin()
        elif choice == "5":
            post_twitter()
        elif choice == "6":
            post_facebook()
        elif choice == "7":
            post_instagram()
        elif choice == "8":
            send_whatsapp()

        elif choice == "0":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    menu()
