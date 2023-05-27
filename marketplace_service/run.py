from flask import Flask, render_template

from books_shared.utils import logger
from marketplace_service.clients.account import Client

app = Flask(__name__)


@app.route("/accounts")
def render_account_page():
    client = Client()
    return render_template('accounts.html', accounts=client.get_accounts())


if __name__ == '__main__':
    app.run(debug=True)
