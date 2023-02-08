import pandas as pd
import numpy as np
import re

def standard_headers(df):
    cols = [col.lower().replace(' ', '_') for col in df.columns]
    df.columns = cols
    df = df.rename(columns={'flight_#': 'flight_no'})
    return df

#Header fixer: Sets the brand at the beggining of the string

def antonov_header(x):
    index = x.find('Antonov')
    if index != -1:
        return x[index:]
    else:
        return x

def douglas_header(x):
    index = x.find('Douglas')
    if index != -1:
        return x[index:]
    else:
        return x

def tupolev_header(x):
    index = x.find('Tupolev')
    if index != -1:
        return x[index:]
    else:
        return x

def lockheed_header(x):
    index = x.find('Lockheed')
    if index != -1:
        return x[index:]
    else:
        return x

def boeing_header(x):
    index = x.find('Boeing')
    if index != -1:
        return x[index:]
    else:
        return x

def cessna_header(x):
    index = x.find('Cessna')
    if index != -1:
        return x[index:]
    else:
        return x


#Applier 1: Applies all header reset to the df

def header_applier(df):
    headers_restart = [antonov_header, douglas_header, tupolev_header, lockheed_header, boeing_header, cessna_header]
    for i in headers_restart:
        df['type'] = df['type'].apply(i)
    return df

#Applier 1 end </>




#Cardinality reducer function: Uses regex to group model variants into the main model.

