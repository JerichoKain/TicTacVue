
# coding: utf-8

# ## Setup ##
# If you have not already done so, install selenium with the command ```pip install selenium```

# In[73]:


get_ipython().run_line_magic('pushd', 'lib')
get_ipython().run_line_magic('run', 'TicTacToeApp.ipynb')
get_ipython().run_line_magic('popd', '')


# This is a test to Open a webdriver for to correct address (local)

# In[74]:


import time
from selenium import webdriver

##driver = webdriver.Chrome(r'C:\Projects\TicTacVue\chromedriver.exe')
driver = webdriver.Firefox(executable_path=r'C:\Projects\TicTacVue\geckodriver.exe')
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()


# In[76]:


import unittest
import time
from datetime import date
from selenium.common.exceptions import NoSuchElementException

class Winner(unittest.TestCase):
    def test_00_init(self):
        comp = app.get_component(self, "Game")
        self.assertEqual(len(comp.get_available_cells()), 9)
                         
    def test_01_cross_takes_NW(self):
        comp = app.get_component(self, "Game")
        comp.click_cell('NW')
        data['crosses'] = comp.get_cells_of_type('cross')
        self.assertEqual(len(data['crosses']), 1)
        self.assertTrue('NW' in data['crosses'])
        data['noughts'] = comp.get_cells_of_type('nought')
        self.assertEqual(len(data['noughts']), 1)
        self.assertTrue('C' in data['noughts'])
    
    def test_02_cross_takes_SE(self):
        comp = app.get_component(self, "Game")
        comp.click_cell('SE')
        data['crosses'] = comp.get_cells_of_type('cross')
        self.assertEqual(len(data['crosses']), 2)
        self.assertTrue('SE' in data['crosses'])
        data['noughts'] = comp.get_cells_of_type('nought')
        self.assertEqual(len(data['noughts']), 2)
        new_nought = [c for c in data['noughts'] if len(c) > 1]
        self.assertEqual(len(new_nought), 1)
        self.assertTrue(new_nought[0] in ['NE', 'SW']) #BUG?
    
    def test_03_cross_takes_open_corner_and_win_game(self):
        comp = app.get_component(self, "Game")
        available = comp.get_available_cells()
        corner = [a for a in available if len(a) > 1][0]
        comp.click_cell(corner)
        data['crosses'] = comp.get_cells_of_type('cross')
        self.assertEqual(len(data['crosses']), 3)
        data['noughts'] = comp.get_cells_of_type('nought')
        self.assertEqual(len(data['noughts']), 3)
        winning_moves = list(corner)
        available = comp.get_available_cells()
        next_move = winning_moves[0] if winning_moves[0] in available else winning_moves[1]
        comp.click_cell(next_move)
    
    def test_04_score_updated_and_game_cleared(self):
        comp = app.get_component(self, "Score")
        comp.has_score_of_type(1, "Wins")
        comp.has_score_of_type(0, "Loses")
        comp.has_score_of_type(0, "Draws")
        
        comp = app.get_component(self, "Game")
        self.assertEqual(len(comp.get_available_cells()), 9)


# In[77]:


if __name__ == '__main__':
    data = {
        'crosses': [],
        'noughts': [],
    }
    app = TicTacToeApp()
    app.wd.execute_script('localStorage.clear()')
    #argv and exit are set because jupyter
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    # close the window & driver
    del app


# In[85]:


app = TicTacToeApp()


# In[86]:


app.wd.execute_script('location.reload()')
comp = app.get_component(None, "Game")
comp.click_cell('C')
data['crosses'] = comp.get_cells_of_type('cross')
# self.assertEqual(len(data['crosses']), 1)
# self.assertTrue('C' in data['crosses'])
print(data['crosses'])
data['noughts'] = comp.get_cells_of_type('nought')
# self.assertEqual(len(data['noughts']), 1)
# self.assertTrue(len(data['noughts'][0]) == 2)
print(data['noughts'])
print(comp.get_available_cells())


# In[82]:


del comp
del app

