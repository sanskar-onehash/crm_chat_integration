# Copyright (c) 2021, codescientist703 and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ChatRoom(Document):
    def get_members(self):
        if self.members:
            return [x.strip() for x in self.members.split(",")]
        return []

    def before_save(self):
        if self.owner:
            current_members = self.get_members()
            if self.owner not in current_members:
                if self.members:
                    self.members += f",{self.owner}"
                else:
                    self.members = self.owner

        if self.owner and hasattr(self, "users") and self.users:
            owner_exists = False
            for user in self.users:
                if hasattr(user, "user") and user.user == self.owner:
                    owner_exists = True
                    break

            if not owner_exists:
                self.append("users", {"user": self.owner})
