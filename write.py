"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    
    # TODO: Write the results to a CSV file, following the specification in the instructions.
    with open(filename, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames)
        writer.writeheader()

        for elem in results:
            message=elem.serialize() 
            message2=elem.neo.serialize() 

            for key, value in message2.items():
                message[key]=value

            writer.writerow( message )
           

def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    _list=[]
    with open(filename,'w') as f:
        for result in results:
            text=result.serialize()
            text["neo"]=result.neo.serialize()

            if text["neo"]["name"] =="" or text["neo"]["name"] == None:
                text["neo"]["name"]=""
            else:
                text["neo"]["name"]=str(text["neo"]["name"])

            if text["neo"]["diameter_km"] =="nan" or text["neo"]["diameter_km"] == None:
                text["neo"]["diameter_km"]="NaN"
            else:
                text["neo"]["diameter_km"]=float(text["neo"]["diameter_km"])

        
            text["distance_au"]=float(text["distance_au"])
            text["velocity_km_s"]=float(text["velocity_km_s"])           
            _list.append(text)
        json.dump(_list, f,indent=2)
            
            
            
