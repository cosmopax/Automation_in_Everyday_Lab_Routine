# 0000000000000000000000000000000000000000
#    FLOW CHEM CALCULATOR 1.0
# 0000000000000000000000000000000000000000
#
#  Automatisierung im Laboralltag
#  Gruppe 4 - Kurs 1
#  Fynnius Monarth
#  Annika Prüher
#  Hannah Riedmüller
#  David Meiffert
#
# -------------------------
# Version 1.0 - 25.06.2025
# -------------------------
#
# Note: one might say writing a program without importing any libraries is
# inefficient or stupid, but we know students and that many would not install
# dependencies if this program would not work for them. So we just had easiest 
# possible usability in mind.
# 

#=============== general stuff ================================================

def get_float_input(prompt: str) -> float:
    '''
    Keep asking the user for input until a valid float input is provided.

    Parameters
    ----------
    prompt : str
        Input prompt for the user.

    Returns
    -------
    float
        The validated input, converted to float.
    '''
    while True:
        user_input = input(prompt)
        try:
            float(user_input)
            return float(user_input)
        except:
            print('Not a valid input, use . as comma.')


#=============== TASK 1 - small calculations ================================================
# to understand these headers reading the main programm at the bottom of the file would
# be advisable

def get_calculationdata() -> float:
    '''
    Takes inputs for two values that are needed for calculation depending
    on what should be calculated.

    Parameters
    ----------
    none

    Returns
    -------
    volume: float
        volume of reactor in mL
    length: float
        length of tube in mm
    diameter: float
        diameter of tube in mm
    '''
    
    print('')
    print('What do you want to calculate?')
    print('1 - Volume')
    print('2 - Length')
    print('3 - Diameter') #why would someone need to do that???
    
    while True:
        print('')
        task = input('Enter 1, 2 or 3: ').strip()
        print('')

        if task in ['1','2','3']:

            if task == '1':
                length = get_float_input('Tube length [mm]: ')
                diameter = get_float_input('Tube diameter [mm]: ')
                volume = 0
                return volume, length, diameter
                
            elif task == '2':
                length = 0
                diameter = get_float_input('Tube diameter [mm]: ')
                volume = get_float_input('Reactor volume [mL]: ')
                return volume, length, diameter
                
            elif task == '3':
                length = get_float_input('Tube length [mm]: ')
                diameter = 0
                volume = get_float_input('Reactor volume [mL]: ')
                return volume, length, diameter
                
            else:
                print('An error occoured')
                            
        else:
            print('Invalid input')            


def calculate_reactorvalue(volume: float, length: float, diameter: float) -> float:
    '''
    Takes volume, length and diameter, one of which can be 0 and calculates the missing value.
    Via V = r²*pi*h

    Parameter
    ---------
    volume: float
        Reactor volume in mL
    length: float
        Reactor length in mm
    diameter: float
        Tube diameter in mm

    Returns
    -------
    float
        calculated value
    '''

    r = diameter / 2

    if volume == 0:
        # calculate volume
        volume_mm3 = 3.14159265359 * r**2 * length
        return [(volume_mm3 / 1000), 'volume', 'mL']  # convert mm³ to mL

    elif length == 0:
        # calculate length
        volume_mm3 = volume * 1000
        return [(volume_mm3 / (3.14159265359 * r**2)), 'lenght', 'mm']

    elif diameter == 0:
        # calculate diameter
        volume_mm3 = volume * 1000
        length = length or 1e-9  # prevent div by 0
        d = ((4 * volume_mm3) / (3.14159265359 * length))**(1/2)
        return [d, 'diameter', 'mm']

    else:
        print("Nothing to calculate. All values provided.")
        return None


#================= TASK 2 - a full reaction setup ==============================

#=======================================
#     SET REACTORS
#=======================================

def set_reactors() -> list:
    '''
    Saves reactor proporties in a list of dicts. Dicts are
    written by get_reactordata()
    
    Parameter
    ---------
    none

    Returns
    -------
    reactors: list
        list of dicts
    '''
    reactors = []
    reactornumber = 1

    print('')
    print(f'--- Add Reactor {reactornumber} ---')
    reactor = get_reactordata(reactornumber)
    reactors.append(reactor)

    while True:
        print('')
        print('Do you want to add another reactor?')
        print('1 - Yes')
        print('2 - No')
        print('3 - Delete last reactor that was added')
        task = input('Enter 1, 2 or 3: ')

        if task == '1':
            reactornumber += 1
            print('')
            print(f'--- Add Reactor {reactornumber} ---')
            reactor = get_reactordata(reactornumber)
            reactors.append(reactor)
            continue
            
        elif task == '2':
            if len(reactors) < 1:
                print('')
                print('You need to add at least one reactor.')
            else:
                break
            
        elif task == '3':
            reactors = delete_lastlistelement(reactors, 'Reactor', reactornumber)
            reactornumber -= 1
            continue
            
        else:
            print('Invalid input.')
            continue

    return reactors


