# Online-Bookstore
### An e-commerce web application to manage, add, remove, buy and sell books.

### 📌 Table of Contents
* [Toolchain](#toolchain)
* [Features](#features)
* [Application Overview](#overview)
* [Learnings](#learning)
* [Challenges faced](#challenges)
* [Future Scope/ What's next?](#scope)
* [Resources](#resources)
* [Setup](#setup)
* [Authors](#authors)
* [Bug Reporting](#bug)
* [Feature Requests](#feature-request)


<a id="toolchain"></a>
## 💻 Toolchain

<img alt="HTML" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/><img alt="CSS" src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"/><img alt="Javascript" src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/><img alt="Bootstrap" src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"/><img alt="Flask" src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/><img alt="SQLite" src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white" /><img alt="Visual Studio Code" src="https://img.shields.io/badge/VisualStudioCode-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/><img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>

***Frontend*** : HTML, CSS, JS, Bootstrap

***Backend*** : Flask, Jinja

***Dtabase*** : SQLite

***API*** : Razorpay

***Other*** : Git - Version Control, Visual Studio Code


<a id="features"></a>
## 🚀 Features
- Provides a web-based interface to search books based on titles or author's name. It displays information such as book title, book's author, description, price, genre, publishing year, and the number of books left in stock.
- User has to login into his/her account to buy a book. Users can buy books through multiple payment options provided. On a successful payment transaction, a receipt is sent to the user's email account.
- All online sales data are recorded in the database with timestamps. Users can view their order history and transactions.
- User can edit his/her account details as well as change password.
- Admin can add books/Users to the database and edit/delete them as per requirement.
- [Add more features](#feature-request)...

<a id="overview"></a>
## 📖 Application Overview
### Home Page
![Website Image](main/static/img/home.png?raw=true "Title")
### About Page 
![Website Image](main/static/img/about.png?raw=true "Title")
### Available Books 
![Website Image](main/static/img/all.png?raw=true "Title")
### Individual Book Page 
![Website Image](main/static/img/book_page.png?raw=true "Title")
### Offers
![Website Image](main/static/img/offers.png?raw=true "Title")
### Sales
![Website Image](main/static/img/sale.png?raw=true "Title")
### Contact Us Page 
![Website Image](main/static/img/contact_page.png?raw=true "Title")
### Register Page 
![Website Image](main/static/img/register.png?raw=true "Title")
### Login Page
![Website Image](main/static/img/login.png?raw=true "Title")
### Add Book Page 
![Website Image](main/static/img/add_book.png?raw=true "Title")
### Admin dashboard 
![Website Image](main/static/img/admin.png?raw=true "Title")
### Book Details in admin dashboard 
![Website Image](main/static/img/book.png?raw=true "Title")
### Account Page
![Website Image](main/static/img/account.png?raw=true "Title")

<a id="learning"></a>
## 💡 Learnings
- Enhancing designing and graphic skills by accomodating bootstrap library.
- To call Razorpay API and integrating payment gateway.
- Using multiple flask extension such as flask mail, flask admin, etc.

<a id="challenges"></a>
## 💡 Challenges faced
- Had technical setup issue while working with smtp requests using flask mail extenson.
- Integrating Razorpay API with the database so that amount of book becomes less after purchasing.
- Faced difficulty while designing admin dashboard with built-in styling.

<a id="scope"></a>
## 🚧 Future Scope/ What's next?
- [ ] Implementing offers and sales section on about page.
- [ ] Adding wishlist and cart feature in user's account.
- [ ] Adding tracking system for knowing the status of book delivery.
- [ ] Make website responsive for multiple devices and develop mobile application for the same.

<a id="resources"></a>
## 📚 Resources

- [HTML Documentation](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS Documentation](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [Tailwind CSS Cheat Sheet](https://nerdcave.com/tailwind-cheat-sheet)
- [JS Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Bootstrap Documentation](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Jinja Documentation](https://jinja.palletsprojects.com/en/3.0.x/)
- [Razorpay Documentation](https://razorpay.com/docs/payment-gateway/server-integration/python/)


<a id="setup"></a>
## ⚙️ Set Up

Take These Steps to configure the Project :

* Clone The Repository
```
git clone https://github.com/Pratyaksha-047/Online-Bookstore
```

* Create a virtual environment(Code is for Windows Only)
```
virtualenv venv 
```

* Download all required modules using
```
pip install -r requirements.txt
```

* Create database by running the following command using python in command prompt
```
from main import db
db.create_all()
exit()
```

*  Run the run.py file in command prompt 
```
python run.py
```
* Now Head on to ['http://127.0.0.1:5000/'](http://127.0.0.1:5000/)


<a id="authors"></a>
## 💻 Authors

Contributors names and contact info :

Punerva Singh<br> 
[@Linkedin](https://www.linkedin.com/in/punerva-singh-958305204)
<br>
[@Github](https://github.com/punervasingh)
<br>

Pratyaksha Gupta<br>
[@Linkedin](https://www.linkedin.com/in/pratyakshagupta-047/)
<br>
[@Github](https://github.com/Pratyaksha-047)
<br>

<a id="bug"></a>
## 🐛 Bug Reporting
Feel free to [open an issue](https://github.com/Pratyaksha-047/Online-Bookstore/issues) on GitHub if you find bugs.

<a id="feature-request"></a>
## ⭐ Feature Request
- Feel free to [open an issue](https://github.com/Pratyaksha-047/Online-Bookstore/issues) on GitHub to add any additional features you feel could enhance this project.  
