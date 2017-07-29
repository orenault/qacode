import logging, os
from selenium import webdriver as WebDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver import DesiredCapabilities

from qacode.core.bots.modules.NavBase import NavBase
from qacode.core.exceptions.CoreException import CoreException
from qacode.core.loggers.LoggerManager import LoggerManager

class BotBase(object):
    '''
    Class Base for handle selenium functionality
    Properties
      curr_caps : Capabilities class
      curr_driver : WebDriver class
      curr_driver_path : WebDriver browser executable path
      navigation : Bot methods to brigde selenium functions
      bot_config : Bot configuration object
      logger_manager : logger manager class loaded from BotConfig object
      log : log class to write messages
    '''
    curr_caps = None 
    curr_driver = None 
    curr_driver_path = None 
    navigation = None
    bot_config = None
    logger_manager = None 
    log = None 

    def __init__(self, bot_config):
        """
        Create new Bot browser based on options object what can be:
        (help for each option can be found on settings.example.ini)
        + bot_mode 
        + bot_browser
        + bot_url_hub
        + bot_url_node
        + bot_profile_path
        + bot_drivers_path
        + bot_log_name
        + bot_log_output_file
        """
        if bot_config is None:
            raise CoreException('[FAILED]', 'BotBase configuration can\'t be none: bad bot_config provided')
        else:
            try:
                self.bot_config = bot_config
                self.logger_manager = bot_config.logger_manager
                self.log = self.logger_manager.get_log()
            except Exception as err:
                raise CoreException('BotBase, Error: at create LoggerManager', err)
            self.navigation = NavBase(self) # TODO: testcases

            if self.bot_config.bot_mode == 'local':
                self.mode_local()
            elif self.bot_config.bot_mode == 'remote':
                self.mode_remote()
            else:
                raise Exception('[FAILED]', 'Unkown word for bot mode config value: {}'.format(self.bot_config.bot_mode))

    def mode_local(self):
        """
        Open new brower on local mode
        """
        self.log.info('Starting browser with mode : LOCAL')
        self.curr_driver_path = "{}/{}".format(self.bot_config.bot_drivers_path)

        if self.bot_config.bot_browser == 'firefox':
            if os.name == 'nt':
                self.curr_driver_path.format("geckodriver.exe")
            else:
                self.curr_driver_path.format("geckodriver")
            self.curr_caps = DesiredCapabilities.FIREFOX.copy()
            self.curr_driver = WebDriver.Firefox(
                capabilities=self.curr_caps,
                executable_path= self.curr_driver_path)

        elif self.options.botBrowser == 'chrome':
            if os.name == 'nt':
                self.curr_driver_path.format("chromedriver.exe")
            else:
                self.curr_driver_path.format("chromedriver")
            self.currCaps = DesiredCapabilities.CHROME.copy()
            self.currDriver = WebDriver.Chrome(
                executable_path=self.curr_driver_path,
                desired_capabilities=self.curr_caps)

        elif self.options.botBrowser == 'iexplorer':
            self.currCaps = DesiredCapabilities.INTERNETEXPLORER.copy()
            self.currDriver = WebDriver.Ie(
                executable_path=self.curr_driver_path.format("IEDriverServer_32.exe"),
                desired_capabilities=self.curr_caps)

        elif self.options.botBrowser == 'edge':
            self.currCaps = DesiredCapabilities.EDGE.copy()
            self.currDriver = WebDriver.Edge(
                executable_path=self.curr_driver_path.format("EdgeDriver_64.exe"),
                desired_capabilities=self.curr_caps)

        elif self.options.botBrowser == 'phantomjs':
             if os.name == 'nt':
                self.curr_driver_path.format("phantomjs.exe")
            else:
                self.curr_driver_path.format("phantomjs")
            self.currCaps = DesiredCapabilities.PHANTOMJS.copy()
            self.curr_driver = WebDriver.PhantomJS(
                executable_path=self.curr_driver_path,
                desired_capabilities=self.curr_caps)
        else:
            raise Exception()
        self.log.info('Started browser with mode : LOCAL OK')

    def mode_remote(self):
        """
        Open new brower on remote mode
        """
        self.log.info('Starting browser with mode : REMOTE')
        if self.bot_config.bot_browser  == 'firefox':
            self.curr_caps = DesiredCapabilities.FIREFOX.copy()

        elif self.bot_config.bot_browser == 'chrome':
            self.curr_caps= DesiredCapabilities.CHROME.copy()

        elif self.bot_config.bot_browser  == 'iexplorer':
            self.curr_caps = DesiredCapabilities.INTERNETEXPLORER.copy()

        elif self.bot_config.bot_browser == 'phantomjs':
            self.curr_caps = DesiredCapabilities.PHANTOMJS.copy()

        elif self.bot_config.bot_browser == 'edge':
            self.curr_caps = DesiredCapabilities.EDGE.copy()
        else:
            raise Exception("Bad browser selected")

        self.curr_driver = RemoteWebDriver(
            command_executor=self.options.bot_url_hub,
            desired_capabilities=self.curr_caps)
        self.log.info('Started browser with mode : REMOTE OK')

    def close(self):
        self.log.info('Closing browser')
        self.curr_driver.close()
        self.curr_driver.quit()
        self.log.info('Closed browser OK')
