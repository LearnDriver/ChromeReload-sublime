import sublime_plugin, subprocess


class ChromeReloadCommand(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        subprocess.call(["/usr/local/bin/chrome-cli", "reload"])
