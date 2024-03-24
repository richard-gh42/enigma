from make_list import num_list_to_let_list, let_list_to_num_list
import tkinter as tk
import tkinter.ttk as ttk

class Enigma:
    def __init__(
            self,
            rotor1=1, ## what rotor is used for the first position (can be reused)
            rotor2=2, ## ^^^^^^^^^^^^
            rotor3=3, ## ^^^^^^^^^^^^
            reflector=1, ## what reflector is used
            notch1=1, ## at which position does the 2nd rotor get advanced by one?
            notch2=2, ## ^^^^^^^^^^^^
            rotor1_pos=1, ## starting position of the rotor
            rotor2_pos=1, ## ^^^^^^^^^^^^
            rotor3_pos=1, ## ^^^^^^^^^^^^
            plugboard=[] ## what letters are connectet on the plugpoard and thus switched?
    ) -> None:

        self.let_to_num = {  ## translates letters to nubers
            "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, 
            "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, 
            "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, 
            "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, 
            "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, 
            "Z": 26,
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 
            'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 
            'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 
            'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 
            'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 
            'z': 26}
        
        self.num_to_let = {  ## translate numbers to letters
            1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 
            6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 
            11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 
            16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 
            21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 
            26: "Z"}

        self.all_rotors = { ## all the rotors avalible (freely interchangeble)
            1: {  ## rotor one
                1: 5, 2: 11, 3: 13, 4: 6, 
                5: 12, 6: 7, 7: 4, 8: 17, 
                9: 22, 10: 26, 11: 14, 12: 20, 
                13: 15, 14: 23, 15: 25, 16: 8, 
                17: 24, 18: 21, 19: 19, 20: 16, 
                21: 1, 22: 9, 23: 2, 24: 18, 
                25: 3, 26: 10},
            2: {  ## rotor two
                1: 1, 2: 10, 3: 4, 4: 11, 
                5: 19, 6: 9, 7: 18, 8: 21, 
                9: 24, 10: 2, 11: 12, 12: 8, 
                13: 23, 14: 20, 15: 13, 16: 3, 
                17: 17, 18: 7, 19: 26, 20: 14, 
                21: 16, 22: 25, 23: 6, 24: 22, 
                25: 15, 26: 5},
            3: {  ## rotor three
                1: 2, 2: 4, 3: 6, 4: 8, 
                5: 10, 6: 12, 7: 3, 8: 16, 
                9: 18, 10: 20, 11: 24, 12: 22, 
                13: 26, 14: 14, 15: 25, 16: 5, 
                17: 9, 18: 23, 19: 7, 20: 1, 
                21: 11, 22: 13, 23: 21, 24: 19, 
                25: 17, 26: 15},
            4: {  ## rotor four
                1: 5, 2: 19, 3: 15, 4: 22, 
                5: 16, 6: 26, 7: 10, 8: 1, 
                9: 25, 10: 17, 11: 21, 12: 9, 
                13: 18, 14: 8, 15: 24, 16: 12, 
                17: 14, 18: 6, 19: 20, 20: 7, 
                21: 11, 22: 4, 23: 3, 24: 13, 
                25: 23, 26: 2},
            5: {  ## rotor five
                1: 22, 2: 26, 3: 2, 4: 18, 
                5: 7, 6: 9, 7: 20, 8: 25, 
                9: 21, 10: 16, 11: 19, 12: 4, 
                13: 14, 14: 8, 15: 12, 16: 24, 
                17: 1, 18: 23, 19: 13, 20: 10, 
                21: 17, 22: 15, 23: 6, 24: 5, 
                25: 3, 26: 11}}
        
        def reverse_rotors(dict: dict): ## since every thing passes through them backwards aswell
            temp = {}
            for i in range(5):
                temp[i+1] = {}
                for j in range(26):
                    temp[i+1][dict[i+1][j+1]] = j+1
            return temp
                
        self.all_rotors_backward = reverse_rotors(self.all_rotors)

        self.all_reflectors = {  ## all avalible reflectors (only in reflector position, doesn't turn)
            1: {  ## reflector one
                1: 5, 2: 10, 3: 13, 4: 26, 
                5: 1, 6: 12, 7: 25, 8: 24, 
                9: 22, 10: 2, 11: 23, 12: 6, 
                13: 3, 14: 18, 15: 17, 16: 21, 
                17: 15, 18: 14, 19: 20, 20: 19, 
                21: 16, 22: 9, 23: 11, 24: 8, 
                25: 7, 26: 4},
            2: {  ## reflector two
                1: 25, 2: 18, 3: 21, 4: 8, 
                5: 17, 6: 19, 7: 12, 8: 4, 
                9: 16, 10: 24, 11: 14, 12: 7, 
                13: 15, 14: 11, 15: 13, 16: 9, 
                17: 5, 18: 2, 19: 6, 20: 26, 
                21: 3, 22: 23, 23: 22, 24: 10, 
                25: 1, 26: 20},
            3: {  ## reflector three
                1: 6, 2: 22, 3: 16, 4: 10, 
                5: 9, 6: 1, 7: 15, 8: 25, 
                9: 5, 10: 4, 11: 18, 12: 26, 
                13: 24, 14: 23, 15: 7, 16: 3, 
                17: 20, 18: 11, 19: 21, 20: 17, 
                21: 19, 22: 2, 23: 14, 24: 13, 
                25: 8, 26: 12}}
        
        self.all_notches = {  ## all avalible notches (freely interghangeble)
            1: [17],
            2: [5],
            3: [22],
            4: [10],
            5: [26],
            6: [26, 13]
        }
        
        self.set_settings(
            rotor1=rotor1,
            rotor2=rotor2,
            rotor3=rotor3,
            reflector=reflector,
            notch1=notch1,
            notch2=notch2,
            rotor1_pos=rotor1_pos,
            rotor2_pos=rotor2_pos,
            rotor3_pos=rotor3_pos,
            plugboard=plugboard,
        )
        
    def en_de_crypt_text(self, text):
        rotor1 = self.all_rotors[self.rotor1]  ## settings
        rotor1_b = self.all_rotors_backward[self.rotor1]
        rotor1_pos = self.rotor1_pos
        notch1 = self.all_notches[self.notch1]

        rotor2 = self.all_rotors[self.rotor2]
        rotor2_b = self.all_rotors_backward[self.rotor2]
        rotor2_pos = self.rotor2_pos
        notch2 = self.all_notches[self.notch2]

        rotor3 = self.all_rotors[self.rotor3]
        rotor3_b = self.all_rotors_backward[self.rotor3]
        rotor3_pos = self.rotor3_pos

        reflector = self.all_reflectors[self.reflector]

        plugboard = self.plugboard            ## settings end

        text = self.__disasseble_str(text) ## breaks text up into letters
        temp_text = []                          ## temp for (my) conveniance

        for i in text:
            for j in range(len(notch2)):    ## advances the rotors
                if rotor2_pos == notch2[j]:
                    rotor3_pos = rotor3_pos+1
            for j in range(len(notch1)):
                if rotor1_pos == notch1[j]:
                    rotor2_pos = rotor2_pos+1
            rotor1_pos = rotor1_pos+1

            rotor1_pos = self.__check_for_26(rotor1_pos)
            rotor2_pos = self.__check_for_26(rotor2_pos)
            rotor3_pos = self.__check_for_26(rotor3_pos)
            
            letter = i          ## again for (my) conveniance
            
            try:    ## if assigned in the plugboard, the letter will be switched
                letter = plugboard[letter]
            except:
                pass
            
            temp_rotor1 = rotor1_pos-1
            letter = self.__check_for_26(letter+temp_rotor1)
            letter = rotor1[letter]
            letter = self.__check_for_26(letter-temp_rotor1)

            temp_rotor2 = rotor2_pos-1
            letter = self.__check_for_26(letter+temp_rotor2)
            letter = rotor2[letter]
            letter = self.__check_for_26(letter-temp_rotor2)

            temp_rotor3 = rotor3_pos-1
            letter = self.__check_for_26(letter+temp_rotor3)
            letter = rotor3[letter]
            letter = self.__check_for_26(letter-temp_rotor3)

            letter = reflector[letter]

            letter = self.__check_for_26(letter+temp_rotor3)
            letter = rotor3_b[letter]
            letter = self.__check_for_26(letter-temp_rotor3)

            letter = self.__check_for_26(letter+temp_rotor2)
            letter = rotor2_b[letter]
            letter = self.__check_for_26(letter-temp_rotor2)

            letter = self.__check_for_26(letter+temp_rotor1)
            letter = rotor1_b[letter]
            letter = self.__check_for_26(letter-temp_rotor1)

            try:    ## if assigned in the plugboard, the letter will be switched
                letter = plugboard[letter]
            except:
                pass

            temp_text.append(letter)

        text = self.__reasemble_str(temp_text)
        return text

    def __disasseble_str(self, str:str):  ## removes all not includet letters, splits the string into a list of letters and converts it to numbers
        str_l = []
        for i in str:
            try:
                str_l.append(self.let_to_num[i])
            except:
                pass
        return str_l
    
    def __reasemble_str(self, list: list=[str,...]):  ## make one string out of the long list again
        list = num_list_to_let_list(list)
        str = ""
        for i in list:
            str = str+i
        return str
    
    def __check_for_26(self, n):    ## makes shure the letter remains betwen 1 and 26
        while n > 26:
            n = n-26
        while n < 1:
            n = n+26
        return n

    def set_settings(  ## sets up the settings
            self, 
            rotor1: int=1, ## what rotor is used here (can be reused)
            rotor2: int=2, ## ^^^^^^^^^^^^
            rotor3: int=3, ## ^^^^^^^^^^^^
            reflector: int=1, ## what reflector is used
            notch1: int=1, ## at which position does the 2nd rotor get advanced by one?
            notch2: int=2, ## ^^^^^^^^^^^^
            rotor1_pos: int=1, ## starting position of the rotor
            rotor2_pos: int=1, ## ^^^^^^^^^^^^
            rotor3_pos: int=1, ## ^^^^^^^^^^^^
            plugboard: list=[["A","B"],["C","D"]] ## what letters are connectet on the plugpoard and thus switched?
    ):
        self.set_rotors(rotor1=rotor1, rotor2=rotor2, rotor3=rotor3)
        self.set_rotor_positions(rotor1=rotor1_pos, rotor2=rotor2_pos, rotor3=rotor3_pos)
        self.set_reflector(reflector=reflector)
        self.set_notches(notch1=notch1, notch2=notch2)
        self.set_plugboard(plugboard=plugboard)

    def set_rotors(self, rotor1=1, rotor2=2, rotor3=3):
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3

    def set_rotor_positions(self, rotor1=1, rotor2=1, rotor3=1):
        self.rotor1_pos = rotor1
        self.rotor2_pos = rotor2
        self.rotor3_pos = rotor3

    def set_reflector(self, reflector=1):
        self.reflector = reflector

    def set_notches(self, notch1=1, notch2=2):
        self.notch1 = notch1
        self.notch2 = notch2

    def set_plugboard(self, plugboard):
        self.plugboard = {}
        for i in range(len(plugboard)):
            if plugboard[i][0] is str:
                plugboard[i] = let_list_to_num_list(plugboard[i])
            self.plugboard[plugboard[i][0]] = plugboard[i][1]
            self.plugboard[plugboard[i][1]] = plugboard[i][0]

