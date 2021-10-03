''' this code made by sl4shroot @rizkyy12 '''

from tkinter import *
import copy


class Node:

    def __init__(self, data):

        self.kiri = None
        self.kanan = None
        self.data = data
        self.parent = None


    def lookup(self, data, parent=None):

        if data < self.data:
            if self.kiri is None:
                return None, None
            return self.kiri.lookup(data, self)
        elif data > self.data:
            if self.kanan is None:
                return None, None
            return self.kanan.lookup(data, self)
        else:
            return self, parent
    # memperbarui parents
    def refresh_parents(self):
        if self.kiri:
            self.kiri.parent = self
            self.kiri.refresh_parents()
        if self.kanan:
            self.kanan.parent = self
            self.kanan.refresh_parents()

    def delete(self, data):

        # dapatkan node yang berisi data
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()
        if children_count == 0:
            # Jika simpul tidak memiliki anak, hapus saja
            if parent:
                if parent.kiri is node:
                    parent.kiri = None
                else:
                    parent.kanan = None
                del node
            else:
                self.data = None
        elif children_count == 1:
            # Jika simpul memiliki 1 anak
            # Temukan penggantinya
            if node.kiri:
                n = node.kiri
            else:
                n = node.kanan
            if parent:
                n.parent = parent
                if parent.kiri is node:
                    parent.kiri = n
                else:
                    parent.kanan = n
                del node
            else:
                self.kiri = n.kiri
                if self.kiri:
                    self.kiri.parent = self
                self.kanan = n.kanan
                if self.kanan:
                    self.kanan.parent = self
                self.data = n.data
                self.parent = n.parent
        else:
            # Jika simpul memiliki 2 anak
            # Temukan penggantinya
            parent = node
            successor = node.kanan
            while successor.kiri:
                parent = successor
                successor = successor.kiri
            # Ganti data node dgn data penggantinya
            node.data = successor.data
            # memperbaikin successor anak
            if parent.kiri == successor:
                parent.kiri = successor.kanan
                if parent.kiri:
                    successor.right.parent = parent
            else:
                parent.kanan = successor.kanan
                if parent.kanan:
                    parent.kanan.parent = parent

    def print_tree(self):
        if self.kiri:
            self.kiri.print_tree()
        print(self.data),
        if self.kanan:
            self.kanan.print_tree()

    def count_levels(self):
        lcount = 0
        rcount = 0
        if self.kiri:
            lcount = self.kiri.count_levels()
        if self.kanan:
            rcount = self.kanan.count_levels()
        return 1 + max(lcount, rcount)
        print(self.data)

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.kiri is None:
                    self.kiri = Node(data)
                    self.kiri.parent = self
                else:
                    self.kiri.insert(data)
            elif data > self.data:
                if self.kanan is None:
                    self.kanan = Node(data)
                    self.kanan.parent = self
                else:
                    self.kanan.insert(data)
        else:
            self.data = data
    

    def get_coords(self, x, y, sw, sh):
        tosend = [[x, y, self.data]]
        if self.kiri:
            tosend = tosend + (self.kiri.get_coords(x - sw / 2, y + sh, sw / 2, sh))
        if self.kanan:
            tosend = tosend + (self.kanan.get_coords(x + sw / 2, y + sh, sw / 2, sh))
        return tosend

    def get_lines(self, x, y, sw, sh):
        tosend = []
        if self.kiri:
            l = self.kiri.get_coords(x - sw / 2, y + sh, sw / 2, sh)
            tosend = tosend + [[x, y, l[0][0], l[0][1]]]
            tosend = tosend + self.kiri.get_lines(x - sw / 2, y + sh, sw / 2, sh)
        if self.kanan:
            r = self.kanan.get_coords(x + sw / 2, y + sh, sw / 2, sh)
            tosend = tosend + [[x, y, r[0][0], r[0][1]]]
            tosend = tosend + self.kanan.get_lines(x + sw / 2, y + sh, sw / 2, sh)
        return tosend

    def show_tree(self):
        h = self.count_levels()
        w = 2 ** (h - 1)
        sh = 512 * 1.25
        sw = 512 * 1.5
        r = sw / w / 2
        if r >=10:
            r = 10
        window = Tk()
        window.title("AVL Tree")  # set judul
        canvas = Canvas(window, width=sw + 100, height=sh + 100, bg="white")
        canvas.pack()
        sh = int((sh - 2 * h * r) / (h))
        toshow = self.get_lines(50 + sw / 2, 50 + r, sw / 2, sh)
        headlabel = Label(window, text = 'welcome to distance time calculator', 
                      fg = 'black', bg = "red")
        for i in toshow:
            x1 = i[0]
            y1 = i[1]
            x2 = i[2]
            y2 = i[3]
            canvas.create_line(x1, y1, x2, y2)
        toshow = self.get_coords(50 + sw / 2, 50 + r, sw / 2, sh)
        for i in toshow:
            x = i[0]
            y = i[1]
            text = i[2]
            if r == 10:
                canvas.create_oval(x - r, y - r, x + r, y + r, fill="white")
            canvas.create_text(x, y, text=text) 

        window.mainloop()
