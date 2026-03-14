import json
import datetime

FILE = "students.json"


class StdMgr:

    def __init__(self):
        self.std_list = self.load()

    # ---------- Login ----------
    def login(self):
        print("\n===== LOGIN =====")
        usr = input("Username: ")
        pwd = input("Password: ")

        if usr == "admin" and pwd == "1234":
            print("Login successful!\n")
            return True
        else:
            print("Invalid credentials\n")
            return False

    # ---------- Load Data ----------
    def load(self):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except:
            return []

    # ---------- Save Data ----------
    def save(self):
        with open(FILE, "w") as f:
            json.dump(self.std_list, f, indent=4)

    # ---------- Add Student ----------
    def add_std(self):

        rl = input("Enter Roll No: ")

        for std in self.std_list:
            if std["rl"] == rl:
                print("Roll number already exists\n")
                return

        nm = input("Enter Name: ")
        dp = input("Enter Department: ")

        data = {
            "rl": rl,
            "nm": nm,
            "dp": dp,
            "dt": str(datetime.date.today())
        }

        self.std_list.append(data)
        self.save()

        print("Student added\n")

    # ---------- View Students ----------
    def view_std(self):

        if not self.std_list:
            print("No records\n")
            return

        print("\n----- Student Records -----")

        for std in self.std_list:
            print(f"{std['rl']} | {std['nm']} | {std['dp']} | {std['dt']}")

        print(f"\nTotal: {len(self.std_list)}\n")

    # ---------- Search ----------
    def search_std(self):

        rl = input("Enter Roll No: ")

        for std in self.std_list:
            if std["rl"] == rl:
                print("\nStudent Found")
                print(f"Name: {std['nm']}")
                print(f"Dept: {std['dp']}")
                print(f"Date: {std['dt']}\n")
                return

        print("Student not found\n")

    # ---------- Update ----------
    def upd_std(self):

        rl = input("Enter Roll No to update: ")

        for std in self.std_list:

            if std["rl"] == rl:

                print("Leave blank to skip")

                nm = input("New Name: ")
                dp = input("New Dept: ")

                if nm:
                    std["nm"] = nm

                if dp:
                    std["dp"] = dp

                self.save()
                print("Updated\n")
                return

        print("Student not found\n")

    # ---------- Delete ----------
    def del_std(self):

        rl = input("Enter Roll No to delete: ")

        for std in self.std_list:

            if std["rl"] == rl:
                self.std_list.remove(std)
                self.save()

                print("Deleted\n")
                return

        print("Student not found\n")

    # ---------- Menu ----------
    def run(self):

        while True:

            print("====== STD MANAGEMENT ======")
            print("1 Add")
            print("2 View")
            print("3 Search")
            print("4 Update")
            print("5 Delete")
            print("6 Exit")

            try:
                ch = input("Choice: ")
            except EOFError:
                print("Program ended")
                break

            if ch == "1":
                self.add_std()

            elif ch == "2":
                self.view_std()

            elif ch == "3":
                self.search_std()

            elif ch == "4":
                self.upd_std()

            elif ch == "5":
                self.del_std()

            elif ch == "6":
                print("Program closed")
                break

            else:
                print("Invalid option\n")


# ---------- Main ----------
if __name__ == "__main__":

    app = StdMgr()

    if app.login():
        app.run()
