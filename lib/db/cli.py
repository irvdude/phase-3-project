from simple_term_menu import TerminalMenu
from models import Person, Chore
from seed import session


class Cli:
    def main(self):
        options = ["Person", "Chores", "Todo"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Person":
            people_names = self.give_all_people()
            if people_names:
                name = self.select_person(people_names)
                if name:
                    self.chore_by_person(name)

        if options[menu_entry_index] == "Chores":
            self.give_all_chores()

        if options[menu_entry_index] == "Todo":
            name = input("Provide a name: ")
            self.chore_by_person(name)

    def give_all_people(self):
        people = Person.list_people(session)
        if people:
            print("List of people:")
            for person in people:
                print(person.name)
            return [person.name for person in people]
        else:
            print("No people found.")
            return []

    def select_person(self, people_names):
        if not people_names:
            return None

        terminal_menu = TerminalMenu(people_names)
        menu_entry_index = terminal_menu.show()
        return people_names[menu_entry_index]

    def give_all_chores(self):
        chores = Chore.list_chores(session)
        if chores:
            print("List of chores")
            for chore in chores:
                print(chore.chore_name)

    def chore_by_person(self, name=None):
        if not name:
            return

        chores = Person.chores_by_person(session, name)
        if chores:
            print(f"Chores for {name}:")
            for chore in chores:
                print(chore.chore_name)
        else:
            print(f"No chores found for {name}")


app = Cli()
app.main()
