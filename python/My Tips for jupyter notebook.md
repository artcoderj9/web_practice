## Tips for jupyter notebook
1. Don't put your entire code in a single cell
2. There are different types of cells
    - code
    - markdown
3. Executing Cells (shift + enter)
    - "run all" command in the "cell" tab
4. To explore enw modules, use questions and TAB auto-complete
    - print?
    - a = [0, 1, 2]
    - a. + TAB
5. Keyboard shortcu
    - ctrl + shift + p
    - h
    - Esc: command mode
    - a, b: insert new cell
    - m, y: markdown, code
    - d + d: delete current cell
    - Enter: edit mode
    - shift + tab : show docstring
6. disable autocomplete
    - (), [], {}, "" 사용시 자동으로 완성시키는 기능 disable
    - ~/.jupyter/nbconfig/notebook.json 수정
    ~~~
    {
        "CodeCell": {
            "cm_config": {
            "autoCloseBrackets": false
            }
        }
    }
    ~~~
6. IPython built-in magic command
    - https://ipython.readthedocs.io/en/stable/interactive/magics.html
7. Jupyter notebook slideshow extension
    - RISE: https://github.com/damianavila/RISE
8. more tips
    - https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/
