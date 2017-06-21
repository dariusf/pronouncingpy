import sublime, sublime_plugin
import platform, os
from . import pronouncing
import random

class ReplaceCommand(sublime_plugin.TextCommand):
  def run(self, edit, start, end, text):
    self.view.replace(edit, sublime.Region(start, end), text)

class RhymeCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    view = self.view

    sel = view.sel()[0]
    word_r = view.word(sel)
    word = view.substr(word_r)

    # matches = 100
    rhymes = pronouncing.rhymes(word) #[:matches]
    random.shuffle(rhymes)

    def replace(i):
      if i > 0:
        view.run_command('replace',
          {'start': word_r.a, 'end': word_r.b, 'text': rhymes[i]})

    if rhymes:
      # view.show_popup_menu(rhymes, replace, 0)
      view.window().show_quick_panel(rhymes, replace, 0, 0)
    else:
      view.window().status_message('No rhymes for "{}"'.format(word))
