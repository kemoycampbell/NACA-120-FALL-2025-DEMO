directory = [
    {
        "item_title": "bird_collection.pptx",
        "date": "11/14/2025",
    },
    {
        "item_title": "Comic-and-novel-collections",
        "date": "11/15/2025",
        "content": []
    },
    {
        "item_title": "foods_to_buy.txt",
        "date": "11/15/2025"
    },
    {
        "item_title": "aircraft-supplies-purchase",
        "date": "11/16/2025",
        "content": [
            {
                "item_title": "boeing-supplies",
                "date": "11/16/2025",
                "content": [
                    {
                        "item_title": "engine.pdf",
                        "date": "11/15/2025"
                    }, 
                    {
                        "item_title": "flap-system.pdf",
                        "date": "11/15/2025"
                    }, 
                    {
                        "item_title": "cockpit-equiments.pdf",
                        "date": "11/15/2025"
                    }
                ]
            },
            {
                "item_title": "airbus-supplies",
                "date": "11/16/2025",
                "content": [
                    {
                        "item_title": "navigation-light.pdf",
                        "date": "11/15/2025"
                    }, 
                    {
                        "item_title": "engine-plyon.pdf",
                        "date": "11/15/2025"
                    },
                    {
                        "item_title": "avionics",
                        "date": "11/14/2025",
                        "content": [
                            {
                                "item_title": "mudc.pdf",
                                "date": "11/15/2025"
                            }, 
                            {
                                "item_title": "pfd.pdf",
                                "date": "11/15/2025"
                            }
                        ]
                    }
                ]
            },
            {
                "item_title": "random.txt",
                "date": "11/15/2025"
            }
        ]
    },
    {
        "item_title": "cookie_reciple.txt",
        "date": "11/15/2025"
    }
]

#option 1 - loop mix with recursion
# def print_directory_tree(directory, space = 0):
#     for item in directory:
#         title = item["item_title"]
#         print(" " * space  + "--> " + title)
#         if "content" in item and len(item["content"]) > 0:
#             next_directory = item["content"]
#             print_directory_tree(next_directory, space + 4)


#option 2 - pure recursion
def print_directory_tree(directory, space = 0):
    # If the list is empty, stop
    if len(directory) == 0:
        return

    # Look at the first item in the list
    item = directory[0]
    title = item["item_title"]

    # Print the item with spacing to show depth
    print(" " * space  + "--> " + title)

    # Check if this item has children inside "content"
    # If yes, go inside that folder by calling the function again
    if "content" in item and len(item["content"]) > 0:
        next_directory = item["content"]
        print_directory_tree(next_directory, space + 4)  # add more space for child items
    
    # After finishing this item, move to the rest of the list
    print_directory_tree(directory[1:], space)


print_directory_tree(directory)
