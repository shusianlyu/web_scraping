# ----------------------------------------------------------------------
# Name:        matchit
# Purpose:     Implement a single player matching game
#
# Author(s): Jessie Lyu, An Tran
# ----------------------------------------------------------------------
"""
A single player matching game.

usage: matchit.py [-h] [-f] {blue,green,magenta} [image_folder]
positional arguments:
  {blue,green,magenta}  What color would you like for the player?
  image_folder          What folder contains the game images?

optional arguments:
  -h, --help            show this help message and exit
  -f, --fast            fast or slow game?
"""
import tkinter
import os
import random
import argparse


class MatchGame(object):
    """
    GUI Game class for a matching game.

    Arguments:
    parent: the root window object
    player_color (string): the color to be used for the matched tiles
    folder (string) the folder containing the images for the game
    delay (integer) how many milliseconds to wait before flipping a tile

    Attributes:
    Please list ALL the instance variables here
    delay: (int) delay before image is hidden
    player_color: (string) color representing the player
    score: (int) score of player
    tries: (int) turns taken by player
    pairs: (int) total number of matches remaining to win
    my_canvas: (tkinter.Canvas) A Canvas widget
    score_label: (tkinter.Label) A Label widget that displays score and
                                 game over message
    image_names: (List) randomized list of image names used as keys in
                        dictionary
    image_dict: (Dictionary) dictionary mapping image names to actual
                             tkinter.PhotoImage
    image_id: (int) ID of the Canvas image object
    """

    # Add your class variables if needed here - square size, etc...)
    CANVAS_SIZE = 600
    TILE_SIZE = 150

    def __init__(self, parent, player_color, folder, delay):
        parent.title('Match it!')

        # set attributes of game
        self.delay = 1000 if delay else 3000
        self.player_color = player_color
        self.score = 100
        self.tries = 0
        self.pairs = 8

        # Create the restart button widget
        restart_button = tkinter.Button(parent, text='RESTART',
                                        command=self.restart)
        restart_button.grid()

        # Create a canvas widget
        self.my_canvas = tkinter.Canvas(parent, width=self.CANVAS_SIZE,
                                        height=self.CANVAS_SIZE)
        self.my_canvas.grid()

        # Create tile widgets
        for row in range(0, self.CANVAS_SIZE, self.TILE_SIZE):
            for col in range(0, self.CANVAS_SIZE, self.TILE_SIZE):
                self.my_canvas.create_rectangle(col, row, col + self.TILE_SIZE,
                                                row + self.TILE_SIZE,
                                                outline=self.player_color,
                                                fill='yellow')

        # Create a label widget for the score and end of game messages
        self.score_label = tkinter.Label(parent, text=f'Score: {self.score}')
        self.score_label.grid()

        # Create any additional instance variable you need for the game
        # Create list of file names and map image names to tkinter.PhotoImage

        # get gif images from directory
        file_images = [file for file in os.listdir(folder) if file.endswith(
            '.gif')]
        # randomize images (useful if more than 8 images)
        random.shuffle(file_images)
        # get 8 images from list
        eight_file_images = file_images[0:8]
        # duplicate list to get 8 pairs of images
        self.image_names = 2 * eight_file_images
        # shuffle images
        random.shuffle(self.image_names)
        # assign each image name to a tkinter.PhotoImage
        self.image_dict = {name: tkinter.PhotoImage(file=os.path.join(
            folder, name)) for name in eight_file_images}

        # temporary variable to hold index of next image name in image_names
        temp = 0
        # find all tiles in the canvas and assign a new image name as a tag
        for tile in self.my_canvas.find_all():
            self.my_canvas.itemconfigure(tile, tag=self.image_names[temp])
            temp += 1

        # bind the left mouse button to the flip method
        self.my_canvas.bind("<Button-1>", self.flip)

        # Call the restart method to finish the initialization
        self.restart()

    def restart(self):
        """
        This method is invoked when player clicks on the RESTART button.
        It should also be called from __init__ to initialize the game.
        It shuffles and reassigns the images and resets the GUI and the
        score.
        :return: None
        """
        # delete all items with 'image' tag on canvas
        self.my_canvas.delete("image")
        # shuffle list of 16 images
        random.shuffle(self.image_names)
        # temporary variable to hold index of next image name in image_names
        temp = 0
        # find all tiles in the canvas and reassign a new image name as a tag
        for tile in self.my_canvas.find_all():
            self.my_canvas.itemconfigure(tile, fill='yellow',
                                         tag=self.image_names[temp])
            temp += 1

        # reset all variables that can be changes
        self.score = 100
        self.tries = 0
        self.pairs = 8
        self.score_label.configure(text=f'Score: {self.score}')

    def flip(self, event):
        """
        This method is invoked when the user clicks on a square.
        It implements the basic controls of the game.
        :param event: event (Event object) describing the click event
        :return: None
        """
        # get tags of clicked item on canvas
        tags = self.my_canvas.gettags(tkinter.CURRENT)
        # get image name from tags
        image_name = tags[0]
        # checks if item clicked is first tile
        if len(self.my_canvas.find_withtag('first')) == 0 and \
                self.my_canvas.itemcget(tkinter.CURRENT, 'fill') \
                != self.player_color \
                and 'first' not in tags:
            # add first tag to clicked item
            self.my_canvas.addtag_withtag('first', tkinter.CURRENT)
            # get coords of clicked item
            x1, y1, x2, y2 = self.my_canvas.coords(tkinter.CURRENT)
            # create image at center of clicked item
            self.image_id = self.my_canvas.create_image((x2 + x1) / 2,
                                                        (y2 + y1) / 2,
                                                        image=self.image_dict[
                                                            image_name],
                                                        tag='image')
        # check if clicked item is second tile
        elif len(self.my_canvas.find_withtag('first')) == 1 and len(
                self.my_canvas.find_withtag('second')) == 0 \
                and self.my_canvas.itemcget(tkinter.CURRENT, 'fill') \
                != self.player_color and 'first' not in tags:
            # add second tag to clicked item
            self.my_canvas.addtag_withtag('second', tkinter.CURRENT)
            # get coords of clicked item
            x1, y1, x2, y2 = self.my_canvas.coords(tkinter.CURRENT)
            # create image at center of clicked item
            self.image_id = self.my_canvas.create_image((x2 + x1) / 2,
                                                        (y2 + y1) / 2,
                                                        image=self.image_dict[
                                                            image_name],
                                                        tag='image')
            # second tile is chosen so can activate delay to hide images
            self.my_canvas.after(self.delay, self.hide)
            # user complete one full turn and game can adjust score
            self.check_score()

    def hide(self):
        """
        This method is called after a delay to hide the two tiles that
        were flipped.  The method will also change the tile color to the
        user specified color if there is a match.
        :return: None
        """
        # delete images on the canvas
        self.my_canvas.delete("image")

        # get id of first tile
        first_tile = self.my_canvas.find_withtag('first')
        # get id of second tile
        second_tile = self.my_canvas.find_withtag('second')
        # get image name tag correlating to first tile
        first_image = self.my_canvas.gettags(first_tile)[0]
        # get image name tag correlating to second tile
        second_image = self.my_canvas.gettags(second_tile)[0]

        # check if image names match
        if first_image == second_image:
            # fill both tiles with player color
            self.my_canvas.itemconfigure(first_tile,
                                         fill=self.player_color)
            self.my_canvas.itemconfigure(second_tile,
                                         fill=self.player_color)

            # decrease match count
            self.pairs -= 1
            # check if player matched all tiles
            self.check_win()

        # delete tiles with 'first' and 'second' tag to reset for another try
        self.my_canvas.dtag('first')
        self.my_canvas.dtag('second')

    # Enter your additional method definitions below
    # Make sure they are indented inside the MatchGame class
    # Make sure you include docstrings for all the methods.

    def check_score(self):
        """
        Adjust the score and score label of game
        :return: None
        """
        # increase number of tries
        self.tries += 1
        # decrease score if over 13 tries
        if self.tries > 13:
            self.score -= 10
            self.score_label.configure(text=f'Score: {self.score}')

    def check_win(self):
        """
        Check if all tiles are matched and change score label to game over
        message
        :return: None
        """
        if self.pairs == 0:
            self.score_label.configure(text=f'Game Over!\nScore: '
                                            f'{self.score}\n Number of '
                                            f'tries: {self.tries}')


