from flask import Flask, send_file, make_response, request
from webscrape import present_prices
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        keyword = request.data
        priceElemsAmazon, priceElemsNike = present_prices(keyword)
    else:
        # response = make_response(send_file("templates/index.html"))
        # response.headers['keyword'] = 'priceElemsAmazon'
        # return response
        pass
    return send_file("templates/index.html")

if __name__ == "__main__":
    app.run(
          host="0.0.0.0",
        #   port=int("80")
    )
