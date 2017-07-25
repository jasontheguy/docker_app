from flask import Flask
import random

app = Flask(__name__)

images = ["https://www.google.com/imgres?imgurl=http%3A%2F%2F3.bp.blogspot.com%2F_SWF9i3Vzpac%2FTMfITNfhMmI%2FAAAAAAAAA2s%2FGdl2pxm1tGY%2Fs1600%2FTetsuo%2B-%2Bfrom%2BAkira.gif&imgrefurl=https%3A%2F%2Fwww.reddit.com%2Fr%2Fgifs%2Fcomments%2F2er59e%2Fthats_a_beautiful_rainbow%2F&docid=ahN691u7fQc3WM&tbnid=1Z0iezfdfme_XM%3A&vet=10ahUKEwiXzfnW66TVAhWE8YMKHVIYCsUQMwiTASgEMAQ..i&w=500&h=273&bih=602&biw=1356&q=akira%20.gif&ved=0ahUKEwiXzfnW66TVAhWE8YMKHVIYCsUQMwiTASgEMAQ&iact=mrc&uact=8"
,
"https://www.google.com/imgres?imgurl=https%3A%2F%2Fs-media-cache-ak0.pinimg.com%2Foriginals%2F44%2Fc1%2F85%2F44c1850f64ea52cd98d5b18fc0699942.gif&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F42010209002310254%2F&docid=_sK3n2btBsMocM&tbnid=5zbNjQ0yyAjugM%3A&vet=10ahUKEwiXzfnW66TVAhWE8YMKHVIYCsUQMwiSASgDMAM..i&w=500&h=281&bih=602&biw=1356&q=akira%20.gif&ved=0ahUKEwiXzfnW66TVAhWE8YMKHVIYCsUQMwiSASgDMAM&iact=mrc&uact=8"
,
"https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.warosu.org%2Fdata%2Ftg%2Fimg%2F0431%2F54%2F1445342174224.gif&imgrefurl=https%3A%2F%2Fwarosu.org%2Ftg%2Fthread%2F43154983&docid=JA54okjyPtorhM&tbnid=RdsQOCr5bPwS5M%3A&vet=10ahUKEwiXzfnW66TVAhWE8YMKHVIYCsUQMwi6ASggMCA..i&w=500&h=269&bih=602&biw=1356&q=akira%20.gif&ved=0ahUKEwiXzfnW66TVAhWE8YMKHVIYCsUQMwi6ASggMCA&iact=mrc&uact=8
"
]