# Enter any function definitions here to get and validate the
# command line arguments.  Include docstrings.
def valid_images(image_folder):
    """
    Validate contents in directory:
    - at least 8 gif files
    :param image_folder: (string) name of directory
    :return: (string) valid directory name
    """
    if not os.path.exists(image_folder):
        raise argparse.ArgumentTypeError(f'{image_folder} is not a valid '
                                         f'folder')
    files = [file for file in os.listdir(image_folder) if file.endswith(
        '.gif')]
    # files = [file for file in os.listdir(image_folder) if not file.endswith(
    #     '.gif')]
    # if len(files) > 0:
    #     raise argparse.ArgumentTypeError(f'{image_folder} must contain '
    #                                      f'gif images')
    if len(files) < 8:
        raise argparse.ArgumentTypeError(f'{image_folder} must contain at '
                                         f'least 8 gif images')
    return image_folder


def get_arguments():
    """
    Parse and validate the command line arguments.
    :return: tuple containing the player color (string), the image
    folder (string) and the fast option (boolean)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('color',
                        help='What color would you like for the player?',
                        choices=['blue', 'green', 'magenta'])
    parser.add_argument('image_folder',
                        help='What folder contains the game images?',
                        type=valid_images,
                        nargs='?',
                        default='images')
    parser.add_argument('-f', '--fast',
                        help='fast or slow game?',
                        action='store_true')
    arguments = parser.parse_args()
    color = arguments.color
    image_folder = arguments.image_folder
    fast = arguments.fast
    return color, image_folder, fast


def main():
    # Retrieve and validate the command line arguments using argparse
    # Instantiate a root window
    # Instantiate a MatchGame object with the correct arguments
    # Enter the main event loop
    color, image_folder, fast = get_arguments()
    root = tkinter.Tk()
    MatchGame(root, color, image_folder, fast)
    root.mainloop()


if __name__ == '__main__':
    main()
