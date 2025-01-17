#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os, json

import cgitb

cgitb.enable()


def _wrapper(page):
    """
    Wraps some text in common HTML.
    """
    return (
        """
    <!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, sans-serif;
                max-width: 24em;
                margin: auto;
                color: #333;
                background-color: #fdfdfd
            }

            .spoilers {
                color: rgba(0,0,0,0); border-bottom: 1px dashed #ccc
            }
            .spoilers:hover {
                transition: color 250ms;
                color: rgba(36, 36, 36, 1)
            }

            label {
                display: flex;
                flex-direction: row;
            }

            label > span {
                flex: 0;
            }

            label> input {
                flex: 1;
            }

            button {
                font-size: larger;
                float: right;
                margin-top: 6px;
            }
        </style>
    </head>
    <body>
    """
        + page
        + """
    </body>
    </html>
    """
    )


def login_page():
    """
    Returns the HTML for the login page.
    """

    return _wrapper(
        r"""
    <h1> Welcome! </h1>

    <form method="POST" action="login.py">
        <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
        <label> <span>Password:</span> <input type="password" name="password"></label>

        <button type="submit"> Login! </button>
    </form>
    """
    )


print("Content-type:text/html\r\n\r\n")

print("<html>")
print("<body>")
# Q1

j = json.dumps(dict(os.environ), indent=4)
print(j)

print("<br>")
print("<br>")
print("<br>")
print(f"\n\n Query string is {os.environ.get('QUERY_STRING')}\n")
print("<br>")
print("<br>")
print("<br>")

# Q2

print(f'user brower is : {os.environ.get("HTTP_USER_AGENT")}')

print("<body>")


# Q4

print(login_page())

# Q6

items = os.environ.get("HTTP_COOKIE").split(";")

pairs = {}

for item in items:
    split = item.split("=")
    pairs[split[0].strip()] = split[1].strip()

print("<br>")

import secret


try:
    if pairs["username"] == secret.username and pairs["password"] == secret.password:
        import templates

        print("user is logged in <br><br>")
        print(templates.secret_page(pairs["username"], pairs["password"]))
except KeyError:
    print("user is not logged in <br><br>")


print("</html>")
