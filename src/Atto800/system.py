class System:
    def __init__(self, device):
        self.device = device
        self.interface_name = "com.attocube.cryostat.interface.system"

    def emptyExternalDatabaseToMaximumBytes(self):
        # type: () -> ()
        """
        Empty database! This solved issues when the UI is hanging! Don't use it otherwise
        """
        
        response = self.device.request(self.interface_name + ".emptyExternalDatabaseToMaximumBytes")
        self.device.handleError(response)
        return                 

    def errorNumberToString(self, errorNumber):
        # type: (int) -> ()
        """
        “Translate” the error code into an error text    Currently we only support the system language

        Parameters:
            errorNumber: error code to translate        
        """
        
        response = self.device.request(self.interface_name + ".errorNumberToString", [errorNumber, ])
        self.device.handleError(response)
        return                 

    def generateCryostatTestdata(self, onOff):
        # type: (bool) -> ()
        """
        Internal use only

        Parameters:
            onOff:         
        """
        
        response = self.device.request(self.interface_name + ".generateCryostatTestdata", [onOff, ])
        self.device.handleError(response)
        return                 

    def getAutoprobeInformationJSONd(self):
        # type: () -> (str)
        """
        Get the hardware autoprobe information

        Returns:
            errorNumber: No error = 0version: firmware version number
        
        """
        
        response = self.device.request(self.interface_name + ".getAutoprobeInformationJSONd")
        self.device.handleError(response)
        return response[1]                

    def getAvailableConfigurationSettings(self):
        # type: () -> (str)
        """
        Gets all available configuration settings

        Returns:
            errorNumber: No error = 0Configuration_settings: CSV of configuration settings
        
        """
        
        response = self.device.request(self.interface_name + ".getAvailableConfigurationSettings")
        self.device.handleError(response)
        return response[1]                

    def getConfigOverrideFile(self):
        # type: () -> (str)
        """
        Get the EEPROM JSON file containing the config overrides.    To know what entries exist have a look at getAvailableConfigurationSettings() and getConfigurationSettingInformation()

        Returns:
            errorNumber: No error = 0overrideFile: String containing the override file
        
        """
        
        response = self.device.request(self.interface_name + ".getConfigOverrideFile")
        self.device.handleError(response)
        return response[1]                

    def getConfigurationConfiguration(self, settingName):
        # type: (str) -> (float)
        """
        Gets the configuration configuration

        Parameters:
            settingName:         

        Returns:
            errorNumber: No error = 0Configuration_setting: 
        
        """
        
        response = self.device.request(self.interface_name + ".getConfigurationConfiguration", [settingName, ])
        self.device.handleError(response)
        return response[1]                

    def getConfigurationSetting(self, settingName):
        # type: (str) -> (float)
        """
        Gets the configuration setting

        Parameters:
            settingName:         

        Returns:
            errorNumber: No error = 0Configuration_setting: 
        
        """
        
        response = self.device.request(self.interface_name + ".getConfigurationSetting", [settingName, ])
        self.device.handleError(response)
        return response[1]                

    def getConfigurationSettingInformation(self, settingName):
        # type: (str) -> (str)
        """
        Gets the configuration setting info string

        Parameters:
            settingName:         

        Returns:
            errorNumber: No error = 0Configuration_settings_information: 
        
        """
        
        response = self.device.request(self.interface_name + ".getConfigurationSettingInformation", [settingName, ])
        self.device.handleError(response)
        return response[1]                

    def getCurrentStatusJSONd(self):
        # type: () -> (str)
        """
        Get the current cryostat status

        Returns:
            errorNumber: No error = 0version: firmware version number
        
        """
        
        response = self.device.request(self.interface_name + ".getCurrentStatusJSONd")
        self.device.handleError(response)
        return response[1]                

    def getDatabaseAsyncQueryResult(self, handle):
        # type: (int) -> (str)
        """
        Get the query result    New!!!

        Parameters:
            handle:         

        Returns:
            errorNumber: No error = 0result: 
        
        """
        
        response = self.device.request(self.interface_name + ".getDatabaseAsyncQueryResult", [handle, ])
        self.device.handleError(response)
        return response[1]                

    def getDatabaseColumnsInterval(self):
        # type: () -> (str)
        """
        Get the cryostat long term status of a time interval    The query has to be prepared with prepareDatabaseColumnsInterval() before. Query until the result is empty    Currently only one query is allowed. If several clients do this simultaneously the results will be garbled. The last client "wins"        We like to query this as quickly as possible. So don't wait after the call here.    Deprecated!!!!

        Returns:
            errorNumber: No error = 0result_rows: 
        
        """
        
        response = self.device.request(self.interface_name + ".getDatabaseColumnsInterval")
        self.device.handleError(response)
        return response[1]                

    def getDatabaseColumnsMinMaxIntervalRows(self, minRow, maxRow, columnNames):
        # type: (int, int, str) -> (str)
        """
        Get the cryostat database columns        New!!!!

        Parameters:
            minRow: maxRow: columnNames: Empty string means all available columns        

        Returns:
            errorNumber: No error = 0result_rows: 
        
        """
        
        response = self.device.request(self.interface_name + ".getDatabaseColumnsMinMaxIntervalRows", [minRow, maxRow, columnNames, ])
        self.device.handleError(response)
        return response[1]                

    def getDatabaseMaximumLogSeconds(self):
        # type: () -> (float)
        """
        Get the cryostat long term status of a time interval

        Returns:
            errorNumber: No error = 0maximumSecondsInLog: 
        
        """
        
        response = self.device.request(self.interface_name + ".getDatabaseMaximumLogSeconds")
        self.device.handleError(response)
        return response[1]                

    def getDatabaseMinMaxResult(self, handle):
        # type: (int) -> (int, int)
        """
        Get the min and max rows.        New!!!

        Parameters:
            handle:         

        Returns:
            errorNumber: No error = 0min_row: may_row: 
        
        """
        
        response = self.device.request(self.interface_name + ".getDatabaseMinMaxResult", [handle, ])
        self.device.handleError(response)
        return response[1], response[2]                

    def getDatabaseMinimumLogSeconds(self):
        # type: () -> (float)
        """
        Get the cryostat long term status of a time interval

        Returns:
            errorNumber: No error = 0minimumSecondsInLog: 
        
        """
        
        response = self.device.request(self.interface_name + ".getDatabaseMinimumLogSeconds")
        self.device.handleError(response)
        return response[1]                

    def getDeviceType(self):
        # type: () -> (str)
        """
        Gets the device type.

        Returns:
            errorNumber: No error = 0type: type of the device
        
        """
        
        response = self.device.request(self.interface_name + ".getDeviceType")
        self.device.handleError(response)
        return response[1]                

    def getFeatures(self):
        # type: () -> (str, str, str, str, str)
        """
        Get the features of the cryostat.

        Returns:
            errorNumber: No error = 0Feature_names: Feature_descriptrions: Feature_short_descriptrions: Feature_display_names: Feature_picture: 
        
        """
        
        response = self.device.request(self.interface_name + ".getFeatures")
        self.device.handleError(response)
        return response[1], response[2], response[3], response[4], response[5]                

    def getFeaturesActivated(self):
        # type: () -> (str)
        """
        Get the active features of the cryostat.

        Returns:
            localErrorNumber: No error = 0Feature_names: 
        
        """
        
        response = self.device.request(self.interface_name + ".getFeaturesActivated")
        self.device.handleError(response)
        return response[1]                

    def getFeaturesJSON(self):
        # type: () -> (str)
        """
        Get the features of the cryostat as a JSON string.

        Returns:
            localErrorNumber: No error = 0JSON: 
        
        """
        
        response = self.device.request(self.interface_name + ".getFeaturesJSON")
        self.device.handleError(response)
        return response[1]                

    def getFirmwareVersion(self):
        # type: () -> (str)
        """
        Gets the version number of the controller firmware.

        Returns:
            errorNumber: No error = 0version: firmware version number
        
        """
        
        response = self.device.request(self.interface_name + ".getFirmwareVersion")
        self.device.handleError(response)
        return response[1]                

    def getIntervalLongTermEntriesJSONd(self, secondsOld, secondsNew):
        # type: (float, float) -> (str)
        """
        Get the cryostat long term status of a time interval

        Parameters:
            secondsOld: secondsNew:         

        Returns:
            errorNumber: No error = 0version: firmware version number
        
        """
        
        response = self.device.request(self.interface_name + ".getIntervalLongTermEntriesJSONd", [secondsOld, secondsNew, ])
        self.device.handleError(response)
        return response[1]                

    def getIntervalShortTermEntriesJSONd(self, secondsOld, secondsNew):
        # type: (float, float) -> (str)
        """
        Get the cryostat status of a time interval

        Parameters:
            secondsOld: secondsNew:         

        Returns:
            errorNumber: No error = 0Short_term_log_entries: 
        
        """
        
        response = self.device.request(self.interface_name + ".getIntervalShortTermEntriesJSONd", [secondsOld, secondsNew, ])
        self.device.handleError(response)
        return response[1]                

    def getLastError(self):
        # type: () -> (int, str, str, str, int)
        """
        Gets all available information on the last error

        Returns:
            i1: i2: s1: s2: s3: i3: 
        
        """
        
        response = self.device.request(self.interface_name + ".getLastError")
        self.device.handleError(response)
        return response[1], response[2], response[3], response[4], response[5]                

    def getLastErrorAge(self):
        # type: () -> (int)
        """
        Gets the age of the last error that happened

        Returns:
            errorNumber: No error = 0age: time in seconds since the last error happened
        
        """
        
        response = self.device.request(self.interface_name + ".getLastErrorAge")
        self.device.handleError(response)
        return response[1]                

    def getLastErrorCommand(self):
        # type: () -> (str)
        """
        Gets the command of the last error that happened

        Returns:
            errorNumber: No error = 0command: command running when the last error happened
        
        """
        
        response = self.device.request(self.interface_name + ".getLastErrorCommand")
        self.device.handleError(response)
        return response[1]                

    def getLastErrorComponent(self):
        # type: () -> (str)
        """
        Gets the component of the last error that happened

        Returns:
            errorNumber: No error = 0component: cryostat component of the error
        
        """
        
        response = self.device.request(self.interface_name + ".getLastErrorComponent")
        self.device.handleError(response)
        return response[1]                

    def getLastErrorNumber(self):
        # type: () -> (int)
        """
        Gets the error number of the last error that happened

        Returns:
            localErrorNumber: No error = 0errorNumber: No error = 0
        
        """
        
        response = self.device.request(self.interface_name + ".getLastErrorNumber")
        self.device.handleError(response)
        return response[1]                

    def getLastErrorRecommendation(self):
        # type: () -> (str)
        """
        Gets the recommendation of the last error that happened

        Returns:
            errorNumber: No error = 0recommendation: error recommendation
        
        """
        
        response = self.device.request(self.interface_name + ".getLastErrorRecommendation")
        self.device.handleError(response)
        return response[1]                

    def getLastErrorsJSONd(self):
        # type: () -> (str)
        """
        Gets the last cryostat errors as a JSON string.

        Returns:
            localErrorNumber: No error = 0JSON: 
        
        """
        
        response = self.device.request(self.interface_name + ".getLastErrorsJSONd")
        self.device.handleError(response)
        return response[1]                

    def getLastErrorsPickled(self, pythonVersion):
        # type: (int) -> (str)
        """
        Gets the last cryostat errors from the snapshot.        Use getLastErrorsAsJSON() and unJSON the data if this call doesn't work for you (the cryostat data can't be unpickled)

        Parameters:
            pythonVersion:         

        Returns:
            localErrorNumber: No error = 0Pickled_data: containing
[
    Error number           -> int
    Recommendation         -> str
    Component              -> str

    Command                -> str
    Age                    -> int
]
        
        """
        
        response = self.device.request(self.interface_name + ".getLastErrorsPickled", [pythonVersion, ])
        self.device.handleError(response)
        return response[1]                

    def getLastLongTermEntriesJSONd(self, seconds):
        # type: (float) -> (str)
        """
        Get the cryostat long term status of the last seconds

        Parameters:
            seconds:         

        Returns:
            errorNumber: No error = 0version: firmware version number
        
        """
        
        response = self.device.request(self.interface_name + ".getLastLongTermEntriesJSONd", [seconds, ])
        self.device.handleError(response)
        return response[1]                

    def getLastShortTermEntriesJSONd(self, seconds):
        # type: (float) -> (str)
        """
        Get the cryostat status of the last seconds

        Parameters:
            seconds:         

        Returns:
            errorNumber: No error = 0version: firmware version number
        
        """
        
        response = self.device.request(self.interface_name + ".getLastShortTermEntriesJSONd", [seconds, ])
        self.device.handleError(response)
        return response[1]                

    def getLogLines(self, maxBytes):
        # type: (int) -> (str)
        """
        Get the last lines of the system logfile.

        Parameters:
            maxBytes: maximum bytes to read        

        Returns:
            errorNumber: No error = 0logLines: String containing the logfile lines
:param maxBytes:
        
        """
        
        response = self.device.request(self.interface_name + ".getLogLines", [maxBytes, ])
        self.device.handleError(response)
        return response[1]                

    def getSecondsFromStartCryostatInstallation(self):
        # type: () -> (float)
        """
        Gets the seconds from start of cryostat installation

        Returns:
            errorNumber: No error = 0seconds: Seconds from start of cryostat installation
        
        """
        
        response = self.device.request(self.interface_name + ".getSecondsFromStartCryostatInstallation")
        self.device.handleError(response)
        return response[1]                

    def getSerialNumber(self):
        # type: () -> (str)
        """
        TGets the serial number.

        Returns:
            errorNumber: No error = 0SN: Serial number
        
        """
        
        response = self.device.request(self.interface_name + ".getSerialNumber")
        self.device.handleError(response)
        return response[1]                

    def getUserConfigOverrideFile(self):
        # type: () -> (str)
        """
        Get he user JSON file containing the config overrides.    To know what entries exist have a look at getAvailableConfigurationSettings() and getConfigurationSettingInformation()

        Returns:
            errorNumber: No error = 0overrideFile: String containing the override file
        
        """
        
        response = self.device.request(self.interface_name + ".getUserConfigOverrideFile")
        self.device.handleError(response)
        return response[1]                

    def isCryostatSane(self):
        # type: () -> (str, int)
        """
        Internal use only

        Returns:
            Sane_or_not: Not_sane_component: errorNumber: No error = 0
        
        """
        
        response = self.device.request(self.interface_name + ".isCryostatSane")
        self.device.handleError(response)
        return response[1], response[2]                

    def lowerError(self):
        # type: () -> ()
        """
        Resets the last error
        """
        
        response = self.device.request(self.interface_name + ".lowerError")
        self.device.handleError(response)
        return                 

    def prepareDatabaseColumnsInterval(self, minTime, maxTime, columnNames):
        # type: (float, float, str) -> ()
        """
        Prepare the cryostat long term status of a time interval query    Get the data with getDatabaseColumnsInterval()    minTime and maxTime can be taken from getDatabaseMinimumLogSeconds()  and getDatabaseMaximumLogSeconds()    Currently only one query is allowed. If several clients do this simultaneously the results will be garbled. The last client "wins"        Deprecated!!!!

        Parameters:
            minTime: maxTime: columnNames: CSV separated, empty means all available columns        
        """
        
        response = self.device.request(self.interface_name + ".prepareDatabaseColumnsInterval", [minTime, maxTime, columnNames, ])
        self.device.handleError(response)
        return                 

    def prepareDatabaseColumnsIntervalAsync(self, minRow, maxRow, columnNames, handle):
        # type: (int, int, str, int) -> ()
        """
        Prepare the cryostat long term status of a time interval query        New!!!

        Parameters:
            minRow: maxRow: columnNames: Empty string means all available columnshandle:         
        """
        
        response = self.device.request(self.interface_name + ".prepareDatabaseColumnsIntervalAsync", [minRow, maxRow, columnNames, handle, ])
        self.device.handleError(response)
        return                 

    def prepareDatabaseMinMaxInterval(self, minTime, maxTime):
        # type: (float, float) -> (int)
        """
        Prepare the cryostat long term status of a time interval query    Get the row numbers with getDatabaseMinMaxResult()    Get the data with getDatabaseColumnsMinMaxIntervalRows()    minTime and maxTime can be taken from getDatabaseMinimumLogSeconds()  and getDatabaseMaximumLogSeconds()        New!!!

        Parameters:
            minTime: maxTime:         

        Returns:
            errorNumber: No error = 0handle: 
        
        """
        
        response = self.device.request(self.interface_name + ".prepareDatabaseMinMaxInterval", [minTime, maxTime, ])
        self.device.handleError(response)
        return response[1]                

    def resetUserConfigOverrideFile(self):
        # type: () -> ()
        """
        Copy the EEPROM config factory defaults to the user config
        """
        
        response = self.device.request(self.interface_name + ".resetUserConfigOverrideFile")
        self.device.handleError(response)
        return                 

    def setConfigOverrideFile(self, secret, fileContent):
        # type: (str, str) -> ()
        """
        Set the EEPROM JSON file containing the config overrides.    To know what entries exist have a look at getAvailableConfigurationSettings() and getConfigurationSettingInformation()    Please set the user file too with setUserConfigOverrideFile()

        Parameters:
            secret: Only allow writing the config file when we know the secret stringfileContent: Contents of the config override file        
        """
        
        response = self.device.request(self.interface_name + ".setConfigOverrideFile", [secret, fileContent, ])
        self.device.handleError(response)
        return                 

    def setConfigurationSetting(self, settingName, settingValue):
        # type: (str, float) -> ()
        """
        Sets the configuration setting

        Parameters:
            settingName: settingValue:         
        """
        
        response = self.device.request(self.interface_name + ".setConfigurationSetting", [settingName, settingValue, ])
        self.device.handleError(response)
        return                 

    def setUserConfigOverrideFile(self, fileContent):
        # type: (str) -> (str)
        """
        Set the user JSON file containing the config overrides.    To know what entries exist have a look at getAvailableConfigurationSettings() and getConfigurationSettingInformation()

        Parameters:
            fileContent: Contents of the config override file        

        Returns:
            errorNumber: No error = 0hintstrting: Free text string to give the caller some hints if things don't work
        
        """
        
        response = self.device.request(self.interface_name + ".setUserConfigOverrideFile", [fileContent, ])
        self.device.handleError(response)
        return response[1]                

