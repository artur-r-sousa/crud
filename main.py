import tkinter as tk
import mysql.connector

#object name
class Crud():

    def __init__(self):
        #self.namemedaddypls.jpg
        self.root = tk.Tk()
        self.root.wm_title('Disney C R U D')
        self.root.geometry('280x520')


        
        self.name_entry0 = tk.Entry(self.root)
        self.name_entry0.grid(row=0, column = 1)
        
        self.l_name_entry0 = tk.Label(self.root, text = 'name')
        self.l_name_entry0.grid(row=0, column = 0)

        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=1, column = 1)

        self.l_email = tk.Label(self.root, text = 'email')
        self.l_email.grid(row=1, column = 0)
        
        #unfortunatelly i could not find a better way for this fix, so it's ugly af, but that's k, guido i still love you my man
        self.go_fuckyourself_frame1 = tk.Label(self.root, text=".......")
        self.go_fuckyourself_frame1.grid(row=2, column=0)

        self.submit = tk.Button(self.root, text='Send Info', command=self.sendtodb)
        self.submit.grid()
        
        self.show_entries = tk.Button(self.root, text='show all users info', command = self.show_userinfo)
        self.show_entries.grid()
        
        #unfortunatelly i still could not find a better way for this fix, so it's really ugly af
        self.go_fuckyourself_frame2 = tk.Label(self.root, text=".......")
        self.go_fuckyourself_frame2.grid(row=5, column=0)

        self.show_entries_selected = tk.Entry(self.root)
        self.show_entries_selected.grid(row=6, column = 1)

        self.l_show_entries_selected = tk.Label(self.root, text = 'Enter Id or name To search')
        self.l_show_entries_selected.grid(row=6, column = 0)

        self.btn_search = tk.Button(self.root, text = 'Search', command=self.search_refined)
        self.btn_search.grid(row = 7, column = 1)



        self.root.mainloop()
        ##favor corrigir as funcoes de search pq ta uma zona isso irmao, seja honesto c a verdade
        ##serio ta feio pra caralho corrige isso
            
    def delete_entry(self):
        value_entered = self.show_entries_selected.get()
        mydb = mysql.connector.connect(
                host="localhost",
                user='artur',
                passwd='581321',
                database='cruddb'
                )
        mycursor = mydb.cursor()
        sql = "DELETE FROM usersinfo WHERE u_name = %s"
        name = (str(value_entered), )
        mycursor.execute(sql, name)
        mydb.commit()
    
    def delete_entry_id(self):
        value_entered = self.show_entries_selected.get()
        mydb = mysql.connector.connect(
                host="localhost",
                user='artur',
                passwd='581321',
                database='cruddb'
                )
        mycursor = mydb.cursor()
        sql = "DELETE FROM usersinfo WHERE id = %s"
        name = (str(value_entered), )
        mycursor.execute(sql, name)
        mydb.commit()

    def update_entry(self):
        self.confirmation_screen = tk.Toplevel()
        self.confirm_entry = tk.Entry(self.confirmation_screen)
        self.confirm_entry.grid(row = 0, column = 1)
        #new name
        self.label_confirm = tk.Label(self.confirmation_screen, text='New Name')
        self.label_confirm.grid(row=0, column=0)

        #new email
        self.confirm_email = tk.Entry(self.confirmation_screen)
        self.confirm_email.grid(row = 1, column = 1)

        self.label_confirm2 = tk.Label(self.confirmation_screen, text='New Email')
        self.label_confirm2.grid(row=1, column=0)

        self.btn_ok = tk.Button(self.confirmation_screen, text='ok', command = self.ue)
        self.btn_ok.grid(row=2)
        
    def ue(self):
        value_entered = self.show_entries_selected.get()
        mydb = mysql.connector.connect(
                host="localhost",
                user='artur',
                passwd='581321',
                database='cruddb'
                )
        mycursor = mydb.cursor()
        sql = "UPDATE usersinfo SET u_name = %s WHERE u_name = %s"        
        preguica0 = str(self.confirm_entry.get())
        preguica1 = str(value_entered)
        name = (preguica0, preguica1)
        
        mycursor.execute(sql, name)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")

    def search_refined(self):
        value_entered = self.show_entries_selected.get()
        try:
            value_entered = int(value_entered)
            mydb = mysql.connector.connect(
                host="localhost",
                user='artur',
                passwd='581321',
                database='cruddb'
                )

            mycursor = mydb.cursor()
            sql = f'''SELECT * FROM usersinfo WHERE id = '{value_entered}' '''
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            self.zoom_toplevel = tk.Toplevel()
            self.tl_label = tk.Label(self.zoom_toplevel, text = myresult)
            self.tl_label.grid()

            self.btn_upd = tk.Button(self.zoom_toplevel, text = 'update', command = self.update_entry).grid()
            self.btn_del = tk.Button(self.zoom_toplevel, text = 'delete', command = self.delete_entry_id).grid()

        except ValueError:
            mydb = mysql.connector.connect(
                host="localhost",
                user='artur',
                passwd='581321',
                database='cruddb'
                )

            mycursor = mydb.cursor()
            sql = f'''SELECT * FROM usersinfo WHERE u_name = '{value_entered}' '''
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            self.zoom_toplevel = tk.Toplevel()
            self.zoom_toplevel.geometry('280x250')
            #self.tl_label = tk.(self.zoom_toplevel, text = myresult)
            #self.tl_label.grid() v0.1
            self.zoom_entry_frame = tk.Frame(self.zoom_toplevel)
            self.zoom_entry_frame.grid()
            self.entry0_update = tk.Entry(self.zoom_entry_frame, width = 35)
            self.entry0_update.grid()
            
            # here is the application variable ('StringVar' object has no attribute 'grid')
            self.variable = tk.StringVar()

            # set it to some value
            self.variable.set(myresult)

            # tell the entry widget to watch this variable
            self.entry0_update["textvariable"] = self.variable
            
            self.zoom_middle_frame = tk.Frame(self.zoom_toplevel)
            self.zoom_middle_frame.grid()
            self.btn_upd = tk.Button(self.zoom_middle_frame, text = 'UPDATE', command = self.update_entry)
            self.btn_upd.grid(row = 1, column = 0)
            self.btn_del = tk.Button(self.zoom_middle_frame, text = 'DELETE', command = self.delete_entry)
            self.btn_del.grid(row = 1, column = 1)
        
    
    def show_userinfo(self):

        mydb = mysql.connector.connect(
        host="localhost",
        user='artur',
        passwd='581321',
        database='cruddb'
        )

        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM usersinfo')
        myresult = mycursor.fetchall()
        self.zoom_toplevel = tk.Toplevel()
        self.tl_label = tk.Label(self.zoom_toplevel, text = myresult)
        self.tl_label.grid()


    def sendtodb(self):

        mydb = mysql.connector.connect(
        host="localhost",
        user='artur',
        passwd='581321',
        database='cruddb'
        )

        user_name = str(self.name_entry0.get())
        user_email = str(self.email_entry.get())
        mycursor = mydb.cursor()
        sql = "INSERT INTO usersinfo (u_name, email) VALUES (%s, %s)"
        val = (user_name, user_email)
        mycursor.execute(sql, val)
        mydb.commit()
        
    


app=Crud()
