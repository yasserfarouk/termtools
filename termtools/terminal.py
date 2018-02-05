#!/usr/bin/env python
"""
This module exposes classes to control displaying text and progress bars at any place of the screen.

The two main classes are TerminalController and ProgressBarController
"""
import math
import sys
import time
import typing as t


class TerminalController(object):
    """A class for controlling where to print on a screen and the attributes of text to be printed."""

    def __init__(self):
        """Constructor."""
        self.x = None
        self.y = None
        pass

    def clear(self):
        """
            clears the screen

        :rtype: TerminalController
        """
        return self.home(erase_screen=True)

    def home(self, erase_screen=False):
        """
            gets the cursor to the top of the screen

        :rtype: TerminalController
        """
        if erase_screen:
            for n in range(0, 64, 1): print("\r\n")
            print("\033[2J", end='')
        print("\033[0;0H", end='')
        return self

    def goto(self, x=0, y=0):
        """
            goes to the specified x-y coordingates on the screen

        :param x: x coordinate from the left to right
        :param y: y coordinate from the top to bottom
        :rtype: TerminalController
        """
        x = int(x)
        y = int(y)
        if x >= 255: x = 255
        if y >= 255: y = 255
        if x <= 0: x = 0
        if y <= 0: y = 0
        HORIZ = str(x)
        VERT = str(y)
        # Plot the user_string at the starting at position HORIZ, VERT...
        print("\033[" + VERT + ";" + HORIZ + "f", end='')
        return self

    def printat(self, txt, x=0, y=0):
        """
            goes to the specified x-y coordingates on the screen and prints the text.

        :param x: x coordinate from the left to right
        :param y: y coordinate from the top to bottom
        :rtype: TerminalController
        """
        x = int(x)
        y = int(y)
        if x >= 255: x = 255
        if y >= 255: y = 255
        if x <= 0: x = 0
        if y <= 0: y = 0
        HORIZ = str(x)
        VERT = str(y)
        # Plot the user_string at the starting at position HORIZ, VERT...
        print("\033[" + VERT + ";" + HORIZ + "f" + txt)
        return self

    def up(self, n=1):
        """
            goes up the specified number of rows

        :param n: The number of rows to go up (a negative number goes down)
        :rtype: TerminalController
        """
        n = int(n)
        if n < 0:
            return self.down(-n)
        print("\033[" + str(n) + "A", end='')
        return self

    def down(self, n=1):
        """
            goes down the specified number of rows

        :param n: The number of rows to go down (a negative number goes up)
        :rtype: TerminalController
        """
        n = int(n)
        if n < 0:
            return self.up(-n)
        print("\033[" + str(n) + "B", end='')
        return self

    def left(self, n=1):
        """
            goes left the specified number of rows

        :param n: The number of rows to go up (a negative number goes right)
        :rtype: TerminalController
        """
        n = int(n)
        if n < 0:
            return self.right(-n)
        print("\033[" + str(n) + "D", end='')
        return self

    def right(self, n=1):
        """
            goes right the specified number of rows

        :param n: The number of rows to go up (a negative number goes left)
        :rtype: TerminalController
        """
        n = int(n)
        if n < 0:
            return self.left(-n)
        print("\033[" + str(n) + "C", end='')
        return self

    def bookmark(self):
        """
            saves current cursor position

        :rtype: TerminalController
        """
        print("\033[s", end='')
        return self

    def goto_bookmark(self):
        """
            goes to current bookmarked position (must use bookmark() before it)

        :rtype: TerminalController
        """
        print("\033[u", end='')
        return self

    def eraseToEOL(self):
        """
            erases all text from currnt location to the end of the line

        :rtype: TerminalController
        """
        print("\033[K", end='')
        return self

    def eraseToBOL(self):
        """
            erases all text from currnt location to the beginning of the line

        :rtype: TerminalController
        """
        print("\033[1K", end='')
        return self

    def eraseLine(self):
        """
            erases all text from currnt line

        :rtype: TerminalController
        """
        print("\033[2K", end='')
        return self

    def eraseUp(self):
        """
            erases all text from currnt line to the beginning of the screen

        :rtype: TerminalController
        """
        print("\033[1J", end='')
        return self

    def eraseDown(self):
        """
            erases all text from currnt line to the end of the screen

        :rtype: TerminalController
        """
        print("\033[J", end='')
        return self

    # TODO Add Tab control support (http://www.termsys.demon.co.uk/vtansi.htm)

    def set_attributes(self, color="keep", background="keep", attrib="keep"):

        """
            sets the text attributes to be used by new prints. a value of "keep" keeps the current set

        :param color: one of ['black','red','green','yellow','blue','magenta','cyan','white']
        :param background: one of ['black','red','green','yellow','blue','magenta','cyan','white']
        :param attrib: one of ['bright','dim','underscore','blink','reverse','hidden']
        :rtype: TerminalController
        """
        color = color.lower()
        background = background.lower()
        attrib = attrib.lower()
        att = []
        clrlst = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        attlst = ['bright', 'dim', 'underscore', 'blink', 'reverse', 'hidden']
        if color == "keep":
            pass
        else:
            clr = clrlst.index(color)
            if clr > 0:
                clr = clr + 30
                att.append(clr)

        if background == "keep":
            pass
        else:
            clr = clrlst.index(background)
            if clr > 0:
                clr = clr + 40
                att.append(clr)

        if attrib == "keep":
            pass
        else:
            clr = attlst.index(background)
            if clr > 0:
                clr = clr + 1
                att.append(clr)

        to_print = "\033["
        nothingAdded = len(att) < 1
        for a in att:
            to_print = to_print + str(a) + ';'
        if nothingAdded:
            return self
        to_print = to_print[:-1]
        to_print = to_print + "m"
        print(to_print, end='')
        return self

    def color(self, color="keep"):
        """
            sets the text foreground color

        :param color: one of ['black','red','green','yellow','blue','magenta','cyan','white']
        :rtype: TerminalController
        """
        return self.set_attributes(color=color)

    def set_foreground(self, color="keep"):
        """
        sets the text foreground color

        :param color: one of ['black','red','green','yellow','blue','magenta','cyan','white']
        :rtype: TerminalController
                """
        return self.color(color=color)

    def background(self, background='keep'):
        """
            sets the text background color

        :param background: one of ['black','red','green','yellow','blue','magenta','cyan','white']
        :rtype: TerminalController
        """
        return self.set_attributes(background=background)

    def set_background(self, background='keep'):
        """
            sets the text background color

        :param background: one of ['black','red','green','yellow','blue','magenta','cyan','white']
        :rtype: TerminalController
        """
        return self.background(background=background)

    def attrib(self, attrib='keep'):
        """
            sets the text attributes

        :param attrib: one of ['bright','dim','underscore','blink','reverse','hidden']
        :rtype: TerminalController
        """
        return self.set_attributes(attrib=attrib)

    def set_attribute(self, attrib='keep'):
        """
            sets the text attributes

        :param attrib: one of ['bright','dim','underscore','blink','reverse','hidden']
        :rtype: TerminalController
        """
        return self.attrib(attrib=attrib)

    def reset_attributes(self):
        """
            resets all text attributes to their defaults

        :rtype: TerminalController
        """
        print("\033[0m", end='')

    def print(self, *args, **kwargs):
        print(*args, **kwargs)
        return self