def get_reactordata(reactornumber: int) -> dict:
    '''
    Asks for custom name, vol, len, diam -> calcs missing value if one is 0 using calculate_reactorvalue()
    Function can be reused for each reactor that is added.

    Parameter
    ---------
    reactornumber: int
        number of reactor to note it in the returning dict

    Returns
    -------
    dict
        dict of current reactor
        reactor number: int, custom name: str, volume: float, length: float, 
        diameter: float, inputs: list, outputs: list
    '''
    
    name = input('Enter custom reactor name: ')
    print('')

    print('Enter reactor parameters (one value can be 0 to calculate it automatically).')
    length = get_float_input('Tube length [mm]: ')
    diameter = get_float_input('Tube diameter [mm]: ')
    volume = get_float_input('Reactor volume [mL]: ')

    # If one value is zero, calculate it
    if volume == 0 or length == 0 or diameter == 0:
        result = calculate_reactorvalue(volume, length, diameter)
        if volume == 0:
            volume = result[0]
        elif length == 0:
            length = result[0]
        elif diameter == 0:
            diameter = result[0]
        print('Calculated', result[1], 'is: ', '%0.3f' % result[0], result[2])

    # Return as a reactor dictionary
    return {
        'number': reactornumber,
        'name': name,
        'volume': volume,
        'length': length,
        'diameter': diameter,
        'inputs': [],
        'outputs': []
    }


#=======================================
#     SET SYRINGES
#=======================================

def set_syringes() -> list:
    '''
    Saves syringe proporties in a list of dicts. Dicts are generated
    by get_syringedata().

    Parameter
    ---------
    none

    Returns
    -------
    syringes: list
        list of dicts
    '''
    syringes = []
    syringenumber = 1

    print('')
    print(f'--- Add Syringe {syringenumber} ---')
    syringe = get_syringedata(syringenumber)
    syringes.append(syringe)

    while True:
        print('')
        print('Do you want to add another syringe?')
        print('1 - Yes')
        print('2 - No')
        print('3 - Delete last syringe that was added.')        
        task = input()

        if task == '1':
            syringenumber += 1
            print(f'--- Add Syringe {syringenumber} ---')
            syringe = get_syringedata(syringenumber)
            syringes.append(syringe)
            continue
            
        elif task == '2':
            if len(syringes) < 1:
                print('')
                print('You need to add at least one syringe.')
            else:
                break
            
        elif task == '3':
            syringes = delete_lastlistelement(syringes, 'Syringe', syringenumber)
            syringenumber -= 1
            continue
            
        else:
            print("Invalid input. Assuming 'No'.")
            break

    return syringes

    
def get_syringedata(syringenumber: int)-> dict:
    '''
    Asks for syringe data and writes it into a dict.

    Parameters
    ----------
    syringenumber: int
        current syringe to be noted in the dict

    Returns
    -------
    dict
        dict of current syringe
        syringe number: int, custom name: str, volume: float, connected to: reactornumber:int,
        flow rate: float
    '''
    name = input('Enter custom syringe name (e.g. chemical name): ')
    volume = get_float_input('Syringe volume [mL]: ')

    return {
        'number': syringenumber,
        'name': name,
        'volume': volume,
        'connected_to': None,
        'flow_rate': None
    }


#=======================================
#     DELETE LAST REACTOR/SYRINGE
#=======================================

def delete_lastlistelement(original_list: list, itemname: str, number: int) -> list:
    '''
    Removes list item corresponding to number.

    Parameter
    ---------
    original_list: list
        syringes or reactors or any other list of dicts with element 'number'
    itemname: str
        name of list item, e.g. syringe or reactor
    number: int
        list item to remove

    Return
    ------
    list
        list minus deleted element
    '''

    for element in original_list:
        if element['number'] == number:
            original_list.remove(element)
            break

    print('')
    print(itemname, number, 'was deleted.')
    print(len(original_list), itemname+'s', 'are left.')
    print('')
    
    return original_list


