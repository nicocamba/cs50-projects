import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
from datetime import datetime

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    compras_user = db.execute("SELECT symbol, SUM(shares) AS shares, prices FROM compras WHERE user_id = ? GROUP BY symbol", user_id)
    cash_user = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash_user_real = cash_user[0]["cash"]
    return render_template("index.html", data = compras_user, cash_user_real = cash_user_real)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    else:

        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Write a symbol")
        ##Buscamos la acción con la función ya implementada
        accion = lookup(symbol.upper())

        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("Shares must be countable")

        if not accion:
            return apology("The symbol does not exist")

        if shares < 0:
            return apology("Shares must be positive")

        value = shares * accion["price"]

        user_id = session["user_id"]
        user_money = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        user_money_number = int(user_money[0]["cash"])

        if user_money_number < value:
            return apology("Need more money in the wallet")

        ##Queremos ahora registrar la transacción sustrayendo el dinero al usuario

        new_user_cash = usd(user_money_number - value)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_user_cash, user_id)
        ##Usamos la funcion datetime implementada en helpers.py para recoger la fecha de la transaccion
        date = datetime.now()
        db.execute("INSERT INTO compras (user_id, symbol, shares, prices, date) VALUES(?, ?, ?, ?, ?)", user_id, accion["symbol"], shares, usd(accion["price"]), date)
        flash("Done")
        return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    datos_compras = db.execute("SELECT * FROM compras WHERE user_id = ?", user_id)
    return render_template("history.html", compras = datos_compras)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Write a symbol")
        ##Buscamos la acción con la función ya implementada
        accion = lookup(symbol)

        if not accion:
            return apology("The symbol does not exist")

        return render_template("/quoted.html", name = accion["name"], price = usd(accion["price"]), symbol = accion["symbol"])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Write a username")

        if not password:
            return apology("Write a password")

        if not confirmation:
            return apology("Repeat the password")

        if password != confirmation:
            return apology("Password and confirmation must be the same")

        pass_cifrado = generate_password_hash(password)
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, pass_cifrado)
        except:
            return apology("Failure(Username not valid)")
        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        user_id = session["user_id"]
        possible_sym = db.execute("SELECT symbol FROM compras WHERE user_id = ? GROUP BY symbol", user_id)
        return render_template("sell.html", symbol_todos = [row["symbol"] for row in possible_sym])
    else:
        user_id = session["user_id"]
        shares = int(request.form.get("shares"))
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Write a symbol")
        ##Buscamos la acción con la función ya implementada
        accion = lookup(symbol)

        if accion == None:
            return apology("The symbol does not exist")

        if shares < 0:
            return apology("Shares must be positive")

        value = shares * accion["price"]
        user_id = session["user_id"]
        user_money = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        user_money_number = user_money[0]["cash"]

        user_shares = db.execute("SELECT shares FROM compras WHERE user_id = ? AND symbol = ? GROUP BY symbol", user_id, symbol)
        user_shares_real = user_shares[0]["shares"]

        if shares > user_shares_real:
            return apology("Not enough shares")

        ##Queremos ahora registrar la transacción sumando el dinero al usuario

        new_user_cash = user_money_number + value
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_user_cash, user_id)
        ##Usamos la funcion datetime implementada en helpers.py para recoger la fecha de la transaccion
        date = datetime.datetime.now()
        db.execute("INSERT INTO compras (user_id, symbol, (-1)*shares, prices, date) VALUES(?, ?, ?, ?, ?)", user_id, accion["symbol"], shares, accion["prices"], date)
        flash("Done")
        return redirect("/")


