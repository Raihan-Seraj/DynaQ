# Copyright 2017 the pycolab Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""An example implementation of the classic blocking-maze problem."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import sys
import copy
from pycolab import ascii_art
from pycolab import human_ui
from pycolab.prefab_parts import sprites as prefab_sprites

GAME_ART = ['###########',
            '#         #',
            '#         #', 
            '#         #',
            '#         #',              
            '#*#######.#',        
            '#   !     #', 
            '###########']
          


GAME_ART_LONG=['##########',
               '#        #',
               '#        #', 
               '#        #',
               '#        #',              
               '# ########',        
               '#        #', 
               '##########'
                          ]
          


def make_game():
  """Builds and returns a blocking_maze_game."""
  return ascii_art.ascii_art_to_game(
      GAME_ART, what_lies_beneath=' ',
      sprites={'!': PlayerSprite})








class PlayerSprite(prefab_sprites.MazeWalker):
  """A `Sprite` for our player.

  This `Sprite` ties actions to going in the four cardinal directions. If it
  walks into all but the first and last columns of the bottom row, it receives a
  reward of -100 and the episode terminates. Moving to any other cell yields a
  reward of -1; moving into the bottom right cell terminates the episode.
  """

  def __init__(self, corner, position, character):
    """Inform superclass that we can go anywhere, but not off the board."""
    super(PlayerSprite, self).__init__(
        corner, position, character, impassable='#,*', confined_to_board=True)
    #position=copy.deepcopy(self.position)
    self.naaam='abc'
    #self.counter=copy.deepcopy(self.counter)
    #the_plot.add_reward(0)

  def update(self, actions, board, layers, backdrop, things, the_plot,ctr):
    #print('Hi',ctr)
    del layers, backdrop, things   # Unused.
    if self.position==(6,4):
    	the_plot.add_reward(0)
    if ctr>=1000:      
      super(PlayerSprite,self).__init__(self.corner,self.position,self.character,impassable='#,.',confined_to_board=True)
      ascii_art.ascii_art_to_game(GAME_ART_LONG,what_lies_beneath='.')
    
    # Apply motion commands.
    if actions == 0:    # walk upward?
      
      self._north(board, the_plot)
    elif actions == 1:
     
      self._south(board, the_plot)
    elif actions == 2:
      
      self._west(board, the_plot)
    elif actions == 3:
      
      self._east(board, the_plot)
      
      # Let the game begin!
      #ui.play(game2)


      
          
    else:
      # All other actions are ignored. Although humans using the CursesUi can
      # issue action 4 (no-op), agents should only have access to actions 0-3.
      # Otherwise staying put is going to look like a terrific strategy.
      return

    # See what reward we get for moving where we moved.
    if (self.position ==(1,9)):
       
      the_plot.add_reward(1)  # get the reward.
    else:
      the_plot.add_reward(0)

    # See if the game is over.
    if self.position == (1,9):
    	the_plot.terminate_episode()
      
  def reset(self):
  	super(PlayerSprite,self).reset()

def main(argv=()):
  del argv  # Unused.

  # Build a blocking-maze game.
  game = make_game()

  # Make a CursesUi to play it with.
  ui = human_ui.CursesUi(
      keys_to_actions={curses.KEY_UP: 0, curses.KEY_DOWN: 1,
                       curses.KEY_LEFT: 2, curses.KEY_RIGHT: 3,
                       -1: 4},
      delay=200)

  # Let the game begin!
  ui.play(game)


if __name__ == '__main__':
  main(sys.argv)