def cardinality_reducer(col):
    if 'Antonov' in col:
        if '140' in col:
            return re.sub('Antonov A?N?n?-?140\w?\w?[^|]*$', 'Antonov AN-140', col)
        elif '124' in col:
            return re.sub('Antonov A?N?n?-?124\w?\w?[^|]*$', 'Antonov AN-124', col)
        elif '74' in col:
            return re.sub('Antonov A?N?n?-?74\w?\w?[^|]*$', 'Antonov AN-74', col)
        elif '72' in col:
            return re.sub('Antonov A?N?n?-?72\w?\w?[^|]*$', 'Antonov AN-72', col)
        elif '32' in col:
            return re.sub('Antonov A?N?n?-?32\w?\w?[^|]*$', 'Antonov AN-32', col)
        elif '28' in col:
            return re.sub('Antonov A?N?n?-?28\w?\w?[^|]*$', 'Antonov AN-28', col)
        elif '26' in col:
            return re.sub('Antonov A?N?n?-?26\w?\w?[^|]*$', 'Antonov AN-26', col)
        elif '24' in col:
            return re.sub('Antonov A?N?n?-?24\w?\w?[^|]*$', 'Antonov AN-24', col)
        elif '12' in col:
            return re.sub('Antonov A?N?n?-?12\w?\w?[^|]*$', 'Antonov AN-12', col)
        elif '10' in col:
            return re.sub('Antonov A?N?n?-?10\w?\w?', 'Antonov AN-10', col)
        elif '8' in col:
            return re.sub('Antonov A?N?n?-?8\w?\w?', 'Antonov AN-8', col)
        elif '2' in col:
            return re.sub('Antonov A?N?n?-?2\w?\w?[^|]*$', 'Antonov AN-2', col)
    
    elif 'Douglas' in col:
        if '124' in col:
            return re.sub('Douglas C?-?124\w?\w?[^|]*$', 'Douglas C-124', col)
        elif '82' in col:
            return re.sub('Douglas M?D?-?82\w?\w?[^|]*$', 'Douglas MD-82', col)
        elif '74' in col:
            return re.sub('Douglas C?-?74\w?\w?[^|]*$', 'Douglas C-74', col)
        elif '54' in col:
            return re.sub('Douglas C?-?54\w?\w?[^|]*$', 'Douglas C-54', col)
        elif '53' in col:
            return re.sub('Douglas C?-?53\w?\w?[^|]*$', 'Douglas C-53', col)
        elif '47' in col:
            return re.sub('Douglas C?-?47\w?\w?[^|]*$', 'Douglas C-47', col)
        elif 'MD-11' or 'MD11' in col:
            return re.sub('Douglas D?C?-?10\w?\w?[^|]*$', 'Douglas C-10', col)
        elif '10' in col:
            return re.sub('Douglas D?C?-?10\w?\w?[^|]*$', 'Douglas C-10', col)
        elif '9' in col:
            return re.sub('Douglas D?C?-?9\w?\w?[^|]*$', 'Douglas DC-9', col)
        elif '8' in col:
            return re.sub('Douglas D?C?-?8\w?\w?[^|]*$', 'Douglas DC-8', col)
        elif '7' in col:
            return re.sub('Douglas D?C?-?7\w?\w?[^|]*$', 'Douglas DC-7', col)
        elif '6' in col:
            return re.sub('Douglas D?C?-?6\w?\w?[^|]*$', 'Douglas DC-6', col)
        elif 'MD-4' or 'MD4' in col:
            return re.sub('Douglas M?D?-?4\w?\w?[^|]*$', 'Douglas MD-4', col)
        elif '4' in col:
            return re.sub('Douglas D?C?-?4\w?\w?[^|]*$', 'Douglas DC-4', col)
        elif '3' in col:
            return re.sub('Douglas D?C?-?3\w?\w?[^|]*$', 'Douglas DC-3', col)
        elif '2' in col:
            return re.sub('Douglas D?C?-?2\w?\w?[^|]*$', 'Douglas DC-2', col)
    
    elif 'Tupolev' in col:
        if '154' in col:
            return re.sub('Tupolev T?U?u? ?-?154\w?\w?[^|]*$', 'Tupolev TU-154', col)
        elif '144' in col:
            return re.sub('Tupolev T?U?u?-?144\w?\w?[^|]*$', 'Tupolev TU-144', col)
        elif '134' in col:
            return re.sub('Tupolev T?U?u?-?134\w?\w?[^|]*$', 'Tupolev TU-134', col)
        elif '104' in col:
            return re.sub('Tupolev T?U?u?-?104\w?\w?[^|]*$', 'Tupolev TU-104', col)
    
    elif 'Lockheed' in col:
        if '1049' in col:
            return re.sub('Lockheed L? ?-?1049\w?\w?[^|]*$', 'Lockheed L-1049', col)
        elif '1011' in col:
            return re.sub('Lockheed L? ?-?1011\w?\w?[^|]*$', 'Lockheed L-1011', col)
        elif '749' in col:
            return re.sub('Lockheed L? ?749\w?\w?[^|]*$', 'Lockheed 749', col)
        elif '188' in col:
            return re.sub('Lockheed L? ?-?188\w?\w?[^|]*$', 'Lockheed L-188', col)
        elif '141' in col:
            return re.sub('Lockheed C? ?-?141\w?\w?[^|]*$', 'Lockheed C-141', col)
        elif '130' in col:
            return re.sub('Lockheed E?C? ?-?130\w?\w?[^|]*$', 'Lockheed C-130', col)
        elif 'Hercules' in col:
            return re.sub('Lockheed M?C? ?-?130\w?\w?[^|]*$', 'Lockheed C-130', col)
        elif '100' in col:
            return re.sub('Lockheed L? ?-?100\w?\w?[^|]*$', 'Lockheed L-100', col)
        elif '049' in col:
            return re.sub('Lockheed L? ?-?049\w?\w?[^|]*$', 'Lockheed L-049', col)
        elif '18' in col:
            return re.sub('Lockheed L? ?-?18\w?\w?[^|]*$', 'Lockheed L-18', col)
        
    elif 'Boeing' in col:
        if '777' in col:
            return re.sub('Boeing B? ?-?777\w?\w?[^|]*$', 'Boeing 777', col)
        elif '767' in col:
            return re.sub('Boeing B? ?-?767\w?\w?[^|]*$', 'Boeing 767', col)
        elif '757' in col:
            return re.sub('Boeing B? ?-?757\w?\w?[^|]*$', 'Boeing 757', col)
        elif '747' in col:
            return re.sub('Boeing B? ?747\w?\w?[^|]*$', 'Boeing 747', col)
        elif '737' in col:
            return re.sub('Boeing B? ?-?737\w?\w?[^|]*$', 'Boeing 737', col)
        elif '727' in col:
            return re.sub('Boeing B? ?-?727\w?\w?[^|]*$', 'Boeing 727', col)
        elif '720' in col:
            return re.sub('Boeing B? ?-?720\w?\w?[^|]*$', 'Boeing 720', col)
        elif '707' in col:
            return re.sub('Boeing B? ?-?707\w?\w?[^|]*$', 'Boeing 707', col)
        elif '377' in col:
            return re.sub('Boeing B? ? ?-?377\w?\w?[^|]*$', 'Boeing 377', col)
        elif '307' in col:
            return re.sub('Boeing B? ? ?-?307\w?\w?[^|]*$', 'Boeing 307', col)
        elif '247' in col:
            return re.sub('Boeing B? ? ?-?247\w?\w?[^|]*$', 'Boeing 247', col)
        elif '135' in col:
            return re.sub('Boeing RC? ? ?-?135\w?\w?[^|]*$', 'Boeing RC-135', col)
        elif '135' in col:
            return re.sub('Boeing KC? ? ?-?135\w?\w?[^|]*$', 'Boeing KC-135', col)
        elif '135' in col:
            return re.sub('Boeing EC? ? ?-?135\w?\w?[^|]*$', 'Boeing EC-135', col)
        elif '95' in col:
            return re.sub('Boeing B? ?-?95\w?\w?[^|]*$', 'Boeing 95', col)
        elif '40' in col:
            return re.sub('Boeing B? ?-?40\w?\w?[^|]*$', 'Boeing 40', col)
        elif 'Vertol' in col:
            return re.sub('Boeing Vertol ?C?H? ?-?47\w?\w?[^|]*$', 'Boeing Vertol CH-47', col)
        elif 'Chinook' in col:
            return re.sub('Boeing ?-?Vertol \w?\w?[^|]*$', 'Boeing Vertol Chinook', col)
        elif '29' in col:
            return re.sub('Boeing B? ?-?29\w?\w?[^|]*$', 'Boeing B-29', col)
        elif '049' in col:
            return re.sub('Boeing L? ?-?049\w?\w?[^|]*$', 'Boeing L-049', col)
        elif '18' in col:
            return re.sub('Boeing L? ?-?18\w?\w?[^|]*$', 'Boeing L-18', col)
        elif '17' in col:
            return re.sub('Boeing B? ?-?17\w?\w?[^|]*$', 'Boeing B-17', col)
        
    elif 'Airbus' in col:
        if '300' in col:
            return re.sub('Airbus ?A?.? ?-?300\w?\w?[^|]*$', 'Airbus A300', col)
        elif '310' in col:
            return re.sub('Airbus ?A? ?-?310\w?\w?[^|]*$', 'Airbus A310', col)
        elif '320' in col:
            return re.sub('Airbus ?A?.? ?-?320\w?\w?[^|]*$', 'Airbus A320', col)
        elif '330' in col:
            return re.sub('Airbus ?A?.? ?-?330\w?\w?[^|]*$', 'Airbus A330', col)
        elif '340' in col:
            return re.sub('Airbus ?A?.? ?-?340\w?\w?[^|]*$', 'Airbus A340', col)
        
    elif 'Cessna' in col:
        if '650' in col:
            return re.sub('Cessna ? ?-?650\w?\w?[^|]*$', 'Cessna 650', col)
        elif '560' in col:
            return re.sub('Cessna ? ?-?560\w?\w?[^|]*$', 'Cessna 560', col)
        elif '551' in col:
            return re.sub('Cessna ? ?-?551\w?\w?[^|]*$', 'Cessna 551', col)
        elif '550' in col:
            return re.sub('Cessna ? ?-?550\w?\w?[^|]*$', 'Cessna 550', col)
        elif '525' in col:
            return re.sub('Cessna ? ?-?525\w?\w?[^|]*$', 'Cessna 525', col)
        elif '501' in col:
            return re.sub('Cessna ? ?-?501\w?\w?[^|]*$', 'Cessna 501', col)
        elif '500' in col:
            return re.sub('Cessna ? ?-?500\w?\w?[^|]*$', 'Cessna 500', col)
        elif '441' in col:
            return re.sub('Cessna ? ?-?441\w?\w?[^|]*$', 'Cessna 441', col)
        elif '425' in col:
            return re.sub('Cessna ? ?-?425\w?\w?[^|]*$', 'Cessna 425', col)
        elif '421' in col:
            return re.sub('Cessna ? ?-?421\w?\w?[^|]*$', 'Cessna 421', col)
        elif '411' in col:
            return re.sub('Cessna ? ?-?411\w?\w?[^|]*$', 'Cessna 411', col)
        elif '404' in col:
            return re.sub('Cessna ? ?-?404\w?\w?[^|]*$', 'Cessna 404', col)
        elif '402' in col:
            return re.sub('Cessna ? ?-?402\w?\w?[^|]*$', 'Cessna 402', col)
        elif '401' in col:
            return re.sub('Cessna ? ?-?401\w?\w?[^|]*$', 'Cessna 401', col)
        elif '337' in col:
            return re.sub('Cessna ? ?-?T?337\w?\w?[^|]*$', 'Cessna 337', col)
        elif '320' in col:
            return re.sub('Cessna ? ?-?320\w?\w?[^|]*$', 'Cessna 320', col)
        elif '310' in col:
            return re.sub('Cessna ? ?-?T?310\w?\w?[^|]*$', 'Cessna 310', col)
        elif '210' in col:
            return re.sub('Cessna ? ?-?T?210\w?\w?[^|]*$', 'Cessna 210', col)
        elif '208' in col:
            return re.sub('Cessna ? ?-?208\w?\w?[^|]*$', 'Cessna 208', col)
        elif '207' in col:
            return re.sub('Cessna ? C??-?T?207\w?\w?[^|]*$', 'Cessna 207', col)
        elif '206' in col:
            return re.sub('Cessna ? ?-?T?U?206\w?\w?[^|]*$', 'Cessna 206', col)
        elif '205' in col:
            return re.sub('Cessna ? ?-?205\w?\w?[^|]*$', 'Cessna 205', col)
        elif '182' in col:
            return re.sub('Cessna ? ?-?R?182\w?\w?[^|]*$', 'Cessna 182', col)
        elif '180' in col:
            return re.sub('Cessna ? ?-?180\w?\w?[^|]*$', 'Cessna 180', col)
        elif '177' in col:
            return re.sub('Cessna ? ?-?177\w?\w?[^|]*$', 'Cessna 177', col)
        elif '172' in col:
            return re.sub('Cessna ? ?-?172\w?\w?[^|]*$', 'Cessna 172', col)
        elif '150' in col:
            return re.sub('Cessna ? ?-?150\w?\w?[^|]*$', 'Cessna 150', col)
    
    return col



