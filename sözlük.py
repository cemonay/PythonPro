onay_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
}

while True:
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

    if word in onay_dict:
        print(onay_dict[word])
    else:
        print("Bu kelime sözlüğümüzde yer almıyor.")