#=======================================
#     CONNECTING SETUP PARTS
#=======================================

def connect_elements(reactors: list, syringes: list):
    '''
    Connects reactors and syringes by setting i/o and connected to
    values in reactors and syringes list

    Parameter
    ---------
    reactors: list
        reactor list of dicts
    syringes: list
        syringe list of dicts

    Returns
    -------
    tuple
        reactors, syringes
    '''
    
    all_reactors = {r['number']: r for r in reactors}
    all_syringes = {s['number']: s for s in syringes}

    print('')
    print("Let's connect the elements now!")
    for syringe in syringes:
        while True:
            print('')
            print(f'Syringe {syringe['number']} ({syringe['name']}) should connect to reactor:')
            for reactor in reactors:
                print(f'{reactor['number']} - Reactor {reactor['number']} ({reactor['name']})')
            choice = input('Enter corresponding reactor number: ')
    
            try:
                choice = int(choice)
                if choice not in all_reactors:
                    print('Reactor ', choice, ' does not exist.')
                    continue
                
                if syringe['connected_to'] is not None:
                    print(f'This syringe is allready connected to {syringe['connected_to']}!')
                    break

                syringe['connected_to'] = choice
                all_reactors[choice]['inputs'].append(('s',syringe['number']))
                print('Connected!')
                break
                
            except:
                print('Invlaid input, please enter a valid integer.')

    output_connected = False

    for reactor in reactors:
        while True:
            print('')
            print(f'Reactor {reactor['number']} ({reactor['name']}) should connect to output or reactor:')
            print('0 - Output (there can only be one output)')
            for r in reactors:
                if r['number'] != reactor['number']:
                    print(f'{r['number']} - Reactor {r['number']} ({r['name']})')
            choice = input('Enter corresponding number: ')

            try:
                choice = int(choice)
                if choice == 0:
                    if output_connected:
                        print('Output is already connected to another reactor!')
                        continue
                    reactor['outputs'].append('product')
                    output_connected = True
                    print('Connected to product output!')
                    break
                    
                elif choice == reactor['number']:
                    print('Reactor cannot connect to itself.')
                    
                elif has_path(choice, reactor['number'], reactors):
                    print('This connection would create a loop! Please choose another reactor.')
                    
                else:
                    reactor['outputs'].append(choice)
                    all_reactors[choice]['inputs'].append(('r',reactor['number']))
                    print('Connected!')
                    break
            except:
                print('Invlaid input, please enter a valid integer.')

    return reactors, syringes
    

def has_path(start, target, reactors, visited=None):
    '''
    Checks whether a path exists from `start` reactor to `target` reactor using DFS.

    Used to prevent creating cycles in the reactor network:
    - If a path exists from `start` to `target`, then connecting `target` to `start`
      would form a loop, so the function returns True.
    - If no such path exists, it is safe to connect, and the function returns False.

    Parameters
    ----------
    start : int
        Reactor number where the search begins.
    target : int
        Reactor number to reach.
    reactors : list
        List of reactor dictionaries, each containing 'number' and 'outputs'.
    visited : set, optional
        Set of reactor numbers already visited (used for recursion).

    Returns
    -------
    bool
        True if a path exists from start to target (which would cause a loop), False otherwise.    

    Note
    ----
    This function was written by ChatGPT bc I had no brain energy for thinking about how to go
    through the reactor and check for potential loops.
    '''
    
    if visited is None:
        # If this is the first function call, initialize an empty set to keep track of visited reactors.
        visited = set()

    if start == target:
        # If the reactor we're currently checking is the same as the target reactor, a path exists.
        # This is the success condition: we found a connection.
        return True

    # Add the current reactor to the set of visited reactors to prevent revisiting it (avoiding infinite loops).
    visited.add(start)

    # Find the reactor dictionary that matches the current reactor ID (start).
    start_reactor = next((r for r in reactors if r['number'] == start), None)

    if not start_reactor:
        # If the reactor is not found in the list (probably an invalid ID), stop searching this path.
        return False

    # Loop through all outputs (connected reactors) from the current reactor.
    for out in start_reactor['outputs']:
        # If the output is a reactor number (int) and we haven't visited it yet:
        if isinstance(out, int) and out not in visited:
            # Recursively check if a path exists from this output to the target reactor.
            if has_path(out, target, reactors, visited):
                # If any recursive call finds a path, return True immediately (path exists).
                return True

    # If we’ve checked all outputs and none lead to the target reactor, return False (no path exists from here).
    return False

    
#=======================================
#     1 - CALCULATE REACTOR VOLUME
#=======================================

def calculate_reactorvolume(reactors: list) -> float:
    '''
    Calculates total reactor volume.
    Allows user to add connection tubes into the volume aswell if wanted.

    Parameter
    ---------
    reactors: list
        list of all reactors and their properties

    Returns
    -------
    float
        Reactor Volume
    '''

    total_volume = 0

    print('Do you want to add connector tubes for more precision?')
    print('(This can usually be ignored if they are not any longer than needed)')
    print('')
    print("1 - Yes, let's add the connector tubes volumes.")
    print("2 - No, the connector tubes are short enough.")
    task = input()
    tubenumber = 1

    if task == '1':
        while True:
            print('')
            print(f'--- Add Tube {tubenumber} ---')
            total_volume += get_tube()

            print('')
            print('Do you want to add another tube?')
            print('1 - Yes')
            print('2 - No')
            print('3 - Delete tube volume')
            task = input('Enter 1, 2 or 3: ').strip()

            if task == '1':
                tubenumber += 1
                continue
            elif task == '2':
                break
            elif task == '3':
                print('To delete a entered tube volume you have to reinput previously typed parameters.')
                print('--- REMOVE TUBE ---')
                new_volume = total_volume - get_tube()
                if new_volume < 0:
                    print('Volume cannot be less than 0, therefore tube will not be removed.')
                    continue
                total_volume = new_volume
            else:
                print("Invalid input. Assuming 'No'.")
                break
                print('')
                
        for reactor in reactors:
            total_volume += reactor['volume']
    else:
        if task != '2':
            print("Invalid input. Assuming 'No'.")
            
        for reactor in reactors:
            total_volume += reactor['volume']

    return total_volume
        

def get_tube() -> float:
    '''
    Asks for connecor tube properties and passes volume back.

    Parameters
    ----------
    none

    Returns
    -------
    float
        volume of connecor tube
    '''
    
    print('Enter tube parameters (one value can be 0 to calculate it automatically).')
    length = get_float_input('Tube length [mm]: ')
    diameter = get_float_input('Tube diameter [mm]: ')
    volume = get_float_input('Tube Volume [mL]: ')

    # If one value is zero, calculate it
    if volume == 0:
        result = calculate_reactorvalue(volume, length, diameter)
        volume = result[0]
        print('Calculated', result[1], 'is: ', '%0.3f' % result[0], result[2])    

    return volume


#=======================================
#     2 - CALC FLOW RATE
#=======================================

def calculate_flowrates(reactorvolume: float, retention_time: float, syringes: list) -> list:
    '''
    Uses reactorvolume and retention time wanted to calculate flowrates needed.

    Parameter
    ---------
    reactorvolume: float
        total reactorvolume in mL
    retention_time: float
        wanted retention time in min
    syringes: list
        List of all syringes and their properties

    Returns
    -------
    syringes: list
        list of dicts with flow rate in mL/min added to them
    '''
    
    connections = [] #all connected_to values of each syringe starting at syringe 1,..
    counted = [] #list to avoid double counting
    connection_counts = [] # list of tuples (reactornumber, count)
    
    for syringe in syringes:
        connections.append(syringe['connected_to'])

    for reactornumber in connections:
        if reactornumber not in counted:
            count = connections.count(reactornumber)
            connection_counts.append((reactornumber, count))
            counted.append(reactornumber)

    max_tuple = max(connection_counts, key=lambda t: t[1])
    max_syringe_count = max_tuple[1]

    virtual_syringecount = max_syringe_count * len(connection_counts) #how many syringes need to be assumend

    virtual_singleflow = reactorvolume / (virtual_syringecount * retention_time) # flow of a virtual syringe

    # assigns flowrates
    for syringe in syringes:
        connected_reactor = syringe['connected_to']

        n_syringes = 1 #default if not found but should not happen but i dont want to delete it in case it happens lol
        for (r, count) in connection_counts:
            if r == connected_reactor:
                n_syringes = count
                break

        factor = max_syringe_count / n_syringes
        flow = virtual_singleflow * factor
        syringe['flow_rate'] = flow
    
    return syringes


def print_flowrates(syringes: list) -> None:
    '''
    Takes syringes list and prints syringe number, name and flowrate.

    Parameter
    ---------
    syringes: list
        list of dicts

    Returns
    -------
    None
    '''

    print('')
    print('========= FLOW RATES =========')
    print('')
    for syringe in syringes:
        print('Syringe ',syringe['number'], '(', syringe['name'], '): ', f"{syringe['flow_rate']:.6f}", 'mL/min')

    return