class Enigma_UI:
    def __init__(self) -> None:
        self.en = Enigma()          ## initiates "enigma"
        self.plugboard = []

        self.tk = tk.Tk()           ## initiate tkinter
        self.tk.geometry("500x500")
        self.tk.title("Enigma")
        
        ##  text field for en-/decryption
        self.txt = tk.Text(self.tk)
        self.txt.place(relx=0, rely=0, relheight=0.62, relwidth=1)

        ##  text field for diplaying plugboard connection
        self.plugboard_txt = tk.Text(self.tk)
        self.plugboard_txt.place(relx=0, rely=0.62, relheight=0.17, relwidth=0.7)
        self.plugboard_txt.configure(state="disabled")

        ##  Rotor selection labels
        self.rotor1_label = tk.Label(self.tk, text="Rotor 1:")
        self.rotor2_label = tk.Label(self.tk, text="Rotor 2:")
        self.rotor3_label = tk.Label(self.tk, text="Rotor 3:")
        self.reflector_label = tk.Label(self.tk, text="Reflector:")

        self.rotor1_label.place(relx=0, rely=0.8)
        self.rotor2_label.place(relx=0, rely=0.84)
        self.rotor3_label.place(relx=0, rely=0.88)
        self.reflector_label.place(relx=0, rely=0.92)

        ## rotor selection Comboboxes
        rotor_list = [1,2,3,4,5]
        reflector_list = [1,2,3]
        self.rotor1_selection = ttk.Combobox(self.tk, values=rotor_list)
        self.rotor2_selection = ttk.Combobox(self.tk, values=rotor_list)
        self.rotor3_selection = ttk.Combobox(self.tk, values=rotor_list)
        self.reflector_selection = ttk.Combobox(self.tk, values=reflector_list)

        self.rotor1_selection.place(relx=0.11, rely=0.8, relwidth=0.1)
        self.rotor2_selection.place(relx=0.11, rely=0.84, relwidth=0.1)
        self.rotor3_selection.place(relx=0.11, rely=0.88, relwidth=0.1)
        self.reflector_selection.place(relx=0.11, rely=0.92, relwidth=0.1)

        self.rotor1_selection.current(0)
        self.rotor2_selection.current(0)
        self.rotor3_selection.current(0)
        self.reflector_selection.current(0)

        self.rotor1_selection.bind("<<ComboboxSelected>>", self.__change_rotors)
        self.rotor2_selection.bind("<<ComboboxSelected>>", self.__change_rotors)
        self.rotor3_selection.bind("<<ComboboxSelected>>", self.__change_rotors)
        self.reflector_selection.bind("<<ComboboxSelected>>", self.__change_reflector)

        self.rotor1_selection.configure(state="readonly")
        self.rotor2_selection.configure(state="readonly")
        self.rotor3_selection.configure(state="readonly")
        self.reflector_selection.configure(state="readonly")

        ##  rotor position selection labels
        self.pos1_label = tk.Label(self.tk, text="Position:")
        self.pos2_label = tk.Label(self.tk, text="Position:")
        self.pos3_label = tk.Label(self.tk, text="Position:")

        self.pos1_label.place(relx=0.21, rely=0.8)
        self.pos2_label.place(relx=0.21, rely=0.84)
        self.pos3_label.place(relx=0.21, rely=0.88)

        ##  rotor position selection Comboboxes
        rotor_state_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
        self.pos1_selection = ttk.Combobox(self.tk, values=rotor_state_list)
        self.pos2_selection = ttk.Combobox(self.tk, values=rotor_state_list)
        self.pos3_selection = ttk.Combobox(self.tk, values=rotor_state_list)

        self.pos1_selection.place(relx=0.31, rely=0.8, relwidth=0.1)
        self.pos2_selection.place(relx=0.31, rely=0.84, relwidth=0.1)
        self.pos3_selection.place(relx=0.31, rely=0.88, relwidth=0.1)

        self.pos1_selection.current(0)
        self.pos2_selection.current(0)
        self.pos3_selection.current(0)

        self.pos1_selection.bind("<<ComboboxSelected>>", self.__change_rotor_positions)
        self.pos2_selection.bind("<<ComboboxSelected>>", self.__change_rotor_positions)
        self.pos3_selection.bind("<<ComboboxSelected>>", self.__change_rotor_positions)

        self.pos1_selection.configure(state="readonly")
        self.pos2_selection.configure(state="readonly")
        self.pos3_selection.configure(state="readonly")

        ##  Turnover notch selection lables
        self.notch1_lable = tk.Label(self.tk, text="Turn over notch:")
        self.notch2_lable = tk.Label(self.tk, text="Turn over notch:")

        self.notch1_lable.place(relx=0.41, rely=0.8)
        self.notch2_lable.place(relx=0.41, rely=0.84)

        ##  Turnover notch selection Comboboxes
        notch_list = [1,2,3,4,5,6]
        self.notch1_selection = ttk.Combobox(self.tk, values=notch_list)
        self.notch2_selection = ttk.Combobox(self.tk, values=notch_list)

        self.notch1_selection.place(relx=0.6, rely=0.8, relwidth=0.1)
        self.notch2_selection.place(relx=0.6, rely=0.84, relwidth=0.1)

        self.notch1_selection.current(0)
        self.notch2_selection.current(0)

        self.notch1_selection.bind("<<ComboboxSelected>>", self.__change_notches)
        self.notch2_selection.bind("<<ComboboxSelected>>", self.__change_notches)

        self.notch1_selection.configure(state="readonly")
        self.notch2_selection.configure(state="readonly")

        ##  Plugboard selection lable
        self.plugboard_lable = tk.Label(self.tk, text="Plugboard connections:")
        self.plugboard_lable.place(relx=0.7, rely=0.62)

        ##  plugboard selection Comboboxes
        plugboard_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.plugboard1_selection = ttk.Combobox(self.tk, values=plugboard_list)
        self.plugboard2_selection = ttk.Combobox(self.tk, values=plugboard_list)

        self.plugboard1_selection.place(relx=0.7, rely=0.66, relwidth=0.15)
        self.plugboard2_selection.place(relx=0.85, rely=0.66, relwidth=0.15)

        self.plugboard1_selection.configure(state="readonly")
        self.plugboard2_selection.configure(state="readonly")

        ##  Buttons
        self.add_remove_connection_button = tk.Button(self.tk, text="Add/Remove connection", command=self.__add_remove_connection)
        self.add_remove_connection_button.place(relx=0.7, rely=0.7, relheight=0.1, relwidth=0.3)

        self.en_de_crypt_button = tk.Button(self.tk, text= "En-/Decrypt", command=self.__en_de_crypt)
        self.en_de_crypt_button.place(relx=0.7, rely=0.8, relheight=0.1, relwidth=0.3)

        self.exit_button = tk.Button(self.tk, text="Exit", command=self.tk.destroy)
        self.exit_button.place(relx=0.7, rely=0.9, relheight=0.1, relwidth=0.3)
        
        self.tk.mainloop()

    ##  send the text in the text field through the enigma
    def __en_de_crypt(self):
        temp = self.txt.get(1.0, tk.END)
        result = self.en.en_de_crypt_text(temp)
        self.txt.delete(1.0, tk.END)
        self.txt.insert(1.0, result)

    ##  adds a connection. If the connection already exists it gets removed. If one of the letters is already connected or both have the same value, nothing happens.
    def __add_remove_connection(self):
        temp = [self.plugboard1_selection.get(), self.plugboard2_selection.get()]
        if temp[0] == "" or temp[1] == "":
            return
        temp = let_list_to_num_list(temp)
        if temp[0] == temp[1]:
            return
        
        check = self.__check_plugboard(temp)
        if check == 0:
            self.plugboard.append(temp)
        elif check == 1:
            try:
                self.plugboard.remove(temp)
            except:
                self.plugboard.remove([temp[1], temp[0]])
        else:
            return
        
        self.en.set_plugboard(self.plugboard)

        self.plugboard_txt.configure(state="normal")
        self.plugboard_txt.delete(1.0, tk.END)

        temp = []
        for i in range(len(self.plugboard)):
            temp.append(num_list_to_let_list(self.plugboard[i]))
        self.plugboard_txt.insert(1.0, temp)
        self.plugboard_txt.configure(state="disabled")

    ##  check whether the given letters are already connencted
    def __check_plugboard(self, check=[1,2]):
        if check[0] in self.en.plugboard and check[1] in self.en.plugboard:
            return 1
        if check[0] in self.en.plugboard or check[1] in self.en.plugboard:
            return 2
        return 0
    
    ## self explanatory
    def __change_rotors(self, event=None):
        self.en.set_rotors(
            rotor1=int(self.rotor1_selection.get()),
            rotor2=int(self.rotor2_selection.get()),
            rotor3=int(self.rotor3_selection.get())
        )
    
    def __change_reflector(self, event=None):
        self.en.set_reflector(int(self.reflector_selection.get()))

    def __change_rotor_positions(self, event=None):
        self.en.set_rotor_positions(
            rotor1=int(self.pos1_selection.get()),
            rotor2=int(self.pos2_selection.get()),
            rotor3=int(self.pos3_selection.get())
        )

    def __change_notches(self, event=None):
        self.en.set_notches(
            notch1=int(self.notch1_selection.get()),
            notch2=int(self.notch2_selection.get())
        )

if __name__ == "__main__":
    v = Enigma_UI()