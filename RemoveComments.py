import sublime_plugin

class RemoveFileCommentsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        comments = self.view.find_by_selector('comment')
        for region in reversed(comments):
            self.view.erase(edit, region)
