# import this into lldb with a command like
# command script import delbrc.py
# https://stackoverflow.com/a/28532079

import lldb


def delbrc(debugger, command, *args):
    """
    Usage: delbrc
    Disables the breakpoint the currently selected thread is stopped at.
    """

    target = None
    thread = None

    if len(args) == 2:
        # Old lldb invocation style
        result = args[0]
        if debugger and debugger.GetSelectedTarget() and debugger.GetSelectedTarget().GetProcess():
            target = debugger.GetSelectedTarget()
            process = target.GetProcess()
            thread = process.GetSelectedThread()

    elif len(args) == 3:
        # New (2015 & later) lldb invocation style where we're given the execution context
        exe_ctx = args[0]
        result = args[1]
        target = exe_ctx.GetTarget()
        thread = exe_ctx.GetThread()
    else:
        print("Unknown python function invocation from lldb.")
        return

    if thread == None:
        print("ERROR - process is not paused, or has not been started yet.", file=result)
        result.SetStatus(lldb.eReturnStatusFailed)
        return

    if thread.GetStopReason() != lldb.eStopReasonBreakpoint:
        print("ERROR - not stopped at a breakpoint.", file=result)
        result.SetStatus(lldb.eReturnStatusFailed)
        return

    if thread.GetStopReasonDataCount() != 2:
        print("ERROR - Unexpected number of StopReasonData returned, expected 2, got %d" %
              thread.GetStopReasonDataCount(), file=result)
        result.SetStatus(lldb.eReturnStatusFailed)
        return

    breakpoint_count = thread.GetStopReasonDataAtIndex(0)
    location_count = thread.GetStopReasonDataAtIndex(1)

    if breakpoint_count == 0 or location_count == 0:
        print("ERROR - Got invalid breakpoint number or location number", file=result)
        result.SetStatus(lldb.eReturnStatusFailed)
        return

    bkpt = target.FindBreakpointByID(breakpoint_count)
    if location_count > bkpt.GetNumLocations():
        print("ERROR - Invalid location number", file=result)
        result.SetStatus(lldb.eReturnStatusFailed)
        return

    breakpoint_loc = bkpt.GetLocationAtIndex(location_count - 1)
    if breakpoint_loc.IsValid() != True:
        print("ERROR - Got invalid BreakpointLocation", file=result)
        result.SetStatus(lldb.eReturnStatusFailed)
        return

    breakpoint_loc.SetEnabled(False)
    # continue running
    thread.process.Continue()
    print("Breakpoint %d.%d disabled." %
          (breakpoint_count, location_count), file=result)
    return


def __lldb_init_module(debugger, dict):
    debugger.HandleCommand(
        'command script add -f %s.delbrc delbrc' % __name__)
