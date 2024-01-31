class TreeNode:
    def __init__(self, value='', children=None):
        self.value = value
        self.children = children if children else dict()

def convert_list_to_prefix_tree_nodes(words: list[str]):
    root = TreeNode()

    for word in words:
        itr = root
        i = 0
        while i < len(word):
            char = word[i]
            if char not in itr.children:
                itr.children[char] = TreeNode(char)                
            itr = itr.children[char]
            i += 1
        # Terminating node showing this is an end to a word, even if another continues.
        itr.children['*'] = TreeNode('*')
    
    return root

# Print with BFS.
def print_tree(root):
    pass

if __name__ == '__main__':
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    months_prefix_tree = convert_list_to_prefix_tree_nodes(months)
    # words = ['at', 'ate', 'it']
    # prefix_tree = convert_list_to_prefix_tree_nodes(words)

