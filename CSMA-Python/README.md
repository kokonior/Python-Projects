# CSMA

SourceCode and detailed report on One, Non and P-persistent CSMA techniques.

* To simulate the project properly-

    1. Change values of variables in ```const.py``` according to your wish. (Specially ```total_sender_number``` and ```total_receiver_number```).\
    Make sure that ```total_sender_number``` = ```total_receiver_number```.

    2. You need to create as many number of input files in ```./src/textfiles/input/``` as the integer value you store in ```total_sender_number```.\
    If ```total_sender_number``` > **number of input files**, the program may throw exceptions and desired results may not show up.

    3. Now make sure you're in the ```./src``` folder and run ```python3 main.py``` in the terminal **after deleting the ```./src/textfiles/report.txt```\
    and ```./src/textfiles/analysis.txt``` files** and also writing **Only '0'** (if anything else or nothing is written) in ```./src/textfiles/collision.txt```.

    4. Keep track of the live changes made on the newly generated ```analysis.txt``` and ```report.txt``` after choosing your desired CSMA\
     technique from the command line.

    5. Press ```ctrl+c``` twice to stop the simulation.
