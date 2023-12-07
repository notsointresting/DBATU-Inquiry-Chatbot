# Ideas for improvement (Final Approach)

---

### Avoiding Unrelated Questions!

- Actually, when user gives any query not related to university, Chatbot still answers the query. So to eliminate that i am thinking to add ML model to check whether it’s related to University or not.
- But Problem is, If i implement ML model, It will increase time complexity of overall project and make it more time consuming.
- Alternatively, i can use hard coded codes, and simply call them whenever user enters query, and it will check does it related to university or not, and additionally it will also check in conversational chain. Does user mentioned university earlier in conversation or not.

---

### Where we can use this chatbot

- I am considering implementing this on WhatsApp with the help of Twilio. However, I am unsure if it will work or not. We won't know unless we try. Therefore, I plan to implement it after all the necessary improvements have been made.
- I am familiar with Telegram bots because I have used them in previous projects. They are free to use and easy to implement. The only drawback is that not all students have Telegram. The Telegram bot is my second approach.
- The best place to interact with a chatbot is on a website. Many websites have their own chatbot services. Similarly, we can implement this on a specific site. I am thinking of using Flask for that. It's the third approach; first, I will try it on WhatsApp.
    - Cons: i) Development Effort (ii) Traffic

---

Feel free to edit this file, and if you have any ideas for improvement, please share them. Your suggestions are highly valued!

###Replace This with Your idea’s Name

- [Add Points]