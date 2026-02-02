import os

from dotenv import load_dotenv

load_dotenv()


valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')

invalid_email = os.getenv('invalid_email')
invalid_password = os.getenv('invalid_password')

invalid_auth_key = {"key": "32dc0fd5f1b1277dd53193dbbc63b284d0b472335914325"}

name1 = 'Буся'
animal_type1 = 'Рэгдолл'
age1 = 1
pet_photo1 = 'images/рэгдолл.jpg'

name2 = 'Дуся'
animal_type2 = 'Мейн-кун'
age2 = 2
pet_photo2 = 'images/мейн-кун.jpg'

pet_photo3 = 'images/мейн-кун.webp'

name_simbols = '!"№%:,.;()'
name_numbers = '0123456789'
animal_type = 'неправильноимённый кот'
age = 0

name_empty = ''
animal_type3 = 'безымянный кот'
age3 = 3

name4 = 'безвозрастной кот'
age_empty = ''

animal_type4 = 'длинноименная кошка'
age4 = 4
name01 = 'c'
name255 = 'EcpGLvy88Jqz5f85wKkIzYYuXw988AD2BnCFCct5im87nlEbtTixCF1N7QQkBe6HDTDdPOZHmYy6TMy5YzTBAeMRmEc8SjCaWvZDoTOS1X6CT17gGOfPtYY4PbF2KLXE6Fwryr5KRGzjS1QHdUnTvWiuAeQL3Cp7k4o63ZRFsBRQrENKWmpojUN9IxFHGtxey1vWnFlRac2D2ti3oHsE4wSFTVDlgnxh8Z3PeWXqfqgX9mbItFypIp9BXM9tcbc'
name1001 = 'RUaM2gjjkQuO4AXs3TyvJuzGIH72Bf6nNTQiXAOzhvxgqfTCnUjJHBhWJcGVv5oeYtuJuOH7OlIHO7vz8Nu0tgYk64iUkP1aoDy4i0IDq0BNeGaUX1k2Gm5eHQrRgRwLnaJ2TUxiOuhavRwg1GGYMZ2hKsnsfzWXYTqYgy3xBTdh6CBYVfOLt1fWYWEAAoi85E9r9b8zPjZSjBsbnwgNcU7XO1PxCQ7e8gMkXbboTreRxyjxj1xoihZaNrnxeQnDj6kCieDEg6wZqqz6sK2nlmGItr3DOKndeXaoOEubT0i3pvBr0R7So3CENozFuA0IRRFUbspBJZSLT4x5w1nB68eNZbJrYSHpZIMHn1CntXPv1dzETEBOchZ1I82zEsiS53wwm8mOsqdbksi35lc4jIc2CWRdYbiQr4RYkFlZDcchgkiSYETjHu1DtAKtkHG6tXaRqSC6kMpN8EuDTIywFlctagEzInbM5caMwaVtdgl5XDdbnOIujZXxRvemcSwNI7GRM0Pj1isKRYLW2rtUQeoe0gEdD5aDIyWV5gTkls7PFzUy5JbuhqstcFvK7DUcZZccH8N0YlQ8U3EFXuNrvTsWOq4JG6DNP2LgecNwDmun72U49yPdEGST2HAmFiqJ43tEnAo7TI3KNTNGLVpbBQQ0rBpHrBkGOhRmo1XPTZo2FHPVwHFQcTb0kqkJzYfXyt29XDAkNBRRAtcRFvA1MBhroZ4yrMkNhfQkKETmgs9C47AiHLleDQMabn432Cw7eMlmoMzaVcnBKE7lo7s5wxqQ5o8xjjMSEX6krHJTbRSzcVNjrebYlebMwFKclr8PxIZ20yxIesOQtGAMvdoTtghS7mF3oTd6eK48ZUfZ19ai2JuAzSa6DPa4RghtSbkgodQyB62SnGEXqOtZ49cvkGjGpVw4ct5NgaVH5ZxA7bGEwCDoCOpWGh6VrJYdyxjX4GMwSU2jUKZd80h7Lpuw6Gvvpu9f4qyyh5pH2arqQ'