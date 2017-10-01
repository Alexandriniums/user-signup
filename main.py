# user must provide:
    # username
    # password (must verify pw in a 2nd field)
    # email address

from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<style>
    .error {{color: red; }}
</style>
    <h2>Signup</h2>
    <form action='/welcome' method=POST>
        <table>
            <tr>
                <td><label for="username" value="">Username:</label></td>
                <td><input type="text" id="username" name="username" value='{username}' /></td> <!-- username field: no spaces, > 3 and < 20 characters <p class=error>{{username_error}}</p>-->
                <td><p class="error">{username_err}</p></td>
            </tr>
            <tr>
                <td><label for="pw">Password:</label></td>
                <td><input type="password" id="pw" name="pw" value='{pw}' /></td> <!-- password field -->
                <td><p class="error">{pw_err}</p></td>
            </tr>
            <tr>
                <td><label for="pw-confirm">Confirm password:</label></td>
                <td><input type="password" id="pw-confirm" name="pw-confirm" value='{pw_confirm}' /></td> <!-- somehow validate pw: must match prior pw field -->
                <td><p class="error">{pw_confirm_err}</p></td>
            </tr>
            <tr>
                <td><label for="email">Email (optional):</label></td>
                <td><input type="text" id="email" name="email" value='{email}'/></td> <!-- email field: can be empty BUT if not, must have @ char and . char, no spaces, b/t 3020 char longd -->
            </tr>
        </table>
        <br>
            <input type="submit" />
    </form>
"""

@app.route('/')
def display_signup_form():
    return form.format(username='', username_err='', pw='', pw_err='', pw_confirm='', pw_confirm_err='', email='', email_err='')
#render_template('form.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    return '<h2>Welcome, ' + username + '!</h2>'

#@app.route('/', methods=['POST'])
#def validate_signup_form():
#    username = request.form['username']
#    pw = request.form['pw']
#    pw_confirm = request.form['pw-confirm']
#    email = request.form['email']

#    username_err = ''
#    pw_err = ''
#    pw_confirm_err = ''

app.run()