#=======================================
#     3 - CALC RETENTION TIME
#=======================================

def get_flowrates(syringes: list) -> list:
    '''
    Asks for flow rates to set them.

    Parameter
    ---------
    syringes: list
        list of dicts

    Return
    ------
    syringes: list
        list of dicts with flowrate values added
    '''

    print("Let's set needed flowrates!")
    print('')

    for syringe in syringes:
        print(f'--- Syringe {syringe['number']} ({syringe['name']}) ---')
        if syringe['flow_rate'] is not None:
            print('There is already a flow rate set to:', f"{syringe['flow_rate']:.6f}", ' mL/min for this syringe.')
            print('This will be overwritten with your new flowrate.')
            print('(or enter the same flow rate to keep the old one)')
            print('')
        rate = get_float_input('Enter your desired flow rate [mL/min]: ')
        print('')
        syringe['flow_rate'] = rate

    return syringes


def calculate_retentiontime(reactorvolume: float, syringes: list) -> float:
    '''
    Calculates retention time based on given flowrates and the reactor volume

    Parameter
    ---------
    reactorvolume: float
        reactor volume in mL
    syringes: list
        list of dicts

    Returns
    -------
    float
        retention time
    '''
    inflow = 0
    
    for syringe in syringes:
        inflow += syringe['flow_rate']

    retention_time = reactorvolume / inflow

    return retention_time
    

#=======================================
#     4 - SHOW SETUP
#=======================================

def print_setup(reactors: list, syringes: list, reactorvolume: float, retention_time: float) -> None:
    '''
    Prints current settings to allow looking at them.

    Parameter
    ---------
    reactors: list
        list of dicts
    syringes: list
        list of dicts
    reactorvolume: float
        volume of reactor in mL
    retention_time:
        retention time of setup in minutes

    Returns
    -------
    none
        prints a lot of stuff
    '''

    print('')
    print('Note: This will only show data that was put in/calculated, if something is 0 or empty that\nis becuase you need to calculate it first using the other options.')
    print('')
    print('================ REACTION SETUP ================')
    print('')
    print(f'Total Volume [mL]         : {reactorvolume:.3f}')
    print(f'Total Retention Time [min]: {retention_time:.3f}')
    print('')
    print('------------------- REACTORS -------------------')
    print('')

    for reactor in reactors:
        print(f'Reactor {reactor['number']}: {reactor['name']}')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'Volume [mL]  : {reactor['volume']:.3f}')
        print(f'Length [mm]  : {reactor['length']}')
        print(f'Diameter [mm]: {reactor['diameter']}')
        print(f'Output: {reactor['outputs']}')
        print('')

    print('')
    print('------------------- SYRINGES -------------------')
    print('')

    for syringe in syringes:
        print(f'Syringe {syringe['number']}: {syringe['name']}')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'Volume [mL]  : {syringe['volume']:.3f}')
        print(f'Connected to: Reactor {syringe['connected_to']}')
        if syringe['flow_rate'] is not None:
            print(f'Flow rate [mL/min]: {syringe['flow_rate']:.6f}')
        else:
            print(f'Flow rate [mL/min]: not calculated yet')
        print('')

    return