#Applier 2: Applies the main function to the models column or type.
def cardinality_reducer_1(df):
    df['type'] = df['type'].apply(cardinality_reducer)
    return df


#Cardinality reducers made ad-hoc for the models not picked up by regex function.
def douglas_header2(x):
    index = x.find('Douglas DC-2')
    if index != -1:
        return 'Douglas DC-2'
    else:
        return x

def douglas_header3(x):
    index = x.find('Douglas DC-3')
    if index != -1:
        return 'Douglas DC-3'
    else:
        return x

def douglas_header4(x):
    index = x.find('Douglas DC-4')
    if index != -1:
        return 'Douglas DC-4'
    else:
        return x

def douglas_header6(x):
    index = x.find('Douglas DC-6')
    if index != -1:
        return 'Douglas DC-6'
    else:
        return x

def douglas_header7(x):
    index = x.find('Douglas DC-7')
    if index != -1:
        return 'Douglas DC-7'
    else:
        return x    

def douglas_header8(x):
    index = x.find('Douglas DC-8')
    if index != -1:
        return 'Douglas DC-8'
    else:
        return x

def douglas_header9(x):
    index = x.find('Douglas DC-9')
    if index != -1:
        return 'Douglas DC-9'
    else:
        return x
    
def tupolev_header154(x):
    index = x.find('Tupolev TU 154B-2')
    if index != -1:
        return 'Tupolev TU 154'
    else:
        return x

def lockheed_hercules(x):
    index = x.find('Hercules')
    if index != -1:
        return 'Lockheed C-130'
    else:
        return x

def lockheed_14(x):
    index = x.find('Lockheed 14')
    if index != -1:
        return 'Lockheed 14'
    else:
        return x

def lockheed_10(x):
    index = x.find('Lockheed 10')
    if index != -1:
        return 'Lockheed 10'
    else:
        return x


def lockheed_049(x):
    index = x.find('Lockheed L-049')
    if index != -1:
        return 'Lockheed L-049'
    else:
        return x

def lockheed_749(x):
    index = x.find('Lockheed L-749')
    if index != -1:
        return 'Lockheed L-749'
    else:
        return x

def lockheed_p3(x):
    index = x.find('Lockheed P-3')
    if index != -1:
        return 'Lockheed P-3'
    else:
        return x
    
def lockheed_vega(x):
    index = x.find('Lockheed Vega')
    if index != -1:
        return x[index:15]
    else:
        return x

def lockheed_orion(x):
    index = x.find('Lockheed Orion 9')
    if index != -1:
        return 'Lockheed Orion 9'
    else:
        return x

def lockheed_hudson(x):
    index = x.find('Lockheed Hudson')
    if index != -1:
        return 'Lockheed Hudson'
    else:
        return x
    
