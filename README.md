# covidstates
jupyter notebook for comparing two American states in regards Covid-19 deaths

Assuming you are at a command line of the home directory of this repo, and have python3 installed, and pip, you can do this:
=========================================
pip3 install -r requirements.txt 
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter notebook


This should open a tab in your browser with the http://localhost:8888/tree home page.  Click on "CompareTwoStatesCovid-19.ipynb",
which will open another tab for this notebook.  Click on the "Cell" menu, and then "Run All". Scroll down a bit and select two states
from the dropdowns, and generate your plot.

If you want to save the images, uncomment this line:

#plt.savefig('/home/rossdavidh/Desktop/'+state1+'_'+state2+'.png', bbox_inches='tight')

...but obviously you will need to change the directory to somewhere on your computer.

