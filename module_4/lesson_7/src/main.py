from flask import Flask

app = Flask(__name__)

@app.route('/<number_one>/<number_two>/<operation>')
def index(number_one: str, number_two: str, operation: str) -> str:
    
    number_one, number_two = float(number_one), float(number_two)
        
    if operation == 'add':
        return f'{number_one} + {number_two} = {number_one + number_two}'
        
    if operation == 'sub':
        return f'{number_one} - {number_two} = {number_one - number_two}'
        
    if operation == 'mul':
        return f'{number_one} * {number_two} = {number_one * number_two}'
        
    if operation == 'div':
        if number_two:
            return f'{number_one} / {number_two} = {number_one / number_two}'
        else:
            return 'Нельзя делить на ноль!'

if __name__ == '__main__':
    app.run()
    