def lockheed_ec121(x):
    index = x.find('Lockheed EC-121')
    if index != -1:
        return 'Lockheed EC-121'
    else:
        return x
    
def lockheed_c5(x):
    index = x.find('Lockheed C-5')
    if index != -1:
        return 'Lockheed C-5'
    else:
        return x
    
def lockheed_wv2(x):
    index = x.find('Lockheed WV-2')
    if index != -1:
        return 'Lockheed WV-2'
    else:
        return x

def boeing_777(x):
    index = x.find('Boeing B-777')
    if index != -1:
        return 'Boeing 777'
    else:
        return x    

def boeing_767(x):
    index = x.find('Boeing B-767')
    if index != -1:
        return 'Boeing 767'
    else:
        return x      

def boeing_757(x):
    index = x.find('Boeing B-757')
    if index != -1:
        return 'Boeing 757'
    else:
        return x       

def boeing_747(x):
    index = x.find('Boeing B-747')
    if index != -1:
        return 'Boeing 747'
    else:
        return x
    
def boeing_737(x):
    index = x.find('Boeing B-737')
    if index != -1:
        return 'Boeing 737'
    else:
        return x

def boeing_727(x):
    index = x.find('Boeing B-727')
    if index != -1:
        return 'Boeing 727'
    else:
        return x

def boeing_377(x):
    index = x.find('Boeing - 377')
    if index != -1:
        return 'Boeing 377'
    else:
        return x

def boeing_kc135(x):
    index = x.find('Boeing KC-135')
    if index != -1:
        return 'Boeing KC-135'
    else:
        return x

def boeing_ec135(x):
    index = x.find('Boeing - EC-135')
    if index != -1:
        return 'Boeing EC-135'
    else:
        return x

def boeing_ec135_2(x):
    index = x.find('Boeing EC-135N')
    if index != -1:
        return 'Boeing EC-135'
    else:
        return x

def boeing_ec97(x):
    index = x.find('Boeing C-97')
    if index != -1:
        return 'Boeing C-97'
    else:
        return x

def boeing_vertol(x):
    index = x.find('Boeing CH47')
    if index != -1:
        return 'Boeing Vertol CH-47'
    else:
        return x

def boeing_chinook(x):
    index = x.find('Vertol Chinook')
    if index != -1:
        return 'Boeing Vertol Chinook'
    else:
        return x

def boeing_c135(x):
    index = x.find('Boeing C-135')
    if index != -1:
        return 'Boeing C-135'
    else:
        return x
    
def cessna_header(x):
    index = x.find('Cessna Citation 500')
    if index != -1:
        return 'Cessna 500'
    else:
        return x

def cessna_t210(x):
    index = x.find('Cessna T210')
    if index != -1:
        return 'Cessna T210'
    else:
        return x

#Cardinality ad-hoc functions applier

def cardinality_reducer_2(df):
    models_heads = [douglas_header2, douglas_header3, douglas_header4, douglas_header6, douglas_header7, douglas_header8, douglas_header9, tupolev_header154, lockheed_hercules, 
                lockheed_14, lockheed_10, lockheed_049, lockheed_749, lockheed_p3, lockheed_vega, lockheed_orion, lockheed_hudson, lockheed_ec121, lockheed_c5, lockheed_wv2, 
                boeing_777, boeing_767, boeing_757, boeing_747, boeing_737, boeing_727, boeing_377, boeing_kc135, boeing_ec135, boeing_ec135_2, boeing_vertol, boeing_chinook, 
                boeing_ec97, boeing_c135, cessna_t210]
    for i in models_heads:
        df['type'] = df['type'].apply(i)
    return df



#Operators cleaners    

def operator_cleaner_us(x):
    index = x.find('Military - U.S')
    if index != -1:
        return 'Military - U.S'
    else:
        return x

def operator_cleaner_us2(x):
    index = x.find('Military - United States')
    if index != -1:
        return 'Military - U.S'
    else:
        return x

def operator_cleaner_uk(x):
    index = x.find('Military - Royal Air Force')
    if index != -1:
        return 'Military - U.K.'
    else:
        return x

def operator_cleaner_uk2(x):
    index = x.find('Military -Royal Air Force')
    if index != -1:
        return 'Military - U.K.'
    else:
        return x