def humanize_time(secs, align=False, always_show_all_units=False):
    '''
    Prints time that is given as seconds in human readable form. Useful only for times >=1sec.

    :param secs float: number of seconds
    :param align bool, optional: whether to align outputs so that they all take the same size (not implemented)
    :param always_show_all_units bool, optional: Whether to always show days, hours, and minutes even when they
                                are zeros. default False
    :return: str formated string with the humanized form
    '''
    units = [("d", 86400), ("h", 3600), ("m", 60), ("s", 1)]
    parts = []
    for unit, mul in units:
        if secs / mul >= 1 or mul == 1 or always_show_all_units:
            if mul > 1:
                n = int(math.floor(secs / mul))
                secs -= n * mul
            else:
                n = secs if secs != int(secs) else int(secs)
            if align:
                parts.append("%2d%s%s" % (n, unit, ""))
            else:
                parts.append("%2d%s%s" % (n, unit, ""))
    return ":".join(parts)


def print_progress(iteration, total, prefix='', suffix='', decimals=2, barLength=50, limit_range=True):
    """
    Call in a loop to create terminal progress bar

    :param iteration int: current iteration
    :param total int: total iterations
    :param prefix str: prefix string
    :param suffix str: suffix string
    :param decimals int: positive number of decimals in percent complete
    :param barLength int: character length of bar
    """
    if total is None:
        total = 1.0
    if iteration is None:
        iteration = 0.0
    boundary_error = 0
    percent = 0
    if decimals > 0:
        formatStr = "{:>6." + str(decimals) + "f}"
        percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    if limit_range:
        if filledLength < 0:
            boundary_error = 1
            filledLength = 0
        if filledLength > barLength:
            boundary_error = 2
            filledLength = barLength
    bar = '#' * filledLength + '-' * (barLength - filledLength)  # █
    if decimals > 0:
        sys.stdout.write('\r\033[2K%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix))
    else:
        sys.stdout.write('\r\033[2K%s |%s| %s' % (prefix, bar, suffix))
    sys.stdout.flush()
    return boundary_error


class ProgressBarController(object):
    '''
    A set of progress bars.

    A set of progress bars with custom pre and post text. It is mostly useful when you have several running threads or
    suprocesses and each needs its own bar. It allows prefixes and postfixes that can be changed using the following tags:
    <name> bar name
    <remaining> remaining time to completion estimate
    <activity> An indicator that the process represented by the bar is active

    '''
    _terminal = TerminalController()
    barNames = None
    current = None
    begTime = None
    activityChars = ['.   ', ' .  ', '  . ', '   .', '  . ', ' .  ', '.   ']
    last_name_updated = None
    last_i = None
    last_n = None
    running_color = 'yellow'
    running_background = 'black'
    completed_color = 'green'
    completed_background = 'black'
    over_complete_color = 'red'
    over_complete_background = 'black'
    under_complete_color = 'red'
    under_complete_background = 'black'

    def __init__(self, barNames=None, barLength=50, align_bars=True):
        """
        Creates the set of progress bars.

        :param barNames: array_like: list of bar names
        :param barLength: int: Length of bar in spaces on screen
        :param align_bars: bool: whether or not to align all bars to start together and end together. Default True
        """
        if barNames is None:
            barNames = []
        self.barNames = barNames
        self.current = [0.0] * len(barNames)
        self.start_timing(None)
        self.barLength = barLength
        self.count = [-1] * len(barNames)
        self.activity = [0] * len(barNames)
        self.align_bars = align_bars
        self.last_skip_rows = None
        pass

    def _indexOfBar(self, name):
        try:
            b = self.barNames.index(name)
        except:
            return -1
        return b

    def add_bar(self, name: str, *, i: float = 0, n: float = 0, start_timing: bool = True):
        """Adds a bar

        Can control the name, starting progress (i) and total progress

        Args:
            name (str): name of bar

        Kwargs:
            i (int): current progress
            n (int): total progress
            start_timing (bool or None): Starts a timer for this bar, otherwise it uses the begTime member which
                                        is common to all bars

        Returns:
            self

        Remarks:

        """
        self.barNames.append(name)
        if n > 0:
            self.current.append(float(i) / float(n))
        else:
            self.current.append(None)
        self.count.append(n)
        self.activity.append(0)
        self.begTime.append(time.perf_counter() if start_timing
                            else (self.begTime[0]
                                  if len(self.begTime) > 0
                                  else 0))
        return self

    def remove_bar(self, name):
        """Removes a bar given its name

        Args:
            name (str): bar name

        Returns:
            self
        """
        i = self._indexOfBar(name)
        if i >= 0:
            self.barNames.pop(i)
            self.current.pop(i)
            self.begTime.pop(i)
            self.count.pop(i)
            self.activity.pop(i)
        return self

    def start_timing(self, forNames=None):
        """Starts timing for ETA calculation for the given bar names

        Args:
            forNames (str or None): The list of bar names. If None (Default), the beginning time of all bars is set to
                                now

        Returns:
            self
        """
        begTime = time.perf_counter()
        if forNames is None:
            self.begTime = [begTime] * len(self.barNames)
        else:
            for name in forNames:
                i = self._indexOfBar(name)
                if i >= 0:
                    self.begTime[i] = begTime
        return self

    def set_progress(self, name: str, i: int, n: int = None):
        """Sets progress for a specific bar, optionally setting its limit as well

        Args:
            name (str):  bar name
            i (int): current progress
            n (int or None): Limit (optional)

        Returns:
            self
        """
        b = self._indexOfBar(name)
        if b >= 0:
            if n is None:
                n = self.count[b]
            if n > 0:
                self.current[b] = float(i) / float(n)
            else:
                self.current[b] = 1.0

            self.last_name_updated = name
            self.last_i = i
            self.last_n = n
        return self

    def get_remaining_time(self, name):
        """Gets the time remaining till the end of execution (only an estimate)

        Args:
            name: bar name

        Returns:
            int: remaining time (ETA)
        """
        b = self._indexOfBar(name)
        if b < 0:
            return -1
        current = self.current[b]
        if current is None:
            return -1
        if current > 1.0:
            return 0
        remaining = (time.perf_counter() - self.begTime[b]) * (1 - current + 0.0005) / (current + 0.0005)
        return remaining

    def _get_max_name_length(self):
        n = len(max(self.barNames, key=len))
        if n == 0:
            return 10
        return n

    def _replace_tags(self, input, name):
        remaining = self.get_remaining_time(name)
        if remaining < 0:
            remaining = 'ETA: unknown'
        else:
            remaining = 'ETA: {}'.format(humanize_time(remaining, align=True, always_show_all_units=True))
        fmt = "{:<" + str(self._get_max_name_length()) + "}"
        input = input.replace('<name>', fmt.format(name))
        input = input.replace('<remaining>', remaining)
        b = self._indexOfBar(name)
        if input.find('<activity>') > -1:
            activity = 0
            if b >= 0:
                activity = self.activity[b]
                self.activity[b] = (self.activity[b] + 1) % len(self.activityChars)
            input = input.replace('<activity>', self.activityChars[activity])
        return input

    def activate(self, name: str = None):
        """Indicate that the given bar is active. If name is None, all bars are indicated to be active by progressing

        Args:
            name (str): bar name. If None is given then all bars are set to be active

        Returns:
            self
        """
        if name is None:
            for name in self.barNames:
                self.activate(name)
        b = self._indexOfBar(name)
        if b >= 0:
            self.activity[b] = (self.activity[b] + 1) % len(self.activityChars)
        return self

    def show(self, name=None, prefix='<name>', suffix='<remaining>', bar_length=-1, from_line_beginning=True):
        """Shows a specific bar just in the current place on the screen. We should have a new line before it

        Args:
            name (str or None): name of the bar
            prefix (str): prefix to write before the bar (see the class doc string for possible tag values)
            suffix (str): postfix (see prefix)
            bar_length (int): Bar length, if less than zero then the current length set during creation of the bar or
                        latest setting of its progess will be used.
            from_line_beginning (bool): If true, a '\r' and flushing will be outputed to set the bar to the beginning
                            of the line

        Returns:
            self
        """
        try:
            if name is None:
                return self.show_all(barname=None, prefix=prefix, suffix=suffix, bar_length=bar_length)
            b = self._indexOfBar(name)
            if b < 0:
                return self
            if prefix is not None:
                prefix = self._replace_tags(prefix, name)
            if suffix is not None:
                suffix = self._replace_tags(suffix, name)
            if from_line_beginning:
                sys.stdout.write('\r')
                sys.stdout.flush()
            c = self.current[b]
            if c is None:
                c = 0.0

            if c < 0:
                self._terminal.color(self.under_complete_color)
                self._terminal.background(self.under_complete_background)
            elif c > 1.00001:
                self._terminal.color(self.over_complete_color)
                self._terminal.background(self.over_complete_background)
            elif c > 0.99999999999:
                self._terminal.color(self.completed_color)
                self._terminal.background(self.completed_background)
            else:
                self._terminal.color(self.running_color)
                self._terminal.background(self.running_background)

            print_progress(self.current[b], 1, prefix=prefix, suffix=suffix
                           , barLength=bar_length if bar_length > 0 else self.barLength)
            self._terminal.reset_attributes()
        except:
            pass
        return self

    def show_all(self, barname=None, i=None, n=None, clean_screen=True, prefix='<name><activity>', suffix='<remaining>',
                 bar_length=-1, skip_rows=0):
        """
        Shows a specific bar or all bars, possibly cleaning the screen.

        Args:
            barname (str or None): name of the bar
            i (int or None): optional progress value
            n (int or None): optional maximum value for the bar
            clean_screen (bool): Whether or not to clean the screen before drawing. Default is true
            prefix (str): prefix to write before the bar (see the class doc string for possible tag values)
            suffix (str): postfix (see prefix)
            bar_length (int): Bar length, if less than zero then the current length set during creation of the bar or
                        latest setting of its progess will be used.
            skip_rows (int): the number of lines to skip between bars
            from_line_beginning (bool): If true, a '\r' and flushing will be outputed to set the bar to the beginning
                            of the line

        Returns:
            self

        Remarks:

        """
        try:
            if clean_screen:
                self._terminal.clear().home().left()
            if barname is not None:
                self.set_progress(barname, i, n)
            self.last_skip_rows = skip_rows
            for name in self.barNames:
                self.show(name, prefix=prefix, suffix=suffix, bar_length=bar_length)
                sys.stdout.write('\n')
                for r in range(skip_rows):
                    sys.stdout.write('\n')
                sys.stdout.flush()
        except:
            pass
        return self

    def _indicateError(self):
        pass

    def terminal(self) -> TerminalController:
        """Gets the built-in `TerminalController` object

        Returns:
            TerminalController
        """
        return self._terminal

    def update(self, name: str or None = None, i: t.Optional[int] = None, n: t.Optional[int] = None
               , prefix: str = '<name><activity>', suffix: str = '<remaining>', bar_length: int = -1):
        """
        Updates the progress value of a given bar and shows all the bars in their relative positions

        Args:
            name (str): bar name
            i (int or None): optional progress value
            n (int or None): optional maximum value for the bar
            clean_screen (bool): Whether or not to clean the screen before drawing. Default is true
            prefix (str): prefix to write before the bar (see the class doc string for possible tag values)
            suffix (str): postfix (see prefix)
            bar_length (int): Bar length, if less than zero then the current length set during creation of the bar or
                        latest setting of its progess will be used.

        Returns:
            self
        """

        try:
            if self.last_skip_rows is None:
                self.show_all(name, i, n, prefix=prefix, suffix=suffix, bar_length=bar_length)
                return self
            if name is None:
                if self.last_name_updated is None:
                    self._indicateError()
                    return self
                name = self.last_name_updated
            if i is None:
                i = self.last_i
            if n is None:
                n = self.last_n
            b = self._indexOfBar(name)
            if b < 0:
                self._indicateError()
                return self
            if i is not None and n is not None and name is not None:
                self.set_progress(name, i, n)
            loc = 1 + (self.last_skip_rows + 1) * b
            self._terminal.goto(0, loc)
            self.show(name, prefix=prefix, suffix=suffix, bar_length=bar_length)

            self._terminal.goto(0, 1 + (self.last_skip_rows + 1) * len(self.barNames))
        except:
            pass
        return self

    def show_in_position(self, name=None, prefix='<name><activity>', suffix='<remaining>', bar_length=-1):
        """
        Shows the named bar in its appropriate position without touching anything else in the screen

        Args:
            name (str): bar name
            clean_screen (bool): Whether or not to clean the screen before drawing. Default is true
            prefix (str): prefix to write before the bar (see the class doc string for possible tag values)
            suffix (str): postfix (see prefix)
            bar_length (int): Bar length, if less than zero then the current length set during creation of the bar or
                        latest setting of its progress will be used.

        Returns:
            self
        """
        try:
            if self.last_skip_rows is None:
                self._indicateError()
                return self
            if name is None:
                if self.last_name_updated is None:
                    self._indicateError()
                    return self
                name = self.last_name_updated
            b = self._indexOfBar(name)
            if b < 0:
                self._indicateError()
                return self
            loc = 1 + (self.last_skip_rows + 1) * b
            self._terminal.goto(0, loc)
            self.show(name, prefix=prefix, suffix=suffix, bar_length=bar_length)

            self._terminal.goto(0, 1 + (self.last_skip_rows + 1) * len(self.barNames))
        except:
            pass
        return self


if __name__ == '__main__':
    import pytest

    pytest.main()
