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
        print("error: process is not paused, or has not been started yet.", file=result)
        result.SetStatus(lldb.eReturnStatusFailed)
        return

    if thread.GetStopReason() != lldb.eStopReasonBreakpoint:
        print("error: not stopped at a breakpoint.", file=result)
        result.SetStatus(lldb.eReturnStatusFailed)
        return

    if thread.GetStopReasonDataCount() != 2:
        print("error: Unexpected number of StopReasonData returned, expected 2, got %d" %
              thread.GetStopReasonDataCount(), file=result)
        result.SetStatus(lldb.eReturnStatusFailed)
        return

    break_num = thread.GetStopReasonDataAtIndex(0)
    location_num = thread.GetStopReasonDataAtIndex(1)

    if break_num == 0 or location_num == 0:
        print("error: Got invalid breakpoint number or location number", file=result)
        result.SetStatus(lldb.eReturnStatusFailed)
        return

    bkpt = target.FindBreakpointByID(break_num)
    if location_num > bkpt.GetNumLocations():
        print("error: Invalid location number", file=result)
        result.SetStatus(lldb.eReturnStatusFailed)
        return

    bkpt_loc = bkpt.GetLocationAtIndex(location_num - 1)
    if bkpt_loc.IsValid() != True:
        print("error: Got invalid BreakpointLocation", file=result)
        result.SetStatus(lldb.eReturnStatusFailed)
        return

    bkpt_loc.SetEnabled(False)
    print("Breakpoint %d.%d disabled." %
          (break_num, location_num), file=result)
    return


def __lldb_init_module(debugger, dict):
    debugger.HandleCommand(
        'command script add -f %s.delbrc delbrc' % __name__)
