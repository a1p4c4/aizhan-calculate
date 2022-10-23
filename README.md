# aizhan-calculate
A tool designed to calculate the right of a website(Aizhan api).
# Why
补天提交漏洞有网站权重要求，故写了个工具方便自己批量查询网站权重。
# How to use
## Step1🎈申请爱站私钥
到https://www.aizhan.com/user.php 去手动注册一个账号，api私钥是免费的，每次限额50个域名
![image](https://user-images.githubusercontent.com/59782799/197393769-ba200425-5667-4442-88b9-87042ebc8600.png)

## Step2🔔保存待查域名到urls.txt
注意：一定是网站的**根域名**，且不能包含类似 http:// 等协议名，否则可能查询失败
![image](https://user-images.githubusercontent.com/59782799/197393901-33236ebf-fec0-4150-8ac2-fa73e717cb47.png)

## Step3🧩python3 ./main.py
Now you got it!

![image](https://user-images.githubusercontent.com/59782799/197394054-9b069a86-6216-41c6-b192-1a7692e695bc.png)
