# Agenda file consolidation

## Why and what
The faculty senate agendas normally have several hyperlinks to documents discussed during the meeting. 

Given the impermanence of links, to store the agenda for posterity, we need all the linked files to be included with the agenda in a single file. 

That's what this tool does. When it is run, it downloads all the linked files and then merges them into a copy of the original.

## Instructions
0. Remove any previously processed files from the To Process folder.

1. Place the files to be processed in the 'To Process' folder. 

2. Click 'run_agenda_consolidation.py' (or, from the command line, run it with python run_agenda_consolidation.py).

3. Check the log for any errors --- sometimes a file cannot be found or downloaded. Those will need to be handled manually.

4. Retrieve the processed file from the 'Output' folder.