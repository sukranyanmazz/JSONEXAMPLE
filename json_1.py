# JSON - UYGULAMA
import json 
import os

FILE_NAME = "Files/people.json"

class Person:
    def __init__(self):
        if not os.path.exists(FILE_NAME):   # "jsonyoutube/people.json" dosyam mevcut değilse oluştur dediğimiz yer
            with open(FILE_NAME, "w", encoding="utf-8") as f:  # türkçe sorunu olmasın diye utf-8
                json.dump([], f, ensure_ascii=False, indent=4)  # burda [] boş bir listeyi json a dönüştürüyoruz
                                                                # türkçe sorun olmaması için ascii=false
                                                                # 4 adet boşluklu(girintili)

# json dosyasını okuyup döndürmek için
    def read_people(self):
        with open(FILE_NAME, "r" , encoding="utf-8") as f:
            return json.load(f)
        
# json a kişi kaydetme        
    def save_people(self,people):
        with open(FILE_NAME, "w" , encoding="utf-8") as f:
            json.dump(people, f, ensure_ascii=False, indent=4)

# kişi ekleme ile function
    def add_person(self):
        name =input("Name:")
        age = int(input("Age:"))
        city = input("City:")
    
        new_person = {"name" : name , "age" : age , "city" : city}

        people = self.read_people() # read_people ile json daki tüm verileri alıp people a atadı (burda jsonı alıp dict olarak people da tutar)
        people.append(new_person)   # people' a yeni kişiyi(new_person) ekledi (burda dict ile aldı )
        self.save_people(people)    # bu da dosyaya yazma işi ( burda jsona dönüştürdü dict i)

        print(f"{name} has been added !")


# dosyadan veri silme
    def delete_person(self):
        name = input("Enter the name of the person to delete:")
        people = self.read_people()  # dosyadan json i oku ve dict olarak people a aktar
        update_people = [item for item in people if item["name"] !=name]  # burda list comprehension
        #(if item["name"] !=name burdaki isim hariç update_people a attı)
        

        if len(people) == len(update_people):
            print(f"{name} not found !")
        else:
            self.save_people(update_people)  # json a çevirir
            print(f"{name} has been deleted!")


# dosyayı gösterme
    def show_people(self):
        people = self.read_people()

        if not people:
            print("No people found")
        else:
            for item in people:
                print(f"Name: {item["name"]} , Age: {item["age"]}, City : {item["city"]}")


class App:
    def __init__(self):
        self.manager = Person() # Composition (Baska bir classı baska bir class ın nesnesi oldu = Person)

    def run(self):
        while True: # sonsuz döngü oldu
            print("\n1- Add Person")
            print("2- Delete Person")
            print("3- Show All Person")
            print("4- Exit")
            choice = int(input("Choose an option:"))

            if choice == 1: self.manager.add_person()
            elif choice == 2: self.manager.delete_person()
            elif choice == 3: self.manager.show_people()
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid option: PLEASE TRY AGAIN")


if __name__=="__main__":
    app = App()
    app.run()