def operator_cleaner_panam(x):
    index = x.find('Pan American World Airways')
    if index != -1:
        return 'Pan American'
    else:
        return x

def operator_cleaner_panam2(x):
    index = x.find('Pan American Airways')
    if index != -1:
        return 'Pan American'
    else:
        return x

def operator_cleaner_panam3(x):
    index = x.find('Pan American Grace Airways')
    if index != -1:
        return 'Pan American'
    else:
        return x

def operator_cleaner_panam4(x):
    index = x.find('Pan American Grace Airways')
    if index != -1:
        return 'Pan American'
    else:
        return x

def operator_cleaner_panam5(x):
    index = x.find('Pan American Grace Airlines')
    if index != -1:
        return 'Pan American'
    else:
        return x

def operator_cleaner_panam6(x):
    index = x.find('Pan American World Airways / KLM')
    if index != -1:
        return 'Pan American'
    else:
        return x

def operator_cleaner_panam7(x):
    index = x.find('Pan American Airways (Scadta)')
    if index != -1:
        return 'Pan American'
    else:
        return x

def operator_cleaner_lft(x):
    index = x.find('Lufthansa Cityline')
    if index != -1:
        return 'Lufthansa'
    else:
        return x

def operator_cleaner_lft2(x):
    index = x.find('Deutche Lufthansa')
    if index != -1:
        return 'Lufthansa'
    else:
        return x

def operator_cleaner_lft3(x):
    index = x.find('Deutsche Lufthansa')
    if index != -1:
        return 'Lufthansa'
    else:
        return x
def operator_cleaner_ib(x):
    index = x.find('Iberia Airlines / Aviaco')
    if index != -1:
        return 'Iberia'
    else:
        return x

def operator_cleaner_ib2(x):
    index = x.find('Iberia Airlines')
    if index != -1:
        return 'Iberia'
    else:
        return x

def operator_cleaner_ger(x):
    index = x.find('Military - German Navy')
    if index != -1:
        return 'Military - German'
    else:
        return x

def operator_cleaner_ger2(x):
    index = x.find('Military - German Army')
    if index != -1:
        return 'Military - German'
    else:
        return x

def operator_cleaner_ger3(x):
    index = x.find('Military - German Air National Guard')
    if index != -1:
        return 'Military - German'
    else:
        return x
    
def operator_cleaner_ger4(x):
    index = x.find('Military - German Air National Guard')
    if index != -1:
        return 'Military - German'
    else:
        return x

def operator_cleaner_ger5(x):
    index = x.find('Military - Deutsche Luftwaffe')
    if index != -1:
        return 'Military - German'
    else:
        return x
    
def operator_cleaner_ger6(x):
    index = x.find('Military - Luftwaffe')
    if index != -1:
        return 'Military - German'
    else:
        return x

def operator_cleaner_ger7(x):
    index = x.find('Military - Luftwaffe / Military - USAF')
    if index != -1:
        return 'Military - German'
    else:
        return x

def operator_cleaner_sp(x):
    index = x.find('Spanish Air Force')
    if index != -1:
        return 'Military - Spanish Air Force'
    else:
        return x

def operator_cleaner_sp2(x):
    index = x.find('Military - Spanish Air Force.')
    if index != -1:
        return 'Military - Spanish Air Force'
    else:
        return x

#Function that applies the operators groupers
def main_operator_grouper(df):
    operators =[operator_cleaner_us, operator_cleaner_us2, operator_cleaner_uk, operator_cleaner_uk2, operator_cleaner_panam, operator_cleaner_panam2, operator_cleaner_panam3, 
                operator_cleaner_panam4, operator_cleaner_panam5, operator_cleaner_panam6, operator_cleaner_panam7, operator_cleaner_lft, operator_cleaner_lft2, 
                operator_cleaner_lft3, operator_cleaner_ib, operator_cleaner_ib2, operator_cleaner_ger, operator_cleaner_ger2, operator_cleaner_ger3, operator_cleaner_ger4, 
               operator_cleaner_ger5, operator_cleaner_ger6, operator_cleaner_ger7, operator_cleaner_sp, operator_cleaner_sp2]
    for i in operators:
        df['operator'] = df['operator'].apply(i)
    return df


#Main cleaning function grouping all previous ones
def clean_df(df):
    df = header_applier(df)
    df = cardinality_reducer_1(df)
    df = cardinality_reducer_2(df)
    df = main_operator_grouper(df)
    return df