import cgi
import secret
import cgitb

cgitb.enable()

form = cgi.FieldStorage()


name = form["username"].value
password = form["password"].value


if name == secret.username and password == secret.password:
    print(
        f"Set-Cookie: username = {name};\r\n",
    )

    print(
        f"Set-Cookie: password = {password};\n\n",
    )

    # print("Content-type:text/html\r\n\r\n")
    # print("login success")
else:
    import templates

    # print("Content-type:text/html\r\n\r\n")
    print(templates.after_login_incorrect())
