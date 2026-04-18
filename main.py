class Sonlar:
    def __init__(self):
        self.sonlar = []

    def son_kirit(self):
        while True:
            son = input("Son kiriting (quitga yozilsa to'xtaydi): ")
            if son.lower() == "quit":
                break
            try:
                self.sonlar.append(int(son))
            except ValueError:
                print("Iltimos son kiriting!")

    def faylga_yoz(self):
        with open("sonlar.txt", "w") as f:
            for son in self.sonlar:
                f.write(str(son) + "\n")

    def fayldan_oq(self):
        try:
            with open("sonlar.txt", "r") as f:
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print("Fayl topilmadi")

    def analiz(self):
        if not self.sonlar:
            print("Sonlar yo'q")
            return
        max_son = max(self.sonlar)
        min_son = min(self.sonlar)
        o_r = sum(self.sonlar) / len(self.sonlar)
        print(f"Max son: {max_son}")
        print(f"Min son: {min_son}")
        print(f"O'rtacha: {o_r}")

def asosiy():
    sonlar = Sonlar()
    while True:
        print("\n1. Son kiriting")
        print("2. Faylga yoz")
        print("3. Fayldan o'q")
        print("4. Analiz")
        print("5. Chiqish")
        tanlov = input("Tanlov: ")
        if tanlov == "1":
            sonlar.son_kirit()
        elif tanlov == "2":
            sonlar.faylga_yoz()
        elif tanlov == "3":
            sonlar.fayldan_oq()
        elif tanlov == "4":
            sonlar.analiz()
        elif tanlov == "5":
            break
        else:
            print("Tanlovda xatolik")

asosiy()