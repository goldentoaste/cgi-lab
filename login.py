import cgi
import secret
from http import cookies


form = cgi.FieldStorage()


name = form["username"].value
password = form["password"].value


if name == secret.username and password == secret.password:

    # cookie = cookies.SimpleCookie()

    # cookie["username"] = name
    # cookie["password"] = password
    # print(cookie)

    print(
        f"Set-Cookie: username = {name}\r\nSet-Cookie: password = {password}",
    )

    print("Content-type:text/html\r\n\r\n")
    print("login success")


else:
    import templates

    # print("Content-type:text/html\r\n\r\n")
    print(templates.after_login_incorrect())
