from cmath import nan
import sqlite3
import math

PATH = 'extcaland.db'

class dbWorker:
    isDataLoaded = False
    
    minDate = ''
    maxDate = ''

    parameters = dict() #[id] = [code]              для всех параметров
    features = dict()   #[id] = [code]              для управляющих воздействий
    defects = dict()    #[id] = [code]              для выходных параметров
    ruNames = dict()    #[id] = [ruName]            для всех параметров
    enNames = dict()    #[id] = [enName]            для всех параметров
    
    limits = {}         #limit[id][0(min)/1(max)]   для всех параметров
    
    dates = list()      #
    
    all = dict()        #[id] = [values]            для всех параметров
    x = dict()          #[id] = [values]            для управляющих воздействий
    y = dict()          #[id] = [values]            для выходных параметров

    #RNN
    optimizers = dict()
    activationFunctions = dict()

    def __init__(self):
        self.getMinMaxDates()
        
    def getMinMaxDates(self):
        conn = sqlite3.connect(PATH)
        cursor = conn.cursor()
        cursor.execute( f" SELECT MIN(DateTime)"
                        f" FROM ParameterValues"
                        f" WHERE LENGTH(DateTime) = LENGTH('yyyy-mm-dd hh:mm:ss')" )
        minDate = cursor.fetchall()
        cursor.execute( f" SELECT MAX(DateTime)"
                        f" FROM ParameterValues"
                        f" WHERE LENGTH(DateTime) = LENGTH('yyyy-mm-dd hh:mm:ss')" )
        maxDate = cursor.fetchall()
        self.minDate = str(minDate[0][0])
        self.maxDate = str(maxDate[0][0])        
        cursor.close()
        conn.close()

    def loadParameters(self):
        conn = sqlite3.connect(PATH)
        cursor = conn.cursor()
        cursor.execute( f" SELECT IdParameter, ParameterCode, ParameterNameRu, ParameterNameEng"
                        f" FROM Parameters"
                        f" WHERE IdParameterType == 2"
                        f"  OR IdParameterType == 3" )
        params_row = cursor.fetchall()
        cursor.execute( f" SELECT Limits.IdParameter, LowLimitValue, HighLimitValue"
                        f" FROM Limits"
                        f"  LEFT JOIN Parameters ON Parameters.IdParameter = Limits.IdParameter"
                        f" WHERE IdParameterType == 2"
                        f"  OR IdParameterType == 3" )
        limits_row = cursor.fetchall()
        for row_id in range(len(params_row)):
            self.ruNames[params_row[row_id][0]] = params_row[row_id][2]
            self.enNames[params_row[row_id][0]] = params_row[row_id][3]
            min = float('nan') if limits_row[row_id][1] is None else float(limits_row[row_id][1])
            max = float('nan') if limits_row[row_id][2] is None else float(limits_row[row_id][2])
            self.limits[limits_row[row_id][0]] = (min, max)
            self.parameters[params_row[row_id][0]] = params_row[row_id][1]
            if params_row[row_id][1].split('.')[0] == 'Defects':
                self.defects[params_row[row_id][0]] = params_row[row_id][1]
                self.y[params_row[row_id][0]] = list()
            else:
                self.features[params_row[row_id][0]] = params_row[row_id][1]
                self.x[params_row[row_id][0]] = list()
        cursor.close()
        conn.close()
    
    def loadRNNParameters(self):
        conn = sqlite3.connect(PATH)
        cursor = conn.cursor()
        cursor.execute( f" SELECT *"
                        f" FROM NNCoefficients" )
        params_row = cursor.fetchall()
        for row_id in range(len(params_row)):
            if params_row[row_id][2] == 1:
                self.activationFunctions[params_row[row_id][0]] = params_row[row_id][1]
            else:
                self.optimizers[params_row[row_id][0]] = params_row[row_id][1]
        cursor.close()
        conn.close()

    def loadValues(self):
        conn = sqlite3.connect(PATH)
        cursor = conn.cursor()
        cursor.execute( f" SELECT DateTime, group_concat(ParameterValues.IdParameter || ': ' || Value, ',')"
                        f" FROM ParameterValues"
                        f"  LEFT JOIN Parameters ON Parameters.IdParameter = ParameterValues.IdParameter"
                        f" WHERE DateTime BETWEEN '{self.minDate}' AND '{self.maxDate}'"
                        f"  AND IdParameterType == 2"
                        f" OR DateTime BETWEEN '{self.minDate}' AND '{self.maxDate}'"
                        f"  AND IdParameterType == 3"
                        f" GROUP BY DateTime" )
        while True:
            row = cursor.fetchone()
            if row:
                row_time = row[0]
                row_parameters = row[1].split(',')
                row_values = self.initializeParametersDictionary()
                for parameter in row_parameters:
                    splited_parameter = parameter.split(':')
                    index = int(splited_parameter[0])
                    row_values[index] = round(float(splited_parameter[1]), 4)
                if self.isValidValues(row_values):
                    self.dates.append(row_time)
                    for index in self.parameters:
                        if index in self.defects:
                            self.y[index].append(row_values[index])
                        else:
                            self.x[index].append(row_values[index])
            else:
                break
        cursor.close()
        conn.close()

    def loadData(self, startDate, endDate):
        self.minDate = startDate
        self.maxDate = endDate

        self.loadParameters()
        self.loadRNNParameters()
        self.loadValues()

        self.isDataLoaded = True

    def initializeParametersDictionary(self):
        param = dict()
        for parameter in self.parameters:
            param[parameter] = float('nan')
        return param
    def isValidValues(self, values):
        for value in values:
            if math.isnan(values[value]):
                return False
        return True
    def getNames(self, names, parameters):
        result = list()
        for parameter in parameters:
            result.append(names[parameter])
        return result