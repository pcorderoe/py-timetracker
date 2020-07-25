import time
import os
import math
from datetime import datetime


class UI:
    start_date = datetime.now()
    initial_time = 0
    title = ''

    def listen_options(self):
        os.system('clear')
        text_options = 'Opciones:\na) Ver acumulado actual(e:defecto)\nb) Salir(s)\n'
        option = str(input(text_options))
        if(option == 'e' or option == 'E'):
            os.system('clear')
            print(
                f"La actividad {self.title} lleva {self.get_elapsed_time():0.1f} minutos")
            time.sleep(1)
            self.listen_options()
        elif(option == 's' or option == 'S'):
            os.system('clear')
            print('Activity stopped!')
            print('==================')
            line = f"{datetime.now().strftime('%Y%m%d%H%M%S')}/{self.title}/{self.start_date.strftime('%Y-%m-%dL%H:%M:%S')}/{(self.get_elapsed_time()/60/60):0.1f} hours/{(self.get_elapsed_time()/60):0.1f} mins/{(self.get_elapsed_time()):0.1f} secs"
            print(line)
            self.save_activity(line)
            # print(f"\tLa actividad {self.title} comenzó en  duró {self.get_elapsed_time():0.1f} minutos\t")
            print('Saved!')
        else:
            os.system('clear')
            print(
                f"La actividad {self.title} lleva {(self.get_elapsed_time()/60):0.1f} minutos")
            time.sleep(1)
            self.listen_options()

    def save_activity(self, line):
        file_object = open(
            r"/home/patricio/pyscripts/tracktimer/register.txt", "a")
        file_object.write(line+"\n")
        file_object.close()

    def start(self):
        self.title = str(input('Ingrese el titulo de la actividad: '))
        self.initial_time = time.perf_counter()

        self.listen_options()

    def get_elapsed_time(self):
        now = time.perf_counter()

        return (math.floor(now - self.initial_time))


def main():
    os.system('clear')
    a = UI()
    a.start()


if __name__ == "__main__":
    main()
