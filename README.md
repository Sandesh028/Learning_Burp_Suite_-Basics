# Learning_Burp_Suite_Basics
## Prerequisite
```sh
pip install Flask==2.1.3 Werkzeug==2.0.3
```

# 🔎 Part 1: Intercepting and Analyzing Traffic 
### Enable Interception
```
Open Burp Suite → Proxy tab → Intercept is ON.
Visit http://127.0.0.1:8080/ in a browser (Flask demo site).
Burp will capture the request; ask students to Forward it.
```
```Discussion Question: 
What do you see in the intercepted request?
```

### Inspect HTTP Requests
Go to HTTP history in the Proxy tab.
Click on a request (e.g., from /login form).
Explain HTTP methods (GET vs POST).
Show Headers, Parameters, Cookies.

## ✅ Hands-on Task:
To submit the login form with:
```
Username: admin
Password: password123
Observe how the credentials are passed.
```

# 🔎 Part 2: Modifying Requests 
###  Manipulating Parameters

- Open Burp → Proxy → Turn Intercept ON.
- Submit the login form, but change the request:
- Modify username=admin → username=hacker
- Modify password=password123 → password=1234
- Forward the modified request.


``` Discussion Question:
What happens if we change login details?
How can an attacker exploit this?
```

# 🔎 Part 3: Burp Suite Repeater

- Right-click on a login request → Send to Repeater.
- Go to Repeater Tab.
- Modify parameters (username=admin → username=hacker).
- Click Send.
- Observe the server response.


### ✅ Hands-on Task:

Try different usernames/passwords.
What happens if the server doesn’t validate login attempts properly?

# 🔎 Part 4: Burp Suite Intruder 

- Right-click on a login request → Send to Intruder.
- Go to Intruder → Positions tab.
- Mark username=admin and password=password123 as payload positions.
- Go to Payloads tab.
- Load a password list (e.g., rockyou.txt).
- Start the attack.
- Observe responses; if one returns 200 OK, the credentials are valid.

``` Discussion Question:
How can websites prevent brute force attacks?
```
# 🔎 Part 5: Real-World Applications & Security Fixes 

| Vulnerability            | How Burp Suite Demonstrates It                         | Prevention                                      |
|--------------------------|------------------------------------------------------|------------------------------------------------|
| Weak Authentication      | Modifying login requests                             | Enforce strong passwords, 2FA                 |
| Broken Access Control    | Changing URLs to access restricted pages             | Role-based access control (RBAC)              |
| SQL Injection           | Modifying form input (`admin' --`)                    | Input validation, parameterized queries       |
| Cross-Site Scripting (XSS) | Injecting `<script>alert('XSS')</script>` in a comment form | Input sanitization, Content Security Policy (CSP) |

✅ Hands-on Task:
To inject JavaScript into the comment box and see if it's executed.

## Where can you practice Burp Suite more?
- TryHackMe: https://tryhackme.com/room/burpsuitebasics
- PortSwigger Academy: https://portswigger.net/web-security
