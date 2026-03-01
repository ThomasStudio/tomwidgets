from functools import partial

from tomwidgets.model import Segoe
from tomwidgets.widget import DictView
from tomwidgets.util.ClassUtil import ClassUtil
from tomwidgets.widget.basic import Tk, Label, ScrollableFrame, Button


def main():
    tkRoot = Tk()
    tkRoot.title("Emoji Example")
    tkRoot.geometry("800x500")

    box = DictView(tkRoot, {}, keyColor="white", valueColor="gold", valueSize=20,
                   splitChar=" ", lineChar="  ")
    box.pack(side='top', fill='x',
             pady=5, anchor='w')

    root = ScrollableFrame(tkRoot)
    root.pack(fill='both', expand=True)

    kvs1 = ClassUtil.getValues(Segoe)

    lineCount = 16
    items = []

    for kvs in [kvs1]:
        for k, v in kvs.items():
            items.append((k, v))

    # split items into several parts, each parts has lineCount items
    itemsParts = [items[i:i+lineCount]
                  for i in range(0, len(items), lineCount)]

    def updateBox(data: list):
        box.clearText()
        box.setDictionary({k: v for k, v in data})

    for parts in itemsParts:
        bar: Label = Button(
            root, text=" ".join([v for k, v in parts]), font=('Arial', 32), anchor='w')
        bar.pack(side='top', fill='x', expand=True,
                 padx=10, pady=5, anchor='w')

        bar.configure(command=partial(updateBox, parts))

    tkRoot.mainloop()


if __name__ == "__main__":
    main()
