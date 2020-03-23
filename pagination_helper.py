class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        if len(self.collection) % self.items_per_page:
            return len(self.collection) // self.items_per_page + 1
        else:
            return len(self.collection) // self.items_per_page

    def page_item_count(self, page_index):
        if page_index > self.page_count() - 1:
            return -1
        elif page_index < self.page_count() - 1:
            return self.items_per_page
        else:
            return len(self.collection) % self.items_per_page

    def page_index(self, item_index):
        if 0 <= item_index < len(self.collection):
            return item_index // self.items_per_page
        else:
            return -1


helper = PaginationHelper(["a", "b", "c", "d", "e", "f"], 4)
print(1, helper.page_count())  # should == 2
print(2, helper.item_count())  # should == 6
print(3, helper.page_item_count(0))  # should == 4
print(4, helper.page_item_count(1))  # last page - should == 2
print(5, helper.page_item_count(2))  # should == -1 since the page is invalid

print(helper.page_index(5))  # should == 1 (zero based index)
print(helper.page_index(2))  # should == 0
print(helper.page_index(20))  # should == -1
print(helper.page_index(-10))  # should == -1 because negative indexes are invalid

