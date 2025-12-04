import requests
import time


#
TOKEN = "Your_Telegram_Token"
turl = f"https://api.telegram.org/bot{TOKEN}/"

instructions = {
    '/start':"Just type in the ticker of any cryptocurrency coin listed on Binance to get the current price",
    "/help": "",

}

#function gets the message sent by a user from the bot

def get_userInput(offset=None):
    url = turl + "getUpdates"
    params = {"offset": offset}
    response = requests.get(url,params=params)
    data = response.json()

    return data


#function to get the current price of crypto 

def get_price(ticker):

    ticker = ticker.upper() + 'USDT'
    print(ticker)

    url = f"https://api.binance.com/api/v3/ticker/price?symbol={ticker}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return float(data['price'])
    else:
        return "Error"

#function to send a response back to the bot
def send_message(chat_id, text):
    url = turl + "sendMessage"
    params = {"chat_id": chat_id, "text": text}
    requests.get(url, params=params)





def main():

    last_update_id = None

    print("The Bot is running >>>>🤖<<<")

    while True:

        userMessage = get_userInput(last_update_id)

        try:


            if "result" in userMessage:

                for data in userMessage['result']:

                    user_input = data['message']['text']

                    chat_id = data["message"]["chat"]["id"]

                    update_id = data["update_id"]

                    last_update_id = update_id + 1

                    if user_input in instructions:
                        reply_text = instructions[user_input]
                        send_message(chat_id,reply_text)
            

                    else:
                        price = get_price(user_input)

                        if price == "Error":
                            reply_text = "An Error occured.. check what you typed!!!"
                            send_message(chat_id, reply_text)
                        else:

                            reply_text = f"The price of {user_input.upper()} is: ${price}"
                            send_message(chat_id, reply_text)

        except:

            print("system Error")


        
            
        
        
        time.sleep(1)


if __name__ == "__main__":
    main()