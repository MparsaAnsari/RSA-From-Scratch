# RSA-From-Scratch
An implementation of the RSA cryptosystem from first principles, demonstrating foundational algorithms like Miller-Rabin, Karatsuba Multiplication, and the Extended Euclidean Algorithm.
RSA Encryption & Decryption Tool 
This project is a command-line implementation of the RSA (Rivest–Shamir–Adleman) cryptosystem in Python. It allows users to encrypt a text file by generating public/private keys and decrypt it back using the generated keys.
The core cryptographic algorithms are implemented from scratch, without relying on external libraries.
✨ Features & Algorithms Implemented
This project demonstrates a fundamental understanding of number theory and cryptographic algorithms by implementing the following from the ground up:
Key Generation:
Generates large prime numbers using a custom Miller-Rabin Primality Test.
Calculates n, phi(n), and the private key d.
Encryption/Decryption:
Uses Modular Exponentiation (Fast Powering) for efficient calculation of (a^n) mod m.
Advanced Algorithms:
Karatsuba Algorithm for fast multiplication of large numbers.
Extended Euclidean Algorithm to find the modular multiplicative inverse for calculating the private key.
🛠️ Technologies Used
Python 3 (No external libraries required)
🚀 How to Use
Encryption
Place the text you want to encrypt inside the text.txt file.
Run the RSA.py script:
python RSA.py


The script will perform the following actions:
Generate a new result.txt file containing the encrypted ciphertext.
Generate a new keys.txt file containing the generated public and private keys, along with p, q, and n.
Decryption
Open the result.txt file and copy the encrypted ciphertext.
Paste the ciphertext into the text.txt file, replacing its content.
Run the Decrypt.py script:
python Decrypt.py


The script will prompt you to enter the private key and the value of n. Copy these values from the keys.txt file.
Enter private key: [Paste your private key here]
Enter n: [Paste your n value here]


A new result.txt file will be created containing the original, decrypted text.
ابزار رمزنگاری و رمزگشایی RSA 
این پروژه یک پیاده‌سازی خط فرمان از سیستم رمزنگاری RSA (Rivest–Shamir–Adleman) با استفاده از پایتون است. این ابزار به کاربران اجازه می‌دهد تا یک فایل متنی را با تولید کلیدهای عمومی/خصوصی رمزنگاری کرده و سپس با استفاده از کلیدهای تولید شده، آن را رمزگشایی کنند.
الگوریتم‌های اصلی رمزنگاری در این پروژه از پایه و بدون اتکا به کتابخانه‌های خارجی پیاده‌سازی شده‌اند.
✨ ویژگی‌ها و الگوریتم‌های پیاده‌سازی شده
این پروژه نشان‌دهنده درک عمیق از نظریه اعداد و الگوریتم‌های رمزنگاری از طریق پیاده‌سازی موارد زیر است:
تولید کلید:
تولید اعداد اول بزرگ با استفاده از آزمون اول بودن میلر-رابین.
محاسبه n, phi(n) و کلید خصوصی d.
رمزنگاری و رمزگشایی:
استفاده از توان‌پیمانه‌ای سریع (Modular Exponentiation) برای محاسبه بهینه (a^n) mod m.
الگوریتم‌های پیشرفته:
الگوریتم کاراتسوبا برای ضرب سریع اعداد بزرگ.
الگوریتم تعمیم‌یافته اقلیدس برای یافتن وارون ضربی پیمانه‌ای جهت محاسبه کلید خصوصی.
🛠️ تکنولوژی‌های استفاده شده
پایتون ۳ (بدون نیاز به کتابخانه خارجی)
🚀 نحوه استفاده
رمزنگاری (Encryption)
۱. متنی که قصد رمز کردن آن را دارید، داخل فایل text.txt قرار دهید.
۲. اسکریپت RSA.py را اجرا کنید:
python RSA.py


۳. پس از اجرا، اسکریپت کارهای زیر را انجام می‌دهد:
یک فایل result.txt جدید حاوی متن رمزنگاری شده می‌سازد.
یک فایل keys.txt جدید حاوی کلیدهای عمومی و خصوصی، به همراه مقادیر p, q و n می‌سازد.
رمزگشایی (Decryption)
۱. فایل result.txt را باز کرده و متن رمز شده را کپی کنید.
۲. محتوای فایل text.txt را پاک کرده و متن رمز شده را در آن قرار دهید.
۳. اسکریپت Decrypt.py را اجرا کنید:
python Decrypt.py


۴. برنامه از شما می‌خواهد که کلید خصوصی و مقدار n را وارد کنید. این مقادیر را از فایل keys.txt کپی کنید.
Enter private key: [کلید خصوصی را اینجا وارد کنید]
Enter n: [مقدار n را اینجا وارد کنید]


۵. یک فایل result.txt جدید حاوی متن اصلی و رمزگشایی شده ایجاد خواهد شد.