def write_setup(reactors: list, syringes: list, reactorvolume: float, retention_time: float, filename) -> None:
    '''
    Writes current settings to a .txt file allow looking at them.

    Parameter
    ---------
    reactors: list
        list of dicts
    syringes: list
        list of dicts
    reactorvolume: float
        volume of reactor in mL
    retention_time:
        retention time of setup in minutes
    filename: str
        filename that will be used to save

    Returns
    -------
    none
        saves filename.txt containing current setup
    '''

    filename = filename + '.txt'
    with open(filename, 'w') as file:

        file.write('Note: This will only show data that was put in/calculated, if something is 0 or empty that\nis becuase you need to calculate it first using the other options.')
        file.write('\n')
        file.write('\n')
        file.write('================ REACTION SETUP ================\n')
        file.write('\n')
        file.write(f'Total Volume [mL]         : {reactorvolume:.3f}\n')
        file.write(f'Total Retention Time [min]: {retention_time:.3f}\n')
        file.write('\n')
        file.write('------------------- REACTORS -------------------\n')
        file.write('\n')
    
        for reactor in reactors:
            file.write(f'Reactor {reactor['number']}: {reactor['name']}\n')
            file.write('~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            file.write(f'Volume [mL]  : {reactor['volume']:.3f}\n')
            file.write(f'Length [mm]  : {reactor['length']}\n')
            file.write(f'Diameter [mm]: {reactor['diameter']}\n')
            file.write(f'Output: {reactor['outputs']}\n')
            file.write('\n')
    
        file.write('\n')
        file.write('------------------- SYRINGES -------------------\n')
        file.write('\n')
    
        for syringe in syringes:
            file.write(f'Syringe {syringe['number']}: {syringe['name']}\n')
            file.write('~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            file.write(f'Volume [mL]  : {syringe['volume']:.3f}\n')
            file.write(f'Connected to: Reactor {syringe['connected_to']}\n')
            if syringe['flow_rate'] is not None:
                print(f'Flow rate [mL/min]: {syringe['flow_rate']:.6f}')
            else:
                print(f'Flow rate [mL/min]: not calculated yet')
            file.write('\n')

    print('')
    print(f'File saved as {filename}!\n')

    return


#=======================================
#     MAIN NO 2 FUNCTION
#=======================================

def do_no2(): #everyone needs to do no2 from time to time
    '''
    Main Function doing Task number 2.
    '''
    reactorvolume = 0
    retention_time = 0
    
    print("Let's set up your reactor!")
    print('Choose a name for your project!')
    print('You can generate a file later using that projet name, \nso dont use any symbols that dont belong into a file name (e.g. .)')
    filename = input('Filename: ').strip()
    
    reactors=set_reactors()
    syringes=set_syringes()
    reactors, syringes = connect_elements(reactors, syringes) #function that allows connecting syringes to elements
    
    print('')
    print('Your reaction is now set up!')
    
    while True:
        print('What do you want to do next?')
        print('1 - calculate total reactor volume')
        print('2 - calculate flowrates by providing wanted retention time')
        print('3 - calculcate retention time by providing flowrates')
        print('4 - show setup data')
        print('5 - write setup data to a file')
        print('x - exit')
        task = input().strip()
        
        if task == '1':
            print('========== Calculate Reactor Volume ==========')
            print('Note: The following calculated total reactor volume will be reused for any other calulations. (e.g. option 2 and 3)')
            print('')
            reactorvolume = calculate_reactorvolume(reactors)
            print(f'Total reactor volume is {reactorvolume:.3f}')
        
        elif task == '2':
            if reactorvolume == 0:
                print('We need to calculate the reactor volume first:')
                print('')
                reactorvolume = calculate_reactorvolume(reactors)
            print('')
            retention_time = get_float_input('Provide your wanted retention time [min]: ')
            syringes = calculate_flowrates(reactorvolume, retention_time, syringes)
            print_flowrates(syringes)

        elif task == '3':
            if reactorvolume == 0:
                print('We need to calculate the reactor volume first:')
                print('')
                reactorvolume = calculate_reactorvolume(reactors)
            print('')
            syringes = get_flowrates(syringes)
            retention_time = calculate_retentiontime(reactorvolume, syringes)
            print(f'Retention time of your setup [min]: {retention_time:.2f}')
            print('')

        elif task == '4':
            print_setup(reactors, syringes, reactorvolume, retention_time)

        elif task == '5':
            write_setup(reactors, syringes, reactorvolume, retention_time, filename)
        
        elif task == 'x':
            print('EXIT reaction setup calculations')
            print('')
            break

        else:
            print('Invalid task input.')
            print('')

    return

#================================================
#    MAIN PROGRAMM
#================================================

print('=====================================')
print('\tFLOW CHEM CALCULATOR 1.0')
print('=====================================')
print('')

print('If the programm lists you options always enter the integer corresponding to what you want to do!')
print("Let's give it a try:")
print('')

while True:
    print('What do you want to do?')
    print('1 - Calculate Reactor Property (Volume, Length, Diameter - enter 2 get the 3rd one)')
    print('2 - Calculations for a full set up. Enter reactors and syringes, calculate volumes, flow rates or retention time.')
    print('x - exit')
    print('')
    task = input('Enter either 1 or 2: ').strip()
    print('')
    
    if task == '1':
        volume, length, diameter = get_calculationdata()
        result = calculate_reactorvalue(volume, length, diameter)
        print('')
        print(f'Your {result[1]} is: {result[0]:.3f} {result[2]}')
        print('')
        
    elif task == '2':
        do_no2()

    elif task == 'x':
        break
    
    else:
        print(task,' is not a valid input.')

exit()