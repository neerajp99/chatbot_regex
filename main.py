import re 
from textblob import TextBlob

# Function to fetch details of bank account
def account(val):
    if re.search('balance', val) or re.search(r'remain[ing]*', val) or re.search(r'available', val) or re.search(r'money.*bank', val) or re.search(r'bank.*money', val):
        # Credit or debit transactions
        if re.search('transactions?', val) or re.search('settlem?e?n?t?', val) or re.search(r'last.*[time]*.*spend?t?', val):
            if re.search(r'.*debite?d?', val) or re.search(r'spent?d?', val) or re.search(r'deduced?', val) or re.search(r'deducte?d?', val) or re.search(r'withdrawn?', val) or re.search(r'last.*debit.*transactions?', val) or re.search(r'removed?', val) or re.search('last.*remove?a?l?', val) or re.search(r'last.*spend?t?', val):  
                print('BOT: Your last debit transaction is for $220 at Costco.')
                return
            elif re.search(r'.*credite?d?', val) or re.search(r'added', val) or re.search(r'include?d?', val) or re.search(r'last.*credit.*transactions?', val) or re.search(r'inserte?d?', val) or re.search('last.*attache?d?', val) or re.search(r'last.*received?', val): 
                print('BOT: Your last credit transaction is $450 from Mr.James Powell')
                return
        else:
            print("BOT: Your Bank balance is $2089.")
            return
    # Credit Transactions 
    elif re.search(r'.*debite?d?', val) or re.search(r'spent?d?', val) or re.search(r'deduced?', val) or re.search(r'deducte?d?', val) or re.search(r'withdrawn?', val) or re.search(r'last.*debit.*transactions?', val) or re.search(r'removed?', val) or re.search('last.*remove?a?l?', val) or re.search(r'last.*spend?t?', val):  
        print('BOT: Your last debit transaction is for $220 at Costco.')
        return
    # Debit Transactions
    elif re.search(r'.*credite?d?', val) or re.search(r'added', val) or re.search(r'include?d?', val) or re.search(r'last.*credit.*transactions?', val) or re.search(r'inserte?d?', val) or re.search('last.*attache?d?', val) or re.search(r'last.*received?', val): 
        print('BOT: Your last credit transaction is $450 from Mr.James Powell')
        return
    else:
        print('BOT: I can’t answer that. Please contact the branch.')
        return

# Function to fetch details from credit card
def credit(val):
    if re.search(r'due', val) or re.search(r'remaining.*payment', val) or re.search(r'payment.*remaining', val) or re.search(r'amount.*due', val) or re.search(r'due.*amount', val) or re.search(r'amount.*[to]*.*pay?i?d?.*someone', val) or re.search(r'money.*due', val) or re.search(r'owe?', val):
        print('BOT: You have $150 due at Walmart')
        return
    elif re.search(r'outstanding', val) or re.search(r'pending.*payment', val) or re.search(r'payment.*pending', val) or re.search(r'pending.*amount', val) or re.search(r'amount.*pending', val) or re.search(r'[money]*.*[pending]*[remaining]*', val) or re.search(r'[pending]*[remaining]*.*money', val) or re.search(r'ongoing.*due', val) or re.search(r'incomplete.*payment', val) or re.search(r'payment.*incomplete.*[bank]*', val) or re.search(r'owe.*bank', val) or re.search(r'.*unpaid', val) or re.search(r'[to]*.*bank', val) or re.search(r'unfinishe?d?.*[payment]*', val) or re.search(r'to.*pay?i?d?', val):
        print("BOT: Your current outstanding amount to the bank is $380 on September 06, 2020")
        return
    else:
        print('BOT: I can’t answer that. Please contact the branch.')
        return

if __name__ == '__main__':
    print('BOT: Hello there! How may I help you today?')
    count = 0
    while True:
        if count == 0:
            val = input()
        else: 
            val = ""
            cond_prompt = input('BOT: Do you need any further help? \n').lower()
            if re.search(r'[Yy][eu]s', cond_prompt) or re.search(r'[Yy]eah', cond_prompt) or re.search(r'^y', cond_prompt) or re.search(r'[Yy][aeup]', cond_prompt):
                val = input("BOT: What can I help you with? \n")
            elif re.search(r'[Nn]o', cond_prompt) or re.search(r'[Nn]o[pe?]*', cond_prompt):
                print('BOT: Thank You for choosing our service!')
                break
            else:
                print('Sorry, I didn\'t understand')
                pass
        # Removing any special character which is not required 
        val = re.sub('[^a-zA-Z0-9 \n\.]', '', val)
        
        # Correcting spelling and converting to lowercase
        val = str(TextBlob(val).correct()).lower()
        if 'created' in val:
            val = val.replace('created', 'credited')
        if re.search('[Aa]ccount', val) or re.search('[Bb]ank', val):
            if re.search(r'creditcard', val) or re.search(r'[Cc]redit.*card', val):
                credit(val)
            else:
                incorrect_count = 0
                while True:
                    if incorrect_count <= 5:
                        ac = input('Kindly enter your bank account number (format: ABC123456789DE):')
                        if re.search(r'[A-Za-z][A-Za-z][A-Za-z]\d\d\d\d\d\d\d\d\d[A-Za-z][A-Za-z]', ac):
                            account(val)
                            break
                        else:
                            print('Incorrect account number, try again!')
                            incorrect_count += 1
                    else:
                        print('Sorry, too many incorrect account numbers...')
                        break  
        elif re.search(r'creditcard', val) or re.search(r'credit.*card', val):
            credit(val)
        else:
             print('BOT: I can’t answer that. Please contact the branch.')
        count += 1

