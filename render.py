from rich.console import Console
from rich.tree import Tree
import yaml
from dataclasses import dataclass


@dataclass(frozen=True)
class TreeNode:
    name: str
    link: str = ""
    description: str = ""
    icon: str = ""


def add_leaves(trees, parent):
    for key in trees:
        node = TreeNode(key, **trees[key])
        temp_tree = Tree(f"[bold link={node.link}]{node.name}[/] - [bright_black]{node.description}")
        parent.add(temp_tree)
    
    return parent


with open("C:\Temp\GitHub - BryanGoodrich README Generator.yaml", encoding="utf-8") as fh:
    data = yaml.safe_load(fh)


console = Console(record=True, width=100)

key = "Bryan Goodrich"
node = TreeNode(key, **data[key])
tree = Tree(f"[bold bright_black link={node.link}]{node.icon} {node.name}")

key = "Open Source Repositories"
trees = data[key].pop("trees")
node = TreeNode(key, **data[key])
tree.add(add_leaves(trees, Tree(f"[bright_black]{node.icon} {node.name}")))

key = "Sandbox"
trees = data[key].pop("trees")
node = TreeNode(key, **data[key])
tree.add(add_leaves(trees, Tree(f"[bright_black]{node.icon} {node.name}")))

key = "Workplace"
trees = data[key].pop("trees")
node = TreeNode(key, **data[key])
tree.add(add_leaves(trees, Tree(f"[bright_black]{node.icon} {node.name}")))

key = "Experiments (Gists)"
trees = data[key].pop("trees")
node = TreeNode(key, **data[key])
tree.add(add_leaves(trees, Tree(f"[bright_black]{node.icon} {node.name}")))


console.print(tree)
console.print("")
console.print("[green]Follow me on twitter [bold link=https://twitter.com/bryangoodrich]@bryangoodrich[/]")


CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("C:\Temp\README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
