import tkinter as tk
from tkinter import ttk
from discodos import log
from discodos import models

class widget_frame():
    def __init__(self, parent, title):
        self.edit_win = tk.Toplevel(parent)
        # log.debug("Window State is " + self.edit_win.state())
        global win_state 
        self.win_state = self.edit_win.state()

        self.edit_win.geometry("350x600")               
        self.edit_win.resizable(False, False) 

        self.edit_win.title(title)
        x = parent.winfo_x()
        y = parent.winfo_y()
        self.edit_win.geometry("+%d+%d" % (x + 800, y))

    def _quit(self):
        self.edit_win.destroy()
        


class edit_mix_view(widget_frame):
    def __init__(self, parent, mix_data, conn):
        self.title = "Edit Mix Info"
        super().__init__(parent, self.title)
        self.mix_data = mix_data
        self.view_mix_content()
        self.conn = conn

        self.insert_track_pool()
        

        # log.debug(mix_data["venue"])


    def view_mix_content(self):

        self.mix_info_frame = tk.LabelFrame(self.edit_win, text="Mix Info")
        self.pool_frame = tk.LabelFrame(self.edit_win, text="Discogs Track Pool")
        self.buttons_frame = tk.Frame(self.edit_win)

        #############################################
        # Mix Info edit
        #############################################


        tk.Label(self.mix_info_frame, text="Name").grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(self.mix_info_frame, width=30)
        self.name_entry.grid(row=0, column=1, sticky="w")
        try:
            self.name_entry.insert(0, self.mix_data["name"])
        except:
            log.error("Couldn't insert Data")

        tk.Label(self.mix_info_frame, text="Played").grid(row=1, column=0, sticky="w")
        self.played_entry = tk.Entry(self.mix_info_frame, width=30)
        self.played_entry.grid(row=1, column=1, sticky="w")
        self.played_entry.insert(0, self.mix_data["played"])

        tk.Label(self.mix_info_frame, text="Venue").grid(row=2, column=0, sticky="w")
        self.venue_entry = tk.Entry(self.mix_info_frame, width=30)
        self.venue_entry.grid(row=2, column=1, sticky="w")
        self.venue_entry.insert(0, self.mix_data["venue"])

        tk.Label(self.mix_info_frame, text="Created").grid(row=3, column=0, sticky="w")
        tk.Label(self.mix_info_frame, text=self.mix_data["created"]).grid(row=3, column=1, sticky="w")

        tk.Label(self.mix_info_frame, text="Last Updated").grid(row=4, column=0, sticky="w")
        tk.Label(self.mix_info_frame, text=self.mix_data["updated"]).grid(row=4, column=1, sticky="w")

        for i in range(5,9):
            self.mix_info_frame.rowconfigure(i, weight=1)

        self.update_collection = tk.Button(self.mix_info_frame, text="Update Collection")
        self.update_collection.grid(row=8, column=0, sticky="s")


        #############################################
        # Track Pool
        #############################################

        self.coll_list = ttk.Treeview(self.pool_frame)
        self.coll_list.pack(fill="both", expand=1)

        self.coll_list["columns"]=("artist", "id")
        self.coll_list.column("#0", width=25,  minwidth=10)
        self.coll_list.column("artist", width=30, minwidth=10)
        self.coll_list.column("id", width=5,  minwidth=3)

        self.coll_list.heading("#0",text="Release",anchor=tk.W)
        self.coll_list.heading("artist", text="Artist", anchor=tk.W)
        self.coll_list.heading("id", text="Discogs ID",anchor=tk.W)



        # TODO: fetch discogs track data


        ###############################################

        # Buttons Area

        tk.Button(self.buttons_frame, text="<- Add Track to Mix").pack(side="left")
        tk.Button(self.buttons_frame, text="Save Mix").pack(side="right")

        # Display Frames

        self.mix_info_frame.pack(fill="both", expand=1, side = "top")
        self.buttons_frame.pack(side="bottom", fill="x")
        self.pool_frame.pack(fill="both", expand=1, side = "bottom")
    
    def insert_track_pool(self):
        self.collection = models.Collection(self.conn)
        try:
            self.all_releases = self.collection.get_all_db_releases()
            log.debug("GUI: Got all releases from Collection Model")
        except:
            log.error("GUI: Couldn't get all releases from Collection Model")
        
        for i, row in enumerate(self.all_releases):
            self.coll_list.insert("" , i, text=row["discogs_title"], values=(row["d_artist"], row["discogs_id"]))

    def add_track_to_mix(self):
        pass

        

        



class edit_track_info(widget_frame):

    def __init__(self, parent):
        self.title = "Edit Track Info"
        super().__init__(parent, self.title)
        self.view_track_content()


    def view_track_content(self):
        pass



