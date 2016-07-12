# -*- coding: utf-8 -*-


class NPMException(Exception):
    pass

# Yes, it's deprecated in Python 2.6 because it's going away in Python 3.0
# BaseException class does not provide a way to store error message anymore. 
# You'll have to implement it yourself. 
# You can do this with a subclass that uses a property for storing the message.

class ElementNotFound(NPMException):
    def _get_message(self):
        return self._message
    def _set_message(self, message):
        self._message = message
    message = property(_get_message, _set_message)
    
    
class ElementVisibleTimeout(NPMException):
    def _get_message(self):
        return self._message
    def _set_message(self, message):
        self._message = message
    message = property(_get_message, _set_message)

class InvalidSwitchToTargetException(NPMException):
    def _get_message(self):
        return self._message
    def _set_message(self, message):
        self._message = message
    message = property(_get_message, _set_message)
  
class ElementTextTimeout(NPMException):
    def _get_message(self):
        return self._message

    def _set_message(self, message):
        self._message = message
    message = property(_get_message, _set_message)


class InvalidLocatorString(NPMException):
    def _get_message(self):
        return self._message

    def _set_message(self, message):
        self._message = message
    message = property(_get_message, _set